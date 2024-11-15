import yaml
from os import environ
import re
from dotenv import load_dotenv
from loguru import logger


def load_yaml_file(path):
    with open(path, 'r') as stream:
        return yaml.safe_load(stream)


def parse_env_vars(value):
    path_matcher = re.compile(r'\$\{([^}^{]+)\}')
    match = path_matcher.match(value)
    if not match:
        return value
    env_var = match.group(1)
    return environ.get(env_var)


path_matcher = re.compile(r'\$\{([^}^{]+)\}')


def path_constructor(loader, node):
    """ Extract the matched value, expand env variable, and replace the match """
    value = node.value
    match = path_matcher.match(value)
    env_var = match.group()[2:-1]
    env_var = environ.get(env_var, None)
    return env_var + value[match.end():] if env_var is not None else None


class ConfigManager:
    config_manager = None

    @staticmethod
    def get_config_manager():
        if ConfigManager.config_manager is None:
            ConfigManager.config_manager = ConfigManager()
        return ConfigManager.config_manager

    def __init__(self, configuration_path='frontend/utils/configs/configuration.yaml'):
        load_dotenv('.env')

        yaml.add_implicit_resolver('!path', path_matcher)
        yaml.add_constructor('!path', path_constructor)

        with open(configuration_path, 'r') as stream:
            self.configs = yaml.load(stream, Loader=yaml.FullLoader)

    def get_prop(self, key):
        try:
            return self.configs[key]
        except KeyError:
            logger.error(f'Config key {key} not found')
            return None
