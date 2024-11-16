import uuid
import reflex as rx

from frontend.states.filters_state import FilterState
from frontend.states.models.messages import Message, FinishReason
from frontend.states.query_state import QueryState
from frontend.utils.openai_controller import OpenAIHelper


class SettingsState(rx.State):
    color: str = "violet"
    font_family: str = "Poppins"


class ChatState(rx.State):
    question: str
    processing: bool = False

    # Keep track of the chat history as a list of (question, answer) tuples.
    chat_history: list[Message] = []
    user_id: str = str(uuid.uuid4())

    async def answer(self):

        self.processing = True
        yield

        question = self.question
        self.question = ''
        yield

        self.chat_history.append(Message.user_message(content=question))

        chat_history_dicts = []
        for message in self.chat_history:
            if message.type != FinishReason.FUNCTION_CALL:
                chat_history_dicts.append(
                    {"role": message.role, "content": message.content}
                )

        openai_helper = OpenAIHelper.get_openai_api_controller()
        response, args, function_call_content = openai_helper.generate_response(chat_history_dicts)

        if function_call_content is not None:
            query_state: rx.State = await self.get_state(QueryState)
            query_state.set_text(response)

            filter_state: rx.State = await self.get_state(FilterState)
            filter_state.set_form_data(args)

            self.chat_history.append(Message.assistant_message(content=function_call_content,
                                                               finish_reason=FinishReason.FUNCTION_CALL))

            yield QueryState.search('enter')
        else:
            self.chat_history.append(Message.assistant_message(content=response,
                                                               finish_reason=FinishReason.STOP_TOKEN))

        self.processing = False

    async def handle_key_down(self, key: str):
        if key == "Enter":
            return self.answer()

    def clear_chat(self):
        # Reset the chat history and processing state
        self.chat_history = []
        self.processing = False
