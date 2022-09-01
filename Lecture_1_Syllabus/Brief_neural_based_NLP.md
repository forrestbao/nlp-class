---
title: | 
         CS 579X Natural Language processing \
         Lecture 1B: A brief intro to neural-based NLP
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

# You need to believe in neural networks 

* In the Deep Learning era, NLP is somehow easy. 
* Church-Turing thesis, computability 
* Neural networks: universal approximation
* Let's see a demo `demo.ipynb` 

# Ask what you want, neural networks can give you
* [Semantic search demo by the instructor](https://github.com/forrestbao/pebble/blob/master/NLP/semantic_search.ipynb)
* [Masked LM](https://huggingface.co/distilbert-base-uncased?text=I+failed+the+%5BMASK%5D+exam+because+calculus+is+too+hard.)
* [DALL-E](https://openai.com/dall-e-2/#demos)
* [GPT](https://transformer.huggingface.co/doc/gpt2-large)
* [coPilot](https://github.com/features/copilot)
* [OpenAI grade school math ](https://github.com/openai/grade-school-math)

# What it takes 

:::::::::::::: {.columns}
::: {.column width="40%"}
* Token-level embedding: string to vectors 
* (Self-)Attention (attention weights, $aij$'s in the figure, are floating-point numbers)
* Some complex flow of information (residual, recurrent, normalization, etc.)
* Finally, mapping the neural network output back to string
* Proper training data 
:::
::: {.column width="60%"}


```{.mermaid width=400 format=pdf}
graph TD; 

W1["I"]-->|embedding|E1["[0.05, 0.17, 0.39, ...]"];
W2["am"]-->|embedding|E2["0.19,0.72, 0.64, ..."]; 
W3["happy"]-->|embedding|E3["0.46, 0.89, 0.37, ..."]; 

E1-->|a11|F1;
E2-->|a21|F1;
E3-->|a31|F1;
E1-->|a12|F2;
E2-->|a22|F2;
E3-->|a32|F2;
E1-->|a13|F3;
E2-->|a23|F3;
E3-->|a33|F3;

```
:::
::::::::::::::


# Training data is all you needed
* Without training data, [how to solve math](http://geometry.allenai.org/demo/)
* SueNes, sentence deletion vs word deletion 