import asyncio

import streamlit as st
from src.packages.chatbot.chatbot import Chatbot


async def main():
    st.set_page_config(page_title="💬 UA-GEC Chat")
    chatbot_app = Chatbot()
    await chatbot_app.app()

if __name__ == '__main__':
    loop = asyncio.new_event_loop()
    loop.run_until_complete(main())
