# Programming Challenge 3

Again, in this [Python](https://www.python.org) challenge, you will leverage the `biasedcoinflip()` module that you created as part of Challenge 1.
A sample method appears below.

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

A binomial random variable with parameter `n` and `p` can be created by summing exactly `n` biased coin flips.

```python
def binomialflips(n=1,p=0.5):
    """
    This method returns a binomial random variable with parameters n and p. The default parameters are n=1 and
    p=0.5; this can be changed by passing arguments to the method.
    """
    numberones = 0
    for BinomialIndex in range(0,n):
        numberones += biasedcoinflip(p)
    return numberones
```

Create a method that return a Poisson random variable.

```python
def poisson(lambda=10):
    #
    # EDIT
    #
```

Next, create a random variable through the following process.
First, use the `poisson()` method with paramater `parameterpoisson=10` to generate an integer.
Then, use this integer as the first argument in `binomialflips()`, along with `p=0.5` as the second argument.
The output of this latter method is the outcome of the experiment.

```python
def experiment3(parameterpoisson3=10,p=0.5):
    return binomialflips(poisson(parameterpoisson3),p)
```

Use averaging over a large number of trials to get an approximate value for the mean of `experiment3()`.
Plot the distribution of `experiment3()` and try to guess its type.
Do you get the same distribution if you use `poisson(binomialflips(parameterpoisson,p))` instead of `binomialflips(poisson(parameterpoisson),p)`?

