---
title: | 
         Title of the paper \
         venue, year 
author: |
          Originally by A, B, C \
          Presented by X, Y, Z \
          for NLP class at Iowa State University
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


# Background (1-2 slides, 2-3 minutes)
- Provide information for an average CS graduate student to know the problem solved by the paper
- Use the language that a documentary would use to explain a scientific concept to general audiences. 
- Example: Motivation section of https://github.com/tensorflow/docs/blob/r1.15/site/en/tutorials/representation/word2vec.md 

# State of the art before the authors' work (1-2 slides, 2-3 minutes)
- A paper usually goes over related work. If the paper you are assigned to does not, then you can skip this part. 
- How other researchers approached the problem before the authors.
- Explain their main ideas in simple English and short equations. 
- Pros and cons of their approaches. 

# The authors' ideas (1-4 slides, 3-7 minutes)
- List the authors' new ideas in bullet points in a language that an average CS graduate student can understand
- If needed, use short equations and illurations (like Figure 1 of Mokolov et al.'s word2vec paper) to give people a high level idea. 
- Math can be your friend because it can be concise and clear than English in many cases, e.g., $E=mc^2$.
- Use examples if they help explain the authors' idea. 
- Example: "Scaling up with Noise-Contrastive Training" section abd "The Skipgram model" section of https://github.com/tensorflow/docs/blob/r1.15/site/en/tutorials/representation/word2vec.md 

# Results showing that the authors' approach works (1-4 slides, 1-3 slides, 3-5 minutes)
- No need to list all results reported in the paper. 
- List those most important or surprising. 
- Include qualitative results, which do not take your audiences much time to digest, like Figure 3 in NEURAL MACHINE TRANSLATION BY JOINTLY LEARNING TO ALIGN AND TRANSLATE at ICLR 2015. 

![Another example](https://camo.githubusercontent.com/18e6fed54d75686195643b2b96b0e57912bbc5c8a0a0571256d39a04cefcf1c1/68747470733a2f2f7777772e74656e736f72666c6f772e6f72672f696d616765732f6c696e6561722d72656c6174696f6e73686970732e706e67){width=400px}

# Possible extensions of the work (optional)
- Future work listed by the authors at the end of the paper
- Future work according to papers citing the work
- Future work according to you 

# Limit your presentation under 15 minutes 
- We have 35 teams in total.
- Each team has 15 minutes to present and 5 minutes for Q&A. 
- Remember: let your presentation be a trailer of the paper. 
- The slides can be generated via Pandoc in the command 
  ```shell
  pandoc -t beamer presentation_template.md -o presentation_template.pdf
  ```