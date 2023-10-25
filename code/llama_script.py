# Copyright (c) Meta Platforms, Inc. and affiliates.
# This software may be used and distributed according to the terms of the GNU General Public License version 3.

import fire
import pandas as pd
import numpy as np

from llama import Llama


def generate_llama2(prompt_list, instruction, generator, max_gen_len, temperature, top_p):
    llama2_continuations = []

    for item in prompt_list:
        full_instruction = instruction + "\n\n" + item #append instruction and story prompt

        results = generator.text_completion(
            [full_instruction],
            max_gen_len=max_gen_len,
            temperature=temperature,
            top_p=top_p,
        )

        output_decoded = results[0]['generation'].replace(full_instruction,'')
        llama2_continuations.append(output_decoded)
    return llama2_continuations


def main(
    ckpt_dir: str,
    tokenizer_path: str,
    temperature: float = 1.0,
    top_p: float = 0.95,
    max_gen_len: int = 300,
    max_batch_size: int = 2,
):
    generator = Llama.build(
        ckpt_dir=ckpt_dir,
        tokenizer_path=tokenizer_path,
        max_seq_len=max_seq_len,
        max_batch_size=max_batch_size,
    )

    # Read file with prompts
    edia_df = pd.read_csv("edia_prompt_continuation_equalized.csv")
    prompt_list = edia_df['prompt'].tolist()

    # Instruction List
    instruct_story_dict = {
        "level1": "Write a story using the following prompt: ",
        "level2_fkg": "Write a story that is readable by Grade 2 learners using the following prompt: ",
        "level2_cefr": "Write a story that is readable by A2 learners using the following prompt:  ",
        "level3_fkg": "Write a story that is readable by Grade 2 learners in the Flesch-Kincaid Grade Level scale using the following prompt: ",
        "level3_cefr": "Write a story that is readable by A2 learners in the CEFR scale using the following prompt: ",
        "level4_fkg": "Write a story that is readable by Grade 2 learners in the Flesch-Kincaid Grade Level scale using the following prompt. The Flesch-Kincaid Grade scale considers the total words, total sentences, and total syllables in a text:  ",
        "level4_cefr": "Write a story that is readable by A2 learners in the CEFR scale using the following prompt. Text assessed as A2 level uses basic sentence patterns with memorised phrases, uses explicit information and limited number of information points:  "
    }

    instruct_simp_dict = {
        "level1": "Simplify the following narrative: ",
        "level2_fkg": "Simplify the following narrative for Grade 2 learners: ",
        "level2_cefr": "Simplify the following narrative for A2 learners:  ",
        "level3_fkg": "Simplify the following narrative for Grade 2 learners in the Flesch Kincaid Grade scale: ",
        "level3_cefr": "Simplify the following narrative for A2 learners in the CEFR scale: ",
        "level4_fkg": "Simplify the following narrative for Grade 2 readers in the Flesch-Kincaid Grade scale. The Flesch-Kincaid Grade scale looks at total words, total sentences, and total syllables in a text:  ",
        "level4_cefr": "Simplify the following narrative for A2 learners in the CEFR Scale. Text assessed as A2 level uses basic sentence patterns with memorised phrases, uses explicit information and limited number of information points:  "
    }

    generations = {}
    sample_prompt_list = ["Once upon a time in a long faraway tower.", "There was once a bad witch."]

    for title,instruction in instruct_story_dict.items():
      print(title)
      generations[title] = generate_llama2(prompt_list, instruction, generator, max_gen_len, temperature, top_p)

    generations_df = pd.DataFrame.from_dict(generations)
    generations_df.to_csv('llama2_story_generations2.csv',index=False)

if __name__ == "__main__":
    fire.Fire(main)
