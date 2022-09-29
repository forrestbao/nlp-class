---
author:
- 'Forrest Sheng Bao, Ph.D.'
date: '2022-9-29'
subtitle: Lecture VI. Machine Learning Basics for NLP
title: Natural Language Processing
---

# Agenda

- Why ML in NLP 
- Math warmup: vectors, matrixes, gradient descent. [Click for ML slides 2](https://github.com/forrestbao/MLClass/blob/master/2_Linear_Classifiers/2_linear_classifiers.md)
- Feature engineering in NLP 
- ML intro 
- Neural networks (main topic)

# Why ML in NLP 
- Two branches of NLP: rule-based and model-based. 
- We have already seen several examples for the 2nd approach: POS tagging (using HMM), NER (using CRF), Naive Bayes spam filter, and TF-IDF document retriever. 
- In all those examples, we scan a corpus to obtain the parameters for the model. We do not teach the computer how to fulfill a task specifically. 
- Rule-based becomes very difficult when it comes to generative tasks: QA, translation, summarization, etc. 

# Why ML in NLP is hard
- All modeling approaches above have limited capacities or are based on strong assumptions. 
- Discrete representation: "cat" vs. "hat",  "cap" vs. "hat". 
- Context: Natural languages are strong context-dependent. Too strong to assume n-grams are independent or Markovian. 
- Long-term dependency: what if two related pieces are very far from each other? Like "Pizza, a favorite food for parties, is not healthy"
<!-- - We also made strong assumptions: words/tokens are independent. In reality they are not: natural languages are context-dependent, e.g., "cold pizza" vs. "cold beer".  -->
- Natural languages are highly flexible. We need a model of lots of parameters to comprehend languages. 



# Machine Learning is all about finding a function
- [Let's move to the ML class](https://github.com/forrestbao/MLClass/blob/master/1_Introduction/1_intro.md)
- Then let's see this [Mathematica notebook](./ML.pdf)

# Feature engineering in ML
- BOW is a simple way of building a feature vector
- CRF example in NER
- Making use of linguistic dictionaries, e.g.,  [Semantic Analysis and Helpfulness Prediction of Text for Online Product Reviews, ACL 2015](https://aclanthology.org/P15-2007/)


# Math warm-ups 
- vectors, matrixes, gradient descent. [Let's move to Lecture 2 of ML class](https://github.com/forrestbao/MLClass/blob/master/2_Linear_Classifiers/2_linear_classifiers.md)

# Notions in ML
- $\mathbf{x} = [x_1, x_2, \dots, x_n] \in \mathbb{R}^n$ is a feature vector. It can be a token, a sentence, a document, depending on the problem you are solving. 
- $\mathbf{w} = [w_1, w_2, \dots, w_n] \in \mathbb{R}^n$ is a weight, usually dot-producted with a feature vector to linearly transform the feature vector: $\mathbf{w}^T\mathbf{x}$.

# Neural networks (NNs)
- Neural networks transformed NLP twice in the past ten years. 
- word2vec: semantic, vector representation of tokens that works
- Attention/Transformers: contextual, semantic representation of tokens, sentences, and docs. 


# New blow-aways this week, thanks to NNs 
- [Ask Command by Tony Dinh](https://askcommand.com/)
- [Make-a-video by Meta FAIR](https://makeavideo.studio/)


# You need to believe in NNs 
"A new scientific truth does not triumph by convincing its opponents and making them see the light, but rather because its opponents eventually die and a new generation grows up that is familiar with it" --  Max Planck, Scientific autobiography, 1950, p. 33, 97

[Demo]()