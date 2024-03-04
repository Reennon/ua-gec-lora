from typing import Union

import streamlit as st
from langchain.memory import ConversationSummaryBufferMemory, RedisChatMessageHistory

from src.packages.chains.conversational_gec_chain import ConversationalGecChain
from src.packages.constants.environ_constants import EnvironConstants
from src.packages.constants.messages_constants import MessagesConstants
from src.packages.llms.gemma7b import Gemma7b
from src.packages.prompts.converstional_gec_prompts import ConversationalGecPromptWithMemory, \
    ConversationalGecPromptWithoutMemory
from src.packages.sessions.session_manager import SessionManager
from src.packages.utils.parameter_server import ParameterServer


class ChainController:
    LLM = Gemma7b

    def __init__(
        self,
        st_memory: Union[ConversationSummaryBufferMemory, None],
        st_first_question: Union[ConversationSummaryBufferMemory, None],
    ):
        self.parameter_server = ParameterServer()
        self.environ_constants = EnvironConstants()
        self.session_manager = SessionManager()

        # region LLMs Parameters

        self.memory_parameters = self.parameter_server.settings.memory_model

        # endregion

        st.session_state.memory = self.memory = st_memory if st_memory else self._construct_memory()
        st.session_state.is_first_question = self.is_first_question = st_first_question if st_first_question else False

        self.chain_with_memory = self._construct_chain_with_memory(memory=self.memory)
        self.chain_without_memory = self._construct_chain_without_memory(memory=self.memory)

    def _construct_memory(self) -> ConversationSummaryBufferMemory:
        memory = ConversationSummaryBufferMemory(
            llm=self.LLM.construct_llm(**self.memory_parameters),
            memory_key='chat_history',
            input_key='query',
            output_key='answer',
            return_messages=True,
            # Max tokens in buffer memory has to be larger than model's to accommodate for memory pruning
            max_token_limit=self.memory_parameters.max_tokens,
            chat_memory=RedisChatMessageHistory(
                session_id=self.session_manager.session_id,
                url=self.environ_constants.REDIS_URL,
            )
        )

        return memory

    def _construct_chain_without_memory(
            self,
            memory: ConversationSummaryBufferMemory,
    ) -> ConversationalGecChain:
        conversational_api_chain_without_memory: ConversationalGecChain = ConversationalGecChain(
            prompt=ConversationalGecPromptWithoutMemory.PROMPT,
            llm=self.LLM.construct_llm(**self.memory_parameters),
            memory=memory,
        )

        return conversational_api_chain_without_memory

    def _construct_chain_with_memory(
        self,
        memory: ConversationSummaryBufferMemory,
    ) -> ConversationalGecChain:
        conversational_api_chain_with_memory: ConversationalGecChain = ConversationalGecChain(
            prompt=ConversationalGecPromptWithMemory.PROMPT,
            llm=self.LLM.construct_llm(**self.memory_parameters),
            memory=memory,
        )

        return conversational_api_chain_with_memory

    async def __call__(self, query: str) -> dict[str, str]:
        chain: ConversationalGecChain = \
            self.chain_without_memory if self.is_first_question else self.chain_without_memory

        response: dict[str, str] = await chain.acall({
            'query': query,
            'not_relevant_output': MessagesConstants.NOT_RELEVANT_QUERY,
            'chat_history': self.memory.chat_memory,
        })

        return response

