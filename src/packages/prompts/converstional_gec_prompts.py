from langchain import PromptTemplate


class ConversationalGecPromptWithoutMemory:
    template = """Given a ("QUERY") respond to query ("QUERY") based on the Grammar Error Correction for Ukrainian Language 
If the query does not match the topic, just answer {not_relevant_output}

QUERY: {query}
FINAL ANSWER:"""

    PROMPT = PromptTemplate(
        template=template,
        input_variables=['query', 'not_relevant_output']
    )


class ConversationalGecPromptWithMemory:
    template = """Given a ("QUERY") and ("CHAT_HISTORY") respond to query ("QUERY") based on the Grammar Error Correction for Ukrainian Language 
If the query does not match the topic, just answer {not_relevant_output}

QUERY: {query}
CHAT_HISTORY: {chat_history}
FINAL ANSWER:"""

    PROMPT = PromptTemplate(
        template=template,
        input_variables=['query', 'chat_memory', 'not_relevant_output']
    )
