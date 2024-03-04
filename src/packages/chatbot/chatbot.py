import time

import streamlit as st

from src.packages.chain_controllers.chain_controller import ChainController
from src.packages.constants.messages_constants import MessagesConstants, Roles
from src.packages.utils.parameter_server import ParameterServer


class Chatbot:
    """
    A class for creating frontend Streamlit Chatbot.
    """


    def __init__(self):
        self.__initialize_session_state()

        self.parameter_server = ParameterServer()

    @staticmethod
    def __initialize_session_state() -> None:
        default_values: dict[str, object] = {
            'messages': [{"role": Roles.ASSISTANT.value, "content": MessagesConstants.DEFAULT_CHATBOT_MESSAGE}],
            'user_input': None,
            'memory': None,
            'is_first_question': None,
            'session_id': None
        }

        for key, value in default_values.items():
            st.session_state.setdefault(key, value)

    async def app(self) -> None:
        """
        Run the chatbot application.
        """

        st.title("💬 Ukrainian GEC ChatBot")

        for message in st.session_state.messages:
            with st.chat_message(message.get("role")):
                st.markdown(message.get("content"))

        if prompt := st.chat_input("What is up?"):
            # Add user message to chat history
            st.session_state.messages.append({"role": Roles.USER.value, "content": prompt})
            # Display user message in chat message container
            with st.chat_message(Roles.USER.value):
                st.markdown(prompt)
                st.session_state.user_input = prompt # None if st.session_state.user_input == prompt else prompt
            # Display assistant response in chat message container
            with st.chat_message(Roles.ASSISTANT.value):
                with st.spinner("Thinking..."):
                    message_placeholder = st.empty()
                    full_response = ""
                    query: str = st.session_state.user_input

                    st_memory = st.session_state.memory
                    st_first_question = st.session_state.is_first_question
                    chain = ChainController(
                        st_memory=st_memory,
                        st_first_question=st_first_question,
                    )
                    response = await chain(query=query)

                    for answer in response.get('answer').split(" "):
                        full_response += answer + " "
                        time.sleep(0.05)
                        message_placeholder.markdown(full_response + "▌")

                    message_placeholder.markdown(full_response)

            st.session_state.messages.append({"role": Roles.ASSISTANT.value, "content": full_response})
