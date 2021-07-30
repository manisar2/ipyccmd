## Show Markdown from within Code Cells in Jupyter and VS Code's Interactive Python

## Description
Display markdown from within code cells in IPython output, while ignoring it when run in normal Python (like usual comments).

More details and explanation on [randompearls.com](https://randompearls.com/science-and-technology/information-technology/coding-and-development-reference-and-tools/show-markdown-within-code-cells-jupyter-and-vs-code-interactive-python/).

## Dependencies
These packages are auto-installed during the installation of this package.
* forbiddenfruit
* markdown
* beautifulsoup4

*IPython* is not installed automatically.<br>
This is because if you use the overridden print statements (explained below), they are supposed to work without IPython as well.<br>
But, if you do have IPython, those print statements will print formatted text.

Note that *forbiddenfruit* is installed as a dependency, so that statements of the form `"*anymdstring*".md(type=DisplayType.Type)` can be used conveniently.<br>

You can uninstall forbiddenfruit if you want and then use `display_string("*anymdstring*", type=DisplayType=Type)`.

## Installation
The package can be installed by running `pip install git+https://github.com/manisar2/ipyccmd.git`.
<br>Or copy the code from *src/ipyccmd/\_\_init\_\_.py* into your project.

## Usage
It can be used in two ways depending upon your taste:
* using function `display_string()` (or curse function `.md()`), or 
* by overriding `print()`.

Note that you will not need the import statements shown below if you have copy-pasted the code from *src/ipyccmd/\_\_init\_\_.py* into your current file.

### A. Using `display_string()` or curse `.md()`:
```python
# With curse .md():
from ipyccmd import DisplayType
"Now we'll *calculate* the **area** as per $A = \pi r^2 + 2 \pi r h$.".md()
"V = {1 \over 3} \pi r^2 h".md(type=DisplayType.MATH, python_print=True)

# Without using curse (can uninstall forbiddenfruit):
from ipyccmd import display_string, DisplayType
display_string("Now we'll calculate the area as per $A = \pi r^2 + 2 \pi r h$.")
display_string("V = {1 \over 3} \pi r^2 h", type=DisplayType.MATH, python_print=True)

# In both the cases, if you pass python_print=True or set global PYTHON_PRINT=True (default), the string will also be printed when the code is run as normal Python - with markdown symbols removed (except equation symbols).

# Thus, you can have your string displayed in both IPython and Python - with formatting and without markdown symbols respectively.
```
### B. By Overriding `print()`:
```python
from ipyccmd import md_print, DisplayType
print = md_print
print("Now we'll *calculate* the **area** as per $A = \pi r^2 + 2 \pi r h$.")
print("V = {1 \over 3} \pi r^2 h", is_md=True, type=DisplayType.MATH)
# This overriden print will ensure that the string is displayed in both IPython (formatted) and Python (with markdown symbols removed).

# The value of the argument is_md or global IS_MD will work as follows:
#   True (default) => formatted text in IPython, plain_text (without markdown symbols) in Python
#   False => unmodified text in both IPython and Python (like normal print)
```

The advantage with B. is that if `print()` is used without any arguments (`is_md` and `type`), all the print statements will continue to work in both IPython and Python even *without* this package, thus giving you the option of not using this package in production.

### See a [.py](example/example.py) or [notebook](example/ipy_md.ipynb) example.
### The [notebook](example/ipy_md.ipynb) shows some of the outputs generated by using different DisplayTypes. 

### The display can be modified in these ways (using `type` argument):
* MARKDOWN
* LATEX
* MATH
* HTML
* PRETTY
