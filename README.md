# NLP class @ Iowa State University

This respository is for the NLP class offered at Iowa State University from Fall 2017 to Fall 2021. 

**Instructor**: Prof. Dr. Forrest Sheng Bao [forrestbao.github.io](forrestbao.github.io)

Slides can be found in the folders for each lecture unit. Default file name is `EE.pdf`.

Slides for Machine Learning can be found in [Bao's ML class repository](https://github.com/forrestbao/MLClass). Note that the information about perceptron algorithm is under the SVM unit. 

For reading assignments, check [reading.md](reading.md)

## How to edit and compile the slides

The slides were written in a mixture of LaTeX and Markdown. Some Markdown slides contain `mermaid` plots. 

### LaTeX (`*.tex`) slides

If you are on Ubuntu Linux, install the following packages: 

```
sudo apt install texlive-latex-recommended  texlive-latex-extra   texlive-science
```

Then, 
```
pdflatex xxxx.tex
```

### Markdown (`*.md`) slides

You will need to install `pandoc`  and [`mermaid-filter`](https://github.com/raghur/mermaid-filter) (which requires `npm` to install) first. Then run the command like below in a slide folder (example below for Lecture 1): 

```
pandoc Brief_neural_based_NLP.md -t beamer --filter mermaid-filter -V fontsize=12pt  -o Brief_neural_based_NLP.pdf
```


## IPython notebooks 
* [Python introduction](Lecture_2_Python/Python_demo.ipynb)
* [Tensorflow introduction ](Tensorflow1_hello_world.ipynb)
* [Regular expressions](Lecture_3_preoprocessing/Lecture_3_preprocessing_regular_expression.ipynb)
* [Web crawling and indexing](Lecture_3_preoprocessing/Lecture_3_HTML_parsing.ipynb)
* [LSTMsin Tensorflow](https://colab.research.google.com/drive/1wl-5uofsShYJic0KQ5zapku_l8dHeJR2?usp=sharing)
* [Embedding layers in Tensorflow](https://colab.research.google.com/drive/15repLULKxghG5FYIeBbxoL-47JyGoRXI)




Opinions expressed in this repository do not reflect those of Iowa State University. 
