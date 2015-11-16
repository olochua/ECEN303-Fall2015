# Programming Challenge 4

In this [Python](https://www.python.org) challenge, you will generate continuous random variables.
As before, this challenge will leverage the Python `random` and `math` modules, along with the [matplotlib](http://matplotlib.org/) library.

```python
import random
import math
import matplotlib.pyplot as plt
```

Generate pseudo-random numbers using `random.uniform(0,math.PI)` and `random.expovariate(1)`.

```python
TrialNumber = 10000
UniformList = []
ExpoList = []
for trial1 in range(0, TrialNumber):
  UniformList.append(random.uniform(0,math.PI))
  ExpoList.append(random.expovariate(1))
```

Plot the empirical distributions associated with `UniformList` and `ExpoList` using binning/quantization or cummulative distribution functions.
Next, create the following random variables.

```python
for trial2 in range(0, TrialNumber):
  Sequence1.append(math.sin(UniformList[trial2]) * ExpoList[trial2])
  Sequence2.append(math.cos(UniformList[trial2]) * ExpoList[trial2])
  Sequence3.append(math.sqrt(Sequence1[trial2]**2 + Sequence2[trial2]**2))
```

Plot the empirical distributions associated with `Sequence1`, `Sequence2`, `Sequence3` using binning/quantization or cummulative distribution functions.
Find the empirical mean and variance of `Sequence1` and `Sequence2`.
Find the empirical covariance of `Sequence1` and `Sequence2`.


