---
title: | 
         CS 673 Natural Language processing \
         9. Attention
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

# 

Images that were not created by the instructor but from the web 
are cited in the Markdown source code in the syntax: 
```
![a web image](URL)
```

# Contextual embedding
- So far we have seen **static embedding** of words: the embedding is invariant to the context. 
- But natural languages are ambigious. 
- A classical error in maching translation: "The spirit is willing, but the flesh is weak." translated to Russian and back becomes "The vodka is good, but the meat is rotten." because "spirit" and "flesh" are ambigious. 
- To precisely determine the meaning of a word, context is needed. Hence, the embedding is better if context-dependent. 
- The type of embedding variant to the context is called **contextual embedding**. 
- Another example 
|Different banks| vector analogy | 
|:----:| :---: | 
|I charge my phone with a mobile power **bank**. | bank - electrity $\approx$ reservoir - water  | 
|There is a **bank** in the student union.| bank - money  $\approx$ parking lot - cars| 
|The view is nice along the **bank**, lots of boats and nice resturants.| bank - river $\approx$ platform - railroad | 




<!-- - Intuition: the meaning of a word is determined not only by itself but also the context.  -->

# Contextual embedding via the attention mechanism

- Denote the embedding of the word whose contextual embedding is to be modeled as $x_c$. 
- Let the embeddings of its context words form a set $\mathcal{X}$. The context could be forward, backward, or both. 
- Then the embedding of the center word $x_c$ of the said context can be, e.g., a weight sum of the static embeddings of context: $\sum_{x\in \mathcal{X}} f(x, x_c) x$ where $x$ is the static embedding of a context word and $f$ is a function modeling the interactions between a context word and the center word. 
- Usually we want $f(x, x_c)$ to be context-dependent as well, e.g., via softmax: $\alpha(x, x_c) = {\exp( f(x, x_c) ) \over \exp\left (\sum_{x'\in \mathcal{X}} f(x', x_c) \right ) }$ and then the contextual embedding of the center word $w_c$ is rewritten as $\sum_{x\in \mathcal{X}} \alpha(x, x_c) x$
- The return of the function $\alpha$, which is a scalar, is called an **attention** which measures how strongly a context word $x$ influences the semantics of the center word $w_c$ in the context. The softmax normalization tunes the influence depending on the context as well. 
- People usually call the return of the function $f$ as **energy**. 
- $f$ can be implemented via a neural network. But what tasks? 

# Attention mechanism in machine translation
- Attention mechanism entered NLP first in machine translation (MT), or neural machine translation (NMT). 
- A milestone work: Neural Machine Translation by jointly learning to align and translate, Dzmitry Bahdanau, Kyunghyun Cho, and Yoshua Benio, ICLR 2015, called *RNNSearch**. 
- Attention mechanism got people's attention via Google's paper: Attention is all you need in NIPS 2017 where they revealed the Transformer architecture.  
- But before we talk about NMT, we need to talk about encoder-decoder architecture first. 

# Encoder-decoder architecture
- Encoder-decoder architecture is widely used in NN research, not only for NMT. 
- Encoder: An NN, converting input information to a vector/latent representation. 
- Decoder: The other NN, generating the output from the vector representation. 
- The input and output information can be in the same domain or different. 
- E.g., a grayscale image $\xRightarrow{\text{encode}}$ latent representation $\xRightarrow{\text{decode}}$ a color image, image colorization
- E.g., a blurry image $\xRightarrow{\text{encode}}$ latent representation $\xRightarrow{\text{decode}}$ a clear image, image deblurring
- E.g., a sentence $\xRightarrow{\text{encode}}$ latent representation $\xRightarrow{\text{decode}}$ a vocal signal, speech synthesis
- E.g., a vocal signal  $\xRightarrow{\text{encode}}$ latent representation $\xRightarrow{\text{decode}}$ a sentence, speech recognition 
- The latent representation usually has a lower size than the input data, only the ``condensed'', key information. 
- An **autoencoder** restores the input information at the output end. It is mostly used for data compression or representation learning. 

# Seq2seq: sequence-to-sequence
::: {.columns}
:::: {.column width=0.5}
![Unrolled Seq2Seq with attention for NMT (Src: TF tutorial, Google)](https://www.tensorflow.org/images/seq2seq/attention_mechanism.jpg){ width=250px }
::::

:::: {.column width=0.5}
- Introduced by Ilya Sutskever, Oriol Vinyals, Quoc V. Le of Google at NIPS 2014. Frequently used in NMT. 
- A seq2seq model is a special kind of encoder-decoders, where both the input and output are sequences (not necessarily time series), e.g., sentences consists of words. 
- It takes inputs in steps and generates outputs in steps, rather than at once for either encoding or decoding stage. 
- Hence, it's frequently implemented in RNNs (vanilla, LSTM, GRU, etc.)
- Input and output could have different lengths, e.g., "Do you speak German?" (4 tokens) to "Sprachen Sie Deutsch?" (3 words) 
::::
:::


# Seq2seq for NMT without attention
::: {.columns}
:::: {.column width=0.4}
![Unrolled Seq2Seq with attention for NMT. Ignore the attention part. (Src: TF tutorial, Google)](https://www.tensorflow.org/images/seq2seq/attention_mechanism.jpg)
::::

:::: {.column width=0.6}
- Encoding stage: Given a sentence $[x_1, x_2, \dots, x_N]$ of $N$ tokens, train an RNN: 
  $h_n = f(x_n, h_{n-1})$.
- $h_N$, the encoder's output in the last step, contains all information of the sentence in the source language. 
- A special token is used to trigger the starting of the decoding stage. 
- Decoder is also an RNN: $s_m = f'(y_{m-1}, s_{m-1}, h_M)$, where $f'$ (correspond to $f$ for encoder) is the neural network that advances the decoder to state $s_m$ using the output $y_{m-1}$ and state $s_{m-1}$ at the previous step and $h_N$. 
- A third function $g$ maps the decoder's state (and optionally other information) to an output token at the current step: e.g., $y_m = g(s_m)$, or $y_m= g(s_m, y_{m-1}, h_T)$. Usually, it's a 1D vector containing the probabilities of all words in the vocabulary being the next word. 
::::
:::

# RNNSearch:  Seq2seq for NMT with attention
- Attention is needed: contextual meaning of words. 
- The need differs in steps: the weights of contexts should differ depending on the output words, e.g., after "Sprachen", the focus should be on "you" not "German". 
- Thus one constant representation $h_M$ for the entire input sentence is not good. We want to gauge the interactions between every input token and every state of the decoder. 
- First, change  $s_m = f'(y_{m-1}, s_{m-1}, h_M)$ to $s_m = f'(y_{m-1}, s_{m-1}, c_m)$ where the representation of the input ($c_m$) depends on the decoding step $m$ instead of fixed on $h_M$. We call $c_m$ the **context vector** at decoding step $m$. 
- $c_m$ is the attention weighted sum of all hidden states (a.k.a. **annotations**) of the encoder: $c_m = \sum_{n=1}^N \alpha_{m,n} h_n$.  
- The attention $\alpha_{m,n}$ between a decoding step (an output token) $m$ and an encoding step (an input token) $n$ is 
  $\alpha_{m,n} = {\exp(e_{m,n}) \over \exp \left (\sum_{n=1}^N e_{m,n} \right )}$ where $e_{m,n}=a(s_{m-1}, h_n)$ where the notations $e$ and $a$  stand for "energy" and "alignment", respectively. 
- Function $a$ is a network "memorizing" the context dependency of tens of thousands of words. 

# Seq2seq for NMT with attention II

![A better illustration than original paper's (Src: Kate Loginova's blog post Attention in NLP)](https://miro.medium.com/max/1050/1*9Lcq9ni9aujScFYyyHRhhA.png){width=300px}


# Bidirectional attention 
- $h_n$ contains information up to encoding step $n$. However, in translation, due to different wording orders in different languages, we may need look-ahead information. E.g., see "Sie" before "Sprachen" in order to yield "you" before "speak". 
- A simple solution: encoding the input sentence bidirectionally: $h_n = [\overrightarrow{h_n}, \overleftarrow{h_n}]$ where $\overrightarrow{h_n}$ and $\overleftarrow{h_n}$ are the hidden states (annotations) of encoding of the input sentence and its reverse, respectively, in step $n$. 
- Better pictures 

# The Transformers -- not the metalic align species


::: {.columns}
:::: {.column width=0.5}
::::

:::: {.column width=0.5}

::::
:::
