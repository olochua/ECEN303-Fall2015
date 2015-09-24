# Programming Challenge 2

In this [Python](https://www.python.org) challenge, you will leverage the `biasedcoinflip()` module you created previously to explore conditional probabilities.
An sample method appears below.

```python
import random
import math

def biasedcoinflip(p=0.5):
    """
    This method returns a one with probability p and it returns a zero with
    probability (1 - p). The default parameter is p=0.5; this can be changed
    by passing an argument to the method.
    """
    return math.floor(random.random() + p)
```

Consider the random experiment where the binary coin `biasedcoinflip()` is flipped until 1 is obtained.
The outcome of this experiment is the number of coin tosses needed to complete the task.
Implement this method using a `while` loop.

```python
def geometricflip(p=0.5):
    """
    This method returns a natural number that denotes the number of digital
    coin flips needed to obtain a one. It relies on method biasedcoinflip().
    """
    #
    # EDIT (possibly using while loop)
    #
    return numberflips
```

Address the following two problems.

1. Find The empirical probability that the number of flips is 4 when `p = 1.0/3.0`.
2. Find the conditional probability that the number of flips is 4 when `p = 1.0/3.0` conditional on number of flips being even.


For the part below, consider the following scenario.
The experiment consists in repetitively flipping binary coin `A` with `ParameterA = 1.0/3.0` and binary coint `B` with `ParamterB = 1.0/2.0` until one of the two coins is 1 and the other shows 0.
The outcome of this experiment is the again the number of coin tosses until the stopping condition is reached.

Address the following two problems.

1. Find The empirical probability that the number of flips is 2.
2. Find the empirical probability that coin `A` is showing 1 when the stopping condition is met.
3. Find the empirical probability that coin `B` is showing 1 when the stopping condition is met.


## Submission

A template named `2challenge.py` has been placed in your personal folder.
Edit this template and address the 5 problems.
After completing this programming challenge, fill out the self-grading portion.
Commit your work to our repository using Git and GitHub.
