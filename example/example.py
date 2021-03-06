# Example
# %%
from ipyccmd import display_ccmd, DisplayType
from ipyccmd import md_print
import numpy as np

r = 5
h = 20
volume = np.pi * r**2 * h
"---".md()
"## Using `display_ccmd()` or curse `.md()`".md(dtype=DisplayType.MARKDOWN)
"<hr>".md(dtype=DisplayType.HTML)
"""Thus we have calculated the **volume** of the *cylinder* by using the formula
$$ V = \pi r^2 h $$

Read on...""".md()
"Now we'll calculate the area as per $A = \pi r^2 + 2 \pi r h$.".md()
A = np.pi * r**2 + 2 * np.pi * r * h
display_ccmd("<h2>Volume of a cone is given by:</h2>", dtype=DisplayType.HTML)
"V = {1 \over 3} \pi r^2 h".md(DisplayType.MATH)
f"New array = \n{np.array_str(np.array([[1, 2],[3, 4]]))}".md(DisplayType.PRETTY)
(2).md(DisplayType.MATH) # .md() is not limited to strings
object().md() # any object can be displayed/printed

################################################################################
md_print("---", dtype=DisplayType.MARKDOWN) # we'll use md_print for print henceforth
print = md_print
print("<h2>Will now use overridden print()</h2>", is_md=True, dtype=DisplayType.HTML)
print("<hr>", dtype=DisplayType.HTML)

print("""Thus we have calculated the **volume** of the *cylinder* by using the formula
$$ V = \pi r^2 h $$

Read on...""")
"Now we'll calculate the area as per $A = \pi r^2 + 2 \pi r h$.".md()
A = np.pi * r**2 + 2 * np.pi * r * h
print("<h2>Volume of a cone is given by:</h2>", dtype=DisplayType.HTML)
print("V = {1 \over 3} \pi r^2 h", dtype=DisplayType.MATH)
print(f"New array = \n{np.array_str(np.array([[1, 2],[3, 4]]))}", dtype=DisplayType.PRETTY)
print(2, is_md=True, dtype=DisplayType.MATH) # the new print can handle other objects as well
print(object(), is_md=True) # any object can be displayed/printed

################################################################################
from graphviz import Digraph
dot = Digraph()
dot.node(name="3", label="3")
dot.node(name="1", label="1")
dot.edge("3", "1")
dot.node(name="6", label="6")
dot.edge("3", "6")
dot.md() # default DisplayType is PRETTY for non-string types
dot.md(DisplayType.NONE) # IPython's display() will handle this now and print show the graph

############# For output in IPython, see the notebook example.ipynb #############
################################ Python Output #################################
# ---
# Using display_ccmd() or curse .md()

# Thus we have calculated the **volume** of the *cylinder* by using the formula
# $$ V = \pi r^2 h $$

# Read on...
# Now we'll calculate the area as per $A = \pi r^2 + 2 \pi r h$.
# Volume of a cone is given by:
# V = {1 \over 3} \pi r^2 h
# New array =
# [[1 2]
#  [3 4]]
# 2
# <object object at 0x00000211FB63FA00>

# Will now use overridden print()

# Thus we have calculated the **volume** of the *cylinder* by using the formula
# $$ V = \pi r^2 h $$

# Read on...
# Now we'll calculate the area as per $A = \pi r^2 + 2 \pi r h$.
# Volume of a cone is given by:
# V = {1 \over 3} \pi r^2 h
# New array =
# [[1 2]
#  [3 4]]
# 2
# <object object at 0x00000211FB63F9E0>
# digraph {
#         3 [label=3]
#         1 [label=1]
#         3 -> 1
#         6 [label=6]
#         3 -> 6
# }
# digraph {
#         3 [label=3]
#         1 [label=1]
#         3 -> 1
#         6 [label=6]
#         3 -> 6
# }