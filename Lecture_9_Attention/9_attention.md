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
|There is a **bank** in the student union.| bank - teller  $\approx$ church - paster | 
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

# RNNSearch: Seq2seq for NMT with attention II

::: {.columns}
:::: {.column width=0.7}
![A better illustration than original paper's (Src: Kate Loginova's blog post Attention in NLP)](https://miro.medium.com/max/1050/1*9Lcq9ni9aujScFYyyHRhhA.png){width=320px}
::::

:::: {.column width=0.3}

It really works. See Figure 4 and Section 5.2.2 on alignment discussion of the original paper. 

::::
:::


# Bidirectional attention 

::: {.columns}
:::: {.column width=0.5}
![Attention with bidirectional encoder (Src: original paper)](https://analyticsindiamag.com/wp-content/uploads/2021/08/Capture.png){width=320px}
::::

:::: {.column width=0.5}

- $h_n$ contains information up to encoding step $n$. However, in translation, due to different wording orders in different languages, we may need look-ahead information. E.g., see "Sie" before "Sprachen" in order to yield "you" before "speak". 
- A simple solution: encoding the input sentence bidirectionally: $h_n = [\overrightarrow{h_n}, \overleftarrow{h_n}]$ where $\overrightarrow{h_n}$ and $\overleftarrow{h_n}$ are the hidden states (annotations) of encoding of the input sentence and its reverse, respectively, in step $n$. 
::::
:::


# How to compute $a$? 
- $a$ is a function between an encoder state and a decoder state. 
- Bahdanau's additive style
  $$a(s_{m-1}, h_n) = v_a^T \tanh (W_1 s_{m-1} + W_2 h_{n})$$
  So first the hidden states of the encoder and the decoder are projected by two neural networks concurrently and then added together, and finally dot-producted with another vector $v_a$. Three matrixes/vectors need to be learned. 
- Luong's multiplicative/dot-product style  
  $$a(s_{m-1}, h_n) = s_{m-1} W h_{n}$$
  where only one matrix needs to be learned. 
- Other notations: 
![Various ways](https://www.tensorflow.org/text/tutorials/images/attention_equation_4.jpg)

# Multihead attention (MHA)
- The attention mechanism we discused so far is single-headed. There is only one attention given an encoder state and a decoder state. Thus only one context vector $c$ at a decoding step. 
- If we blow up the number of parameters by allowing different context vectors at one decoding step, the model can capture more complex information. 
- This is MHA. Basically, attention memory is distributed. 

# Self-attention
<!-- ::: {.columns}
:::: {.column width=1} -->
Attention between the same sequence, not between input/encoding and output/decoding sequences. 

See Figures 3 to 5 at the end of "Attention is all you need". 


<!-- ![Self_attention (Src: Long Short-Term Memory-Networks for Machine Reading, Jianpeng Cheng, Li Dong, and Mirella Lapata, EMNLP 2016)](https://cdn.analyticsvidhya.com/wp-content/uploads/2019/11/image2.png){width=320px}
::::

:::: {.column width=0}


::::
::: -->

# Attention for Question Answering (QA) / Machine Reading Comprehension (MRC)
![Multi-hop QA, Src: End-To-End Memory Networks, Sainbayar Sukhbaatar, Arthur Szlam, Jason Weston and Rob Fergus, NIPS 2015](./QA.png){width=500px}

- Like NMT, QA is another problem in NLP. 

- Earlier, we mentioned that the attention network $a$ memorizes the interactions between the input and output sequences. 

- Such an memory effect can be used to model the interaction between other types of data, e.g., between a passage containing the answer to a question and the question. 

- Two embedding matrixes for the passage, one for learning attention, and the other for learning output representation.

<!-- - For example, if the passage is "I ate turkey for breakfast" and the question is "What did you eat for breakfast?", then we want "turkey" to have high attention with the question. 
- If you have different question, "In what meal did you have turkey?", then we want a different attention focusing on "breakfast".  -->

# Key-query-value (K-Q-V) formalization of attentions
- The use of attention as memeories in QA inspires researchers to model the attention mechanism as a query system, e.g., the passage as **keys**, storing the information to be looked up by a **query**. The matchness between a key and the query is modeled by attention. 
- Some tasks require two sets of representations for the keys, like the input and output embedding for the passage in the NIPS 2015 paper End-to-End Memory Network. Such representation is called **value**. 
- The seperation between $K$ and $V$ allows separating attention modeling and output geneation. Empirical results show that it is better. 

# The Transformers -- not the metalic alien species

::: {.columns}
:::: {.column width=0.39}
![Src: Attention is all you needed, NIPS 2017](https://www.tensorflow.org/images/tutorials/transformer/transformer.png)
::::

:::: {.column width=0.6}
- Details are clearly listed in Section 3 of the paper, Attention Is All You Need, NIPS 2017.
- Hightlights: 
    - Using self-attention to models correlations between all words of the input sequence in parallel, unlike step-based recurring encoding in RNNs. 
    - Bidirectional attention in encoders vs. rightward attention in decoders enforced by mask-out.
    - Encoders encode input once vs. a decoder generates one output each time, consulting the previously decoded results and encoder outputs.
    - Position encoding for self-attention to see order
    - Multi-head self attention in encoders, in decoders, and between encoders and decoders. 
    - Scaled dot-product/multiplicative attention for each head.
    - Residual connections in encoder and decoder for preserving gradients. 


::::
:::

# Further reading
- [Code for NMT with attention, officla TF tutorial](https://www.tensorflow.org/text/tutorials/nmt_with_attention)
- [Code implementation of Transformer, official TF tutorial](https://www.tensorflow.org/text/tutorials/transformer)
- [A different implementation of Transformer](http://nlp.seas.harvard.edu/2018/04/03/attention.html)
- [Attention in NLP, Kate Loginova's blog post](https://medium.com/@edloginova/attention-in-nlp-734c6fa9d983)
- [Attention in Natural Language Processing](https://arxiv.org/pdf/1902.02181.pdf), Galassi et al., IEEE Trans. on Neural Networks and Learning Systems, vol. 32, No. 10, October, 2021
- If you feel the dimensions in Transformer architecture confuses you, you can read this blog https://towardsdatascience.com/transformers-explained-visually-part-3-multi-head-attention-deep-dive-1c1ff1024853

# Sentence Embedding
- The context vector provides an embedding to the context. If we treat all words in a sentence as a whole, then its context embedding is the embedding to the sentence, i.e., a distributed representation of the semantics of the sentence. 
- Ideally, we want two sentences bearing a semantic relation (e.g., causal, or equivalent) to have some relation in their embeddings (e.g., the cosine similarity of their embeddings is close to 1) 

# BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding
- Hypothesis: attentions between (hidden states of) sentence encodings contain essential nature of the langauge, e.g., "bank" and "money" are strongly related. 
- Hence, attentions learned for one task (e.g., next-word prediction) just needs to be tuned slightly to function on another task (e.g., QA).  
- BERT thus trains attentions on some tasks on large corpora, and then fine-tunes the attentions (and subsequent FC layers) using data for other tasks. 
- A pretrained model can be ported to various application scenaria via fine-tuning. 
- Benefit: saves computational time, e.g., days of training vs. hours of fine-tuning. 

# BERT's architecture
- Multiple layers (e.g., $L=12$) of Transformer's encoder followed by an FC layer and a softmax layer. 
- The input of BERT is a sequence of one or more sentences, seperated by the `[SEP]` token. The first token is a special one `[CLS]` standing for Classification, e.g., 

  `[CLS] Here is a sentence. [SEP] Optionally, here is another one. [SEP]`
- The context vector for the `[CLS]` token is the embedding for the entire input sequence. 
- For each token, the final FC-softmax layer outputs a vector of size $H$ (called hidden size). The number of attention heads for each token is denoted as $A$. 
- There're multiple versions of BERT models, e.g., BERT Base means $L=12, A=12, H=765$. 

# The output for the `[CLS]` token

Many NLP tasks, such as comparing the relation between two sentences, 
has a simple scalar output. For them, BERT is trained to rely on the output of the `[CLS]` token only. 

![Diagram of DistilBERT by HuggingFace, which is very similar to BERT. BERT has both models in the figure. Model 2 for BERT is FC + softmax, outputing a logit.](https://jalammar.github.io/images/distilBERT/bert-model-calssification-output-vector-cls.png){width=300px}

[Demo DistilBert](https://huggingface.co/distilbert-base-uncased)

# The pretraining of BERT
- Two tasks: Masked Language Model (MLM) and Next Sentence Prediction (NSP). 
- MLM: Cloze task with e.g., 15\% words masked. 
- NSP: Binary classification using the output on the `[CLS]` token.

# How to use BERT for sequence labeling output such as QA/MRC

::: {.columns}
:::: {.column width=0.5}
![](google_qa.png)
::::

:::: {.column width=0.5}
- Many tasks can be modeled as predicting a label for each token. 
- In this case, we need to use the outputs of all tokens, not only that for `[CLS]`. 
- We apply the same NN to the output of every token to predict its label. The NN is trained via BP. 
::::
:::

- We can have only one NN for all labels (e.g., multiclass classification for POS tagging), or one NN for each label (e.g., Section 4.2 of the BERT paper using two NNs for start and end in QA/MRC)

- https://mccormickml.com/2020/03/10/question-answering-with-a-fine-tuned-BERT/
- https://d2l.ai/chapter_natural-language-processing-applications/finetuning-bert.html

# More on the input for BERT
- BERT uses WordPiece tokenizer which may break down words to subwords. 
- BERT has a fixed encoder step: 512. Hence, the input is always 512 WordPiece tokens. To make up 512 tokens, append special token `[PAD]`. 
- If longer than 512, and multiple (usually 2) sentences per input sequence, BERT uses round robin trimmer that trims all/both sentences concurrently. In worst case, they will end up in the same length, e.g., 256 for each sentence. 
- Tokens are translated into token IDs, integers. 
- Besides that, an input mask and an input type id vector (aka type encoding, segment embedding) are needed. The input mask (NOT to be confused with the mask in MLM task) has 0's for positions padded and 1's otherwise. The input type id vector has 1's for tokens in the first sentence and 0's otherwise. 

::: {.columns}
:::: {.column width=0.3}
![input mask](https://www.tensorflow.org/text/tutorials/fine_tune_bert_files/output_EezOO9qj91kP_1.png)
::::

:::: {.column width=0.3}
![input type id](https://www.tensorflow.org/text/tutorials/fine_tune_bert_files/output_2CetH_5C9P2m_1.png)
::::
:::

# More on the input for BERT II
The embedding of each token is the sum of its context-independent embedding (e.g., GloVe), its position encoding (discussed in Transformer), and its type/segment encoding. 
![Src: TF tutorial, Google](https://www.tensorflow.org/text/tutorials/fine_tune_bert_files/output_8L__-erBwLIQ_0.png){height=700px}


# Battle of the Transformers
- BERT vs ELMo vs GPT: Fig. 3 in BERT paper. 
- In Japanese https://elyza-inc.hatenablog.com/entry/2021/03/25/160727 
- ![Src: Pre-Trained Models: Past, Present and Future, AI Open, 2021](https://ars.els-cdn.com/content/image/1-s2.0-S2666651021000231-gr8_lrg.jpg){width=400px}

# Discriminative (e.g., BERT) vs Generative (e.g., GPT)
![Src: Pre-Trained Models: Past, Present and Future, AI Open, 2021](https://ars.els-cdn.com/content/image/1-s2.0-S2666651021000231-gr6_lrg.jpg) 

# RoBERTa(**R**obustly **o**ptimized BERT **a**pproach, Facebook AI Research, 2019)
- Same model but different training strategies 
- "We find that BERT was significantly undertrained, and can match or exceed the performance of every model published after it."
- Using one or two sentences (for MLM and NSP respectively) is not good. Filling up the 512 token limit is better. 
- With long input sequences (not necessarily long sentences), NSP can be opt out. 
- Large batches, long training steps. 

# Other pretrained models
- [RoBERTa, Facebook, 2019](https://arxiv.org/pdf/1907.11692.pdf)
- [BART, Facebook, 2019](https://arxiv.org/pdf/1910.13461.pdf)
- [XLNet, Google, 2020](https://arxiv.org/pdf/1906.08237.pdf)
- [T5, Google, 2020](https://ai.googleblog.com/2020/02/exploring-transfer-learning-with-t5.html)
- [A good review by Tsinghua NLP group](https://www.sciencedirect.com/science/article/pii/S2666651021000231)

# Further reading on the Attention of BERT
- [Revealing the Dark Secrets of BERT, Olga Kovaleva, Alexey Romanov, Anna Rogers, Anna Rumshisky, EMNLP 2019](https://aclanthology.org/D19-1445.pdf)
- [What does BERT look at? An Analysis of BERT’s Attention, Kevin Clark, Urvashi Khandelwal, Omer Levy, Christopher D. Manning, BlackBoxNLP 2019](https://aclanthology.org/W19-4828.pdf)
- [Analyzing Multi-Head Self-Attention: Specialized Heads Do the Heavy Lifting, the Rest Can Be Pruned, Elena Voita, David Talbot, Fedor Moiseev, Rico Sennrich, Ivan Titov, ACL 2019](https://aclanthology.org/P19-1580.pdf)

# Some good tutorials on BERT and others
- https://jalammar.github.io/a-visual-guide-to-using-bert-for-the-first-time/
- https://www.tensorflow.org/text/tutorials/fine_tune_bert
- https://www.tensorflow.org/text/guide/bert_preprocessing_guide
