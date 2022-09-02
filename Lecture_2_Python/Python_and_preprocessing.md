---
title: | 
         CS 579X Natural Language processing \
         Lecture 2: Python and Preprocessing
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


# Python
* The language of NLP and DL
* NLP and DL: SpaCy, Stanza, PyTorch, Tensorflow
* Web APIs made easy: Flask, FastAPI, `functions_framework` ([click to see demo](https://hello-world-ovrqou53aq-uc.a.run.app/?name=CS579X))
* Web apps made easy: Gradio, Streamlit 
* The Zen of Python
* A good PL or framework should be ``quick to get, consistent to scale'' (my own words)

# Why is Python successful? 
* Lots of small but handy features (including many syntax sugars) put together ([Lecture 7, How to Start a startup, Y Combinator on YouTube](https://www.youtube.com/watch?v=sz_LgBAGYyo))
* the first to do it in its time 
* element-wise iteration or iterators, dynamic typing, arguments and returns of a function as tuples, `enumerate`, `zip`, nested functions, `pickle`, negative index (`a[-1]`), `with`


# Easy compounding of data structures
* It's not only `int`, `float`, and `str`
* `list`, `tuple`, and `dict`
* Nested and/or compound lists, tuples, and dictionaries
* Built-in JSON support, the `json` module
* ```python
  [
    {"document":"blah blah blah",
     "summaries":[
        "system_1":{"summary":"du du du ", 
                         "scores": {
                            "human_rater_1": 
                                {"aspect_1":0.7, "aspect_2":0.4}, 
                            "human_rater_2": 
                                {"aspect_1":0.5, "aspect_2":0.2}
                            }
                        },
        "system_2":{"summary":"dah dah dah ", 
                         "scores": {
                            "human_rater_1": 
                                {"aspect_1":0.6, "aspect_2":0.9}, 
                            "human_rater_2": 
                                {"aspect_1":0.2, "aspect_2":0.3}
                            }
                        }
     ]}, 
     {"document":"blu blu blu",
     "summaries":[
        ...
  ]
  ```
