---
title: | 
         CS 673 Natural Language processing \
         10. Topic Modeling
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

# Topic modeling 
![Blei 2012, Probabilistic topic models, CACM](https://i.ibb.co/zV5rjX6/Screen-Shot-2020-09-24-at-11-21-38.png)


# Topic Modeling in Latent Dirichlet Allocation (LDA) 

![Lee et al. (2018). Ensemble Modeling for Sustainable Technology Transfer. Sustainability.](https://www.researchgate.net/publication/326140642/figure/fig1/AS:644129876873217@1530583938944/Graphical-model-of-latent-Dirichlet-allocation-LDA.png){width=400px}

- Two basic probabilistic distributions.
- First: a topic is a distribution over words, e.g., the chance of the word ``gas'' is high in the topics about cars but low in the topics about computers. This distribution is controled by the varaible $\beta$. 
- Second: a document is a distribution over topics, e.g., my blog is a mixture of NLP, cars, and wood work while the blog of someone else differs.  This distribuition  is controlled by the variable $\alpha$. 



# LDA-based generative process 

![Lee et al. (2018). Ensemble Modeling for Sustainable Technology Transfer. Sustainability.](https://www.researchgate.net/publication/326140642/figure/fig1/AS:644129876873217@1530583938944/Graphical-model-of-latent-Dirichlet-allocation-LDA.png){width=300px}


- In LDA, a document is assumed to be generated as follows. 
- First, pick a topic distribution for a document ($P(\theta|\alpha)$). The topics are switched when generating a document, e.g., ``Today I tried out PyTorch... Then I drove 100 miles to meet a friend. ... I showed my recent workbench photo to him. ''
- Then, the document is generated word by word. 
  * For each word position, a topic is assigned ($P(z| \theta)$). 
  * Based on the assigned topic (which is a distribution over words), a word is drawn $P(w| z, \beta)$. 

# LDA parameter estimation via Gibbs sampling 
* Variables to begin with: 
  - $K$: number of topics, assigned by you. 
  - the set $V$: the vocabulary, whose size is denoted as $|V|$
  - the set $D$: all documents, each of which is a sequence of words. 
* Three matrixes are maintained: 
  - $TA$: topic assignment, $|D| \times |V|$. Each row is a document, and each column is a word. Thus, an element is the topic ($\in [1..K]$) that a word in a document is assigned to. **Initially randomly assigned**. 
  - $WT$: word-topic matrix, $K \times |V|$, the count of each word being assigned to each topic. 
  - $DT$: document-topic matrix, which is the number of words assigned to each topic for each document (distribution of the topic assignment list)
* The last two $WT$ and $DT$ is what we need to estimated. They are initialized from $TA$. 

# Let's see the demo to know more details 
https://deepnote.com/workspace/forrest-bao-8d3a-8e96c0f9-789e-4b51-b08f-8c67f93fd301/project/NLPclass-5185c4e4-930a-4349-b76b-be1834007069/notebook/Notebook%201-d3cd48df628e43349658499d66eb8093

# What can LDA be used for
- Given a document, we can compute its topic distribution. 
- The topic distribution is a vector representation of the document -- document embedding! 
- Then for example, we can group documents based on their topic distribution, in applications like news aggregation. 
