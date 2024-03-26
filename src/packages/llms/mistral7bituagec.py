import os
from typing import Optional, List, Any, Mapping

from langchain.callbacks.manager import CallbackManagerForLLMRun
from langchain.llms.base import LLM
from langchain.llms.llamacpp import LlamaCpp

from src.packages.constants.path_constants import PathConstants


class Mistral7BITUAGEC(LLM):
    llama_cpp_model: LlamaCpp

    @property
    def _llm_type(self) -> str:
        return "mistral-7b-it-ua-gec"

    def _call(
        self,
        prompt: str,
        stop: Optional[List[str]] = None,
        run_manager: Optional[CallbackManagerForLLMRun] = None,
        **kwargs: Any,
    ) -> str:
        prompt = prompt.format(task=prompt)
        output = self.llama_cpp_model(prompt=prompt, stop=stop, **kwargs)

        return output

    @property
    def _identifying_params(self) -> Mapping[str, Any]:
        """Get the identifying parameters."""
        return {"llama_cpp_model": self.llama_cpp_model}

    @staticmethod
    def construct_llm(**kwargs) -> LLM:
        path_constants = PathConstants()

        model_parameters: dict = kwargs
        model_name: str = model_parameters.get('model_name')
        model_path: str = os.path.join(path_constants.MODELS_FOLDER, model_name)

        llm = Mistral7BITUAGEC(
            llama_cpp_model=LlamaCpp(
                model_path=model_path,
                f16_kv=True,  # MUST set to True, otherwise you will run into problem after a couple of calls
                verbose=True,  # Verbose is required to pass to the callback manager
                **model_parameters,
            )
        )

        return llm
