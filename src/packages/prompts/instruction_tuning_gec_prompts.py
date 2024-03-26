from langchain.prompts import PromptTemplate


class InstructionTuningGecPrompts:
    """Define instructions for the LLM to generate proper answer during PeFT tuning."""
    template = """Given ("SOURCE") text with errors, correct them if present, fulfilling GEC (Grammar Error Correction) Task for Ukrainian Language.
Consider following set of error types ("ERROR_TYPES"):
{error_types}
Throughout the text, if you would detect error ("ERROR"), fix it according to the structure:
{{("ERROR")=>("CORRECTION"):::("ERROR_TYPE")}}
Where ("CORRECTION") Specifies how the error should be corrected.
Keep the original text, only correcting errors in it, without outputting this instructions.

SOURCE: {query}
FINAL ANSWER:"""

    PROMPT = PromptTemplate(
        template=template,
        input_variables=['query', 'error_types']
    )
