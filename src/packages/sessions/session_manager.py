import streamlit as st
from uuid import uuid4


class SessionManager:
    @property
    def session_id(self):
        st.session_state.session_id = str

        return st.session_state.session_id

    @session_id.getter
    def session_id(self):
        if not st.session_state.session_id:
            st.session_state.session_id = str(uuid4())

        return st.session_state.session_id
