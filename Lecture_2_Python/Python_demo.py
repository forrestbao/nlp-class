
# coding: utf-8

# In[2]:

import antigravity
"""
Is Python difficult to learn? 
* UNIX is user-friendly. It's just picky who its friends are. 
* Contrary to popular belief, Unix is user friendly. It just happens to be very selective about who it decides to make friends with.   -- unknown 
* It’s is easy to use - if you’re one of the 2 percent of the population who thinks logically and can read an instruction manual. The other 98 percent of the population would ﬁnd it very hard to use. -- 
"""


# In[3]:

def foo(x):
    """ a function to compute the square of integer x
    
    Parameters 
    ----------
    
        x: integer
            the number to be squared
    
    Returns 
    -----------
    
        y: integer
            the square of x 
    
    """
    y = x * x 
    return y 


# In[9]:

"""How to write good progarms.
* Linux has succeeded not because the original goal was to make it widely portable and widely available, but because it was based on good design principles and a good development model. -- Linus Torvalds, "The Linux edge", Open Sources: Voices from the Open Source Revolution, O'Reilly, 1999 
* Modularize 
* Test each module before 

Why do we define functions? 
* For reusing a snippet of code -- save me from re-typing
* For others to pay to use your function -- so I can be rich and be a happy professor
* For making debugging easier -- aim small, miss small 
"""

def f(a, b, c):
    '''
    
    Examples
    ------------
        
    >>> f(1,2,3)
    42
    '''
    return (a+b)/c


# In[10]:

# Doctest is one way to test from examples in docstrings
import doctest 
doctest.run_docstring_examples(f, globals())



#if __name__ == '__main__':
#    import doctest
#    doctest.testmod()


# In[7]:

"""Good documentation means good code 

Good examples: 

* https://github.com/nipy/mindboggle/blob/master/mindboggle/shapes/laplace_beltrami.py 
* https://github.com/numpy/numpy/blob/master/numpy/linalg/linalg.py
* https://github.com/forrestbao/pyeeg/blob/master/pyeeg/__init__.py

Bad examples:
* https://github.com/forrestbao/glacier-upload/blob/master/main.py

Use Sphinx to produce documents from your code. 

"""


# In[ ]:



