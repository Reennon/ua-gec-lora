UA-GEC LoRA
----

In this solution we researched the impact of LoRA fine-tuning method for LLMs; Test the impact, improvement on language understanding for 
grammar correction on non-english languages. In this solution we used UA-GEC dataset, presented by grammarly: https://github.com/grammarly/ua-gec 

The paper and dataset abstract can be checked here: https://www.grammarly.com/blog/engineering/ua-gec-2/ and here https://arxiv.org/pdf/2103.16997v2.pdf

### Installation

1. Install ua-gec package or dataset. \
We used `git submodule` in order to install it, follow the dataset's instructions, and do the
```shell
pip install ua-gec
```
Or, download a submodule, and install the `gec-ua` package from there:
```shell
git submodule add https://github.com/grammarly/ua-gec.git ./data/ua-gec && \
cd ./data/ua-gec/python && \
python setup.py develop  
```
2. Install necessary packages with __pip-install__
```shell
pip install -r requirements.txt
```
3. Download and unpack pickled (one or many) gguf file to use the LLM locally
    - Gemma 7b Instruct: https://huggingface.co/google/gemma-7b-it
    - Gemma 7b Pre-trained: https://huggingface.co/google/gemma-7b
    - Jaskier 7b DPO (Fine-tuned Mistral7B): https://huggingface.co/bardsai/jaskier-7b-dpo-v6.1 


### LLM Choise

For proper LLM we would need either to use Open-Source Multi-Language LLM, or extend the tokenizer for pre-existing English LLM, like _Mistral-7B_, in order for the model to understand ukrainian language. 

### Output
----

Generated corrected texts for documents in UA-GEC validation set are located in the [output folder](https://github.com/Reennon/ua-gec-lora/tree/master/output):
- [Mistral-7B without fine-tuning](https://github.com/Reennon/ua-gec-lora/blob/master/output/raw-model.txt)
- [Mistral-7B LoRA Fine-tuned on 500 samples from training set with r=4](https://github.com/Reennon/ua-gec-lora/blob/master/output/fine-tuned-r4-500.txt)

### Evaluation
----

Evaluation is implemented using [Errant](https://github.com/chrisjbryant/errant) taking [m2 file](https://github.com/osyvokon/unlp-2023-shared-task/blob/main/data/gec-only/valid.m2) from [UNLP-2023 Shared Task](https://github.com/osyvokon/unlp-2023-shared-task/tree/main) as the ground truth.

For more details please check [Erran Evaluation notebook](https://github.com/Reennon/ua-gec-lora/blob/master/notebooks/errant-evaluation.ipynb).

The metrics output looks the following way:
```
=========== Span-Based Correction ============
TP	FP	FN	Prec	Rec	F0.5
52	8024	1101	0.0064	0.0451	0.0078
==============================================


============ Span-Based Detection ============
TP	FP	FN	Prec	Rec	F0.5
351	7724	1033	0.0435	0.2536	0.0521
==============================================
```

Correction F0.5 is the primary metric used to compare models. To get a true positive (TP), the edit must match at least one of the annotators' edits exactly -- both the span and the suggested text.

To get a TP in span-based detection, it is enough to correctly identify erroneous tokens. The actual correction doesn't matter here.
