from langchain.prompts import PromptTemplate


class InstructionTuningGecPrompts:
    """Define instructions for the LLM to generate proper answer during PeFT tuning."""
    template = """Given ("SOURCE") text, correct errors if present, fulfilling GEC (Grammar Error Correction) Task for Ukrainian Language.
Use following set of errors ("ERROR_TYPES"):
{error_types}
If you would detect error ("ERROR"), generate correction ("CORRECTION") following the structure and specifying error type ("ERROR_TYPE"):
{{("ERROR")=>("CORRECTION"):::("ERROR_TYPE")}}
Otherwise keep original text.

SOURCE: {query}
ERROR_TYPES: {error_types}
FINAL ANSWER:"""

    PROMPT = PromptTemplate(
        template=template,
        input_variables=['query', 'error_types']
    )
