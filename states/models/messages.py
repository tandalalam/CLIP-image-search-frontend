from enum import Enum
import reflex as rx


class Role(Enum):
    USER = 'user'
    ASSISTANT = 'assistant'


class FinishReason(Enum):
    FUNCTION_CALL = 'function_call'
    STOP_TOKEN = 'stop_token'
    USER_MESSAGE = 'user_message'


class Message(rx.Base):
    content: str
    role: Role
    type: FinishReason

    @classmethod
    def user_message(cls, content: str):
        return cls(content=content, type=FinishReason.USER_MESSAGE, role=Role.USER)

    @classmethod
    def assistant_message(cls, content: str, finish_reason: FinishReason):
        return cls(content=content, type=finish_reason, role=Role.ASSISTANT)
