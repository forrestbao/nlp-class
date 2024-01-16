---
title: | 
         CS 673 Natural Language processing \
         10. Few-shot, zero-shot, and prompting
author: |
          Prof. Dr. Forrest Sheng Bao \
          Dept. of Computer Science \
          Iowa State University \
          Ames, IA, USA \
date:   \today
header-includes: |
    \usepackage{amssymb,mathtools,blkarray,bm}
        \usefonttheme[onlymath]{serif}
    \usepackage[vlined,algoruled,titlenotnumbered,linesnumbered]{algorithm2e}
    \usepackage{algorithmic}
    \setbeamercolor{math text}{fg=green!50!black}
    \setbeamercolor{normal text in math text}{parent=math text}
    \newcommand*{\vertbar}{\rule[-1ex]{0.5pt}{2ex}}
    \newcommand*{\horzbar}{\rule[.5ex]{2ex}{0.5pt}}
    \setlength\labelsep   {.5pt}  
    \setbeamersize{text margin left=3mm,text margin right=4mm} 
    \setlength{\leftmargini}{15pt}
    \usepackage{hyperref}
    \hypersetup{
    colorlinks=true,
    linkcolor=blue,
    filecolor=magenta,      
    urlcolor=cyan,
    }
    \setlength{\abovedisplayskip}{1pt}
    \setlength{\belowdisplayskip}{1pt}
    \usepackage{graphicx}
classoption:
- aspectratio=169
---

# The taxonomy of language models (LMs) 

* Language models (LMs) 
  - conventional, statistics based: n-gram, topic modeling 
  - neural language models (NLMs): based on neural networks 
    - Masked LMs (MLMs): e.g., `I felt so <MASK>`. Do HuggingFace `bert-base-cased` fill-mask demo. 
    - Pre-trained LMs (PLMs): such as BERT. "Pre-trained" means that you do not have to train from scratch but just finetune (training with much less amount of training data than from scratch) to adapt it for your own application. 
    - Large LMs (LLMs): some PLMs are so big that they can not only **characterize the semantics of documents** but even **generate new text** (if their architectures are also generative). Such as GPT. 
* A rule of thumb: generative LMs are generally larger than discriminative ones.

# How large is large? 
* Let's compare models and their # of number parameters (weights in the neural networks)
* BERT-base (2018, 12 Transformer blocks, 12 attention heads, and 756-D vector): 110M
* GPT-1 (2018): 117M 
* BART (2019): 140M 
* GPT-2 (2020): 1.5B 
* T5 (2020): Up to 11B (T5-11B)
* GPT-3 (2021): 175B 

# Few-shot vs. one-shot vs. zero-shot
* One special case of fine-tuning is called few-shot
* Few-shot: fine-tuning using substiantially small amount (usually under a few thousand) of samples
* An example: FewshotQA by Amazon Science. [Link](https://www.amazon.science/publications/fewshotqa-a-framework-for-few-shot-learning-of-question-answering-tasks-using-pre-trained-text-to-text-models)
* Let's see a demo on few-shot sentiment analysis. 
* One-shot: only one or a handful of training/fine-tuning samples. 
* Zero-shot: No training/fine-tuning at all! ML without learning! 
* Figure 2.1, GPT-3 paper Language Models are Few-Shot Learners

# Prompting and zero-shot
![](https://github.com/ucinlp/autoprompt/raw/master/app/assets/bert-mouth.png)

* Adding some words into a text and then feeding the augmented text into a PLM could repurpose the PLM for a specific task, e.g., as a movie rater above. 
* Originally found in GPT-2: Simply adding `TL;DR` after an article to trigger [GPT-2](https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf) to generate the summary. 
* This technique is called **prompting**. 
* It allows repurposing the same PLMs for different tasks without training/fine-tuning. Thus, zero-shot! 

# What prompting really does
* Prompting converts any task into a masked LM task. 
* A prompt text is usually added to the original input text via a **template**. 
* For example, `[X] This article is about [MASK]` can be template where `[X]` is the input text and `[MASK]` is the masked part to be generated. In this example, this template can be used to categorize news articles and  `[MASK]` can be "sport", "science", "finance", etc. 
* As another example, `[X1]. [MASK], [X2].` can be used to estimate the causality between two texts `[X1]` and `[X2]` where `[MASK]` to be generated, can be "consequently", "therefore", "however", "constrastly". 
* The generated text at `[MASK]` by a PLM is called the **answer**. 
* Answer mapping: mapping the generated text at the masked location to what you want. 
* More examples of using prompting for various tasks: Tables 3 and 10 of [Pre-train, Prompt, and Predict: A Systematic Survey of
Prompting Methods in Natural Language Processing](https://arxiv.org/pdf/2107.13586.pdf). 

# Prompt Engineering
* So how to design the template becomes a problem for using prompting effectively. 
* This becomes an area in NLP known as prompt engineering. 

# Prompt mining: a simple approach to prompt engineering 
* Prompting can work because the PLMs have captured certain language patterns from training data. 
* So the prompt template should match such language patterns, synatactically. 
* For example, suppose we have many training data like "Paris is the capital of France" or "Tokyo is the capital of Japan". Then to let a PLM answer the capital of a nation, the template should be `[MASK] is the capital of [X]` where `[X]` is a nation.
* How do we find such patterns from data? It depends on your task. You can search for pairs of `[X]` and `[MASK]` in your task data in a corpus and extract words between them and let your template be `[X] WORDS BETWEEN THEM [MASK]`. 


# AutoPrompt: an automated approach to prompt engineering
* The prompt template does not even have to be a meaningful sentence! 
* ![](https://thegradient.pub/content/images/2021/07/Screenshot-from-2021-07-01-22-26-56.png)

# Answer mapping
* Still remember the definition of an answer? It's the text generated from the mask `[MASK]` by a PLM. 
* However, an answer may not be what we really want. For example, `I saw Titanic yesterday. The movie is [MASK]. ` but `[MASK]` can be generated into many answers by a PLM, e.g., "good", "great", "thrilling". How do we map the answers to a movie rating? 
* The naive approach would be to manually map each answer to the final answer we want. 
* One solution is answer paraphrasing. 

# More complex use of prompting 
* Multi-prompting 
* Prompt-based fine-tuning: The goal of prompting is to specialize a LM without fine-tuning. But research shows that fine-tuning can be more efficient with prompting. Example: https://thegradient.pub/prompting/
* Few-/one-shot prompting: Prompt contains examples. The examples condition or influence the generation. 

  ![](https://huggingface.co/blog/assets/22_few_shot_learning_gpt_neo_and_inference_api/few-shot-prompt.png)


# Chain-of-thought prompting
* I'd consider this is as a special case of few-/one-shot prompting.

  ![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgVgTjwA0IzKekrQoMziCmDXjO10QKjdDdzK1Oj8bZToPOI6VjVzTKXZ6vnWvAGOdVnWznJK2ZZjfBuTLojobayI_yrvlFzE3dCErF2j5wKLGFWAkuGP9-r-hMrqFivnjYhbCIu7HFINSmHu4wUjlKHfJxWHZ8Y7CYUowWvxTeRJhQEAUswGh2fUd3VHA/s16000/chainofthought.png)

* The language model was shown how to solve one problem. And it is expected that it can generate the chain of thought and the final answer for another problem. 
* This is not the end!
* What if we teach the LM to learn different chains of thought? 
* Figure 1 of [Self-Consistency Improves Chain of Thought Reasoning in Language Models](https://arxiv.org/pdf/2203.11171v1.pdf)


# LLMs are knowledge bases
* Human knowledge are reflected in texts, e.g., "Des Moines is the capital of Iowa."
* LLMs are actually knowledge bases. 
* Prompting is actually one way to for knowlege reasoning. Figure 1 of [Language Models as Knowledge Bases?](https://aclanthology.org/D19-1250.pdf) 

# Surface form competition: language models are not always right 
* A common problem in LLMs for commonsense question answering is surface form competition. 
* Figure 1 in [PMI_DC paper](https://arxiv.org/pdf/2104.08315.pdf)
* Figure 2 of [SEQA paper](https://aclanthology.org/2021.acl-long.237.pdf). 


# Text generation methods 
* Prompting relies on the generating power of LMs. 
* GPT-3 demo  https://transformer.huggingface.co/doc/gpt2-large
* It's more than seq2seq. 
* Auto-regression 
* [Greedy vs. beam search](https://huggingface.co/blog/how-to-generate) 
* top-k, top-p
* constrastive search 
