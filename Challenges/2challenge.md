# Programming Challenge 2

In this [Python](https://www.python.org) challenge, you will leverage the `biasedcoinflip()` module you created previously to explore conditional probabilities.

```python
import random


def biasedcoinflip(p=0.5):
    #
    # [...]
    #
```

Consider the random experiment where the binary coin `biasedcoinflip()` is flipped until a one is obtained.
The outcome of this experiment is the total number of coin tosses needed to complete the task.
Implement this method using a `while` loop.

```python
def flipsuntilone(ParameterP=0.5)

totalflips = 1
while biasedcoinflip(ParameterP) != 1:
  totalflips += 1
```

Address the following two problems.

1. Find the approximate probability that the total number of flips is 4 when `ParameterP = 1/3`.
2. Find the conditional probability that the total number of flips is 4 for `ParameterP = 1/3` conditional on the total number of flip being even.


For the part below, consider the following scenario.
One experiment consists in repetitively flipping binary coin `A` with `ParameterA = 1/2` and binary coint `B` with `ParamterB = 1/3` until one of the two coins is one and the other one is zero.
The outcome of this experiment is the again the total number of coin tosses until the stopping condition is reached.

Address the following two problems.

1. Find the approximate probability that the total number of flips is two.
2. Find the approximate probability that coin `A` is showing a one when the stopping condition is met.


## Submission

A template named `2challenge.py` will be placed in your personal folder.
Edit this template and address the problems at the end.
After completing this programming challenge, fill out the self-grading portion.
Commit your work to our repository using Git and GitHub.

