# Flesch or Fumble? Evaluating Readability Standard Alignment of Instruction-Tuned Language Models

This repository hosts the code and data used for the [GEM Workshop 2023 paper](https://arxiv.org/abs/2309.05454) "Flesch or Fumble? Evaluating Readability Standard Alignment of Instruction-Tuned Language Models" by Joseph Imperial and Harish Tayyar Madabushi.

### What is Readability Standard Alignment?
Readability Standard Alignment is the task proposed in the paper evaluating the capability of instruction-tuned large language models (listed below) to capture the correct readability levels of generated texts with respect to specifications provided in the prompts. In the paper, we use enrich prompts iteratively with details from the [Flesch Kincaid Grade Level](https://en.wikipedia.org/wiki/Flesch%E2%80%93Kincaid_readability_tests) and [CEFR] Framework (https://www.coe.int/en/web/common-european-framework-reference-languages/level-descriptions) to see if there are improvements with aligning to the target reading level specified. We do this for two tasks: `prompt-based story completion` and `prompt-based narrative simplification`. Read the paper for the outcomes of the experiments.

### Models Evaluated
1. ChatGPT (GPT-3.5 Turbo)
2. Llama-7B
3. FlanT5-250M
4. BLOOMZ-3B
5. LongForm T5 XL-3B
6. Dolly-3B

### Data
The data folder contains the generated texts per model per task. Please read the dedicated sections on the paper for the generation specifications used per task.

### Code
The code folder contains the various scripts used for prompting the instruction-tuned models used to generate story completions or simplifications.

### Contact
If you need any help reproducing the results, please don't hesitate to contact me below:

**Joseph Marvin Imperial** <br/>
jmri20@bath.ac.uk <br/>
www.josephimperial.com 
