from enum import Enum, unique


class MessagesConstants:
    DEFAULT_CHATBOT_MESSAGE: str = "Hi, How can I help you?"
    NOT_RELEVANT_QUERY: str = "Unfortunately I couldn't find any relevant information to your question in the app " \
                              "documentation. Please reformulate or elaborate your question, so I could help you."


@unique
class Roles(Enum):
    ASSISTANT: str = 'assistant'
    USER: str = 'user'
