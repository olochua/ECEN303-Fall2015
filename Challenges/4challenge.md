# Programming Challenge 4

In this [Python](https://www.python.org) challenge, you will generate continuous random variables.
As before, this challenge will leverage the Python `random` and `math` modules, along with the `numpy` and `pylab` libraries.

```python
import random
import math
import numpy
import pylab
```

Generate pseudo-random numbers using `random.uniform(0,math.PI)` and `numpy.random.rayleigh(1)`.

```python
TrialNumber = 10000
UniformList = []
RayleighList = []
for trial1 in range(0, TrialNumber):
    UniformList.append(random.uniform(0, 2*math.pi))
    RayleighList.append(numpy.random.rayleigh(1))
```

Plot the empirical distributions associated with `UniformList` and `RayleighList` using binning/quantization or cumulative distribution functions.

```python
pylab.figure()
n, bins, patches = pylab.hist(UniformList, 1000, normed=1, histtype='stepfilled')
pylab.setp(patches, 'facecolor', 'k', 'alpha', 0.75)

pylab.figure()
n, bins, patches = pylab.hist(RayleighList, 1000, normed=1, histtype='stepfilled')
pylab.setp(patches, 'facecolor', 'g', 'alpha', 0.75)

pylab.show()
```

Next, create the following random variables.

```python
Sequence1 = []
Sequence2 = []
Sequence3 = []
for trial2 in range(0, TrialNumber):
    Sequence1.append(math.sin(UniformList[trial2]) * ExpoList[trial2])
    Sequence2.append(math.cos(UniformList[trial2]) * ExpoList[trial2])
    Sequence3.append(math.sqrt(Sequence1[trial2]**2 + Sequence2[trial2]**2))
```

Plot the empirical distributions associated with `Sequence1`, `Sequence2`, `Sequence3` using binning/quantization or cumulative distribution functions.

* What is the type of random variable `Sequence1`?
* What is its mean and variance?
* What is the type of random variable `Sequence2`?
* What is its mean and variance?
* What is the type of random variable `Sequence3`?
* What is its mean and variance?
* What is the empirical covariance between `Sequence1` and `Sequence2`?
* Do you think they are independent? Justify your answer.


