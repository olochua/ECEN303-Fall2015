__author__ = "Jonathan Moore"
__NetID__ = "spirituallyinsane"
__GitHubID__ = "spirituallyinsane"
__challenge__ = "1"
__version__ = "1.0"
__grader__ = ""
__SelfGrade__ = ""
__PeerGrade__ = ""

"""
Random Signals and Systems
Course: ECEN 303-502
Maximum Grade: 5pt
"""

import random

def biasedcoinflip(p=0.5):
    if(random.random() < p)
        return 1
    else
        return 0

Create a method that sums `NumberFlips` outcomes of `biasedcoinflip()` and appends the result to list `SumTrials`.

```python
SumTrials = []

for TrialIndex2 in range(0, NumberTrials):
    # EDIT
    # Add NumberFlips coin flips for each SumTrials outcome
    #
```

Sum the values of all the elements contained in list `Distribution` and print the result.

```python
print repr(Distribution)
# EDIT
# Print the sum of the elements in Distribution
#
```

Address the following two problems.

1. Describe what happens to the figure as you vary `ParameterP` from zero to one.
2. What is the most likely outcome for `ParameterP = 0.7` and `NumberFlips = 8`?


## Submission

A template named `1challenge.py` has been placed in your personal folder.
Edit this template and address the two problems at the end.
After completing this programming challenge, fill out the self-grading portion.
Commit your work to our repository using Git and GitHub.

