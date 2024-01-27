---
title: | 
         CS 579X Natural Language processing \
         Lecture 12: NLG and NLG evaluation metrics
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


# Natural Language Generation (NLG)
* Classical NLG: template/rule-based
* Modern NLG: neural-based
* Classical NLG tasks: summarization and translation (or, machine translation or MT)

# Neural-based NLG
* Sequence-to-sequence (seq2seq) models (e.g., `transformers.AutoModelForSeq2SeqLM`)
* Concepts in NLG: 
    * begin or end of sequence (BOS or EOS) tokens 

# Non-greedy decoding
* Beam search
* Nucleus sampling (top-$p$ sampling)
* Contrastive search
* Temperature 
* How to avoid repetition 

# References for NLG 
* [A Colab notebook for NLG](https://colab.research.google.com/github/huggingface/blog/blob/main/notebooks/02_how_to_generate.ipynb#scrollTo=XbbIyK84wHq6)
* [Generation strategies by HuggingFace Transformers](https://huggingface.co/docs/transformers/v4.37.1/en/generation_strategies) 
* [Utilities for Generation by HuggingFace Transformers](https://huggingface.co/docs/transformers/internal/generation_utils)
* [`transformers.GenerationMixin`](https://huggingface.co/docs/transformers/v4.37.1/en/main_classes/text_generation#transformers.GenerationMixin)


# Machine translation (MT)
* NLLB
* T5 
* Pegasus 

# Summarization 
* Abstractive vs. extractive
* LexRank 


# NLG evaluation metrics
* Reference-based vs. reference-free
* Classical ones: ROUGE, BLEU, etc.
* Transformers-based: BERTScore, BLEURT, etc.
* Summarization metrics using special tasks: BLANC, SUPERT, SummaQA, etc.

# NLG evaluation using LLMs themselves 
* G-Eval
* 
