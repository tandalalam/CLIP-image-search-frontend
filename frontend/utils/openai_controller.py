import json
import httpx
from openai import OpenAI
from frontend.utils.configs.configs import ConfigManager


class OpenAIHelper:
    openai_helper = None

    @staticmethod
    def get_openai_api_controller():
        if OpenAIHelper.openai_helper is None:
            openai_configs = ConfigManager.get_config_manager().get_prop('openai_configs')
            OpenAIHelper.openai_helper = OpenAIHelper(openai_configs)
        return OpenAIHelper.openai_helper

    def __init__(self, openai_configs):
        with open('frontend/utils/model_instruction.md') as f:
            self.instruction = f.read()

        with open('frontend/utils/search_function.json') as f:
            self.function_spec = json.load(f)

        openai_configs = {k: v for k, v in openai_configs.items() if v is not None}
        http_client = None
        if 'proxy' in openai_configs:
            http_client = httpx.Client(proxies=openai_configs['proxy'])
            del openai_configs['proxy']
        self.openai_client = OpenAI(**openai_configs, http_client=http_client)

    def generate_response(self, conversation: list[dict]):

        data = {
            "model": 'gpt-4o',
            "messages": [
                {
                    "role": "system",
                    "content": self.instruction
                },
                *conversation
            ],
            "temperature": 0.5,
            "tools": [self.function_spec],
            "tool_choice": "auto"
        }

        resp = self.openai_client.chat.completions.create(
            **data
        ).choices[0].message

        if dict(resp).get('tool_calls'):
            function_args = json.loads(resp.tool_calls[0].function.arguments)
            search_term = function_args.pop('text')
            return search_term, dict(**function_args), resp.content
        else:
            return resp.content, {}, None
