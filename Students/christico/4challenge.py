__NetID__ = "christico"
__GitHubID__ = "christico"
__SelfGrade__ = "5"
__Challenge__ = "4"

"""
Random Signals and Systems
Course: ECEN 303-502
Maximum Grade: 5pt
"""

import random
import math
import numpy
import pylab

TrialNumber = 100000

UniformList = []
RayleighList = []
for trial1 in range(0, TrialNumber):
    UniformList.append(random.uniform(0, 2*math.pi))
    RayleighList.append(numpy.random.rayleigh(1))

pylab.figure()
n, bins, patches = pylab.hist(UniformList, 1000, normed=1, histtype='stepfilled')
pylab.setp(patches, 'facecolor', 'k', 'alpha', 0.75)

pylab.figure()
n, bins, patches = pylab.hist(RayleighList, 1000, normed=1, histtype='stepfilled')
pylab.setp(patches, 'facecolor', 'g', 'alpha', 0.75)

pylab.show()

Sequence1 = []
Sequence2 = []
Sequence3 = []
for trial2 in range(0, TrialNumber):
    Sequence1.append(math.sin(UniformList[trial2]) * RayleighList[trial2])
    Sequence2.append(math.cos(UniformList[trial2]) * RayleighList[trial2])
    Sequence3.append(Sequence1[trial2]**2 + Sequence2[trial2]**2)

#1
pylab.figure()
n, bins, patches = pylab.hist(Sequence1, 1000, normed=1, histtype='stepfilled')
pylab.setp(patches, 'facecolor', 'r', 'alpha', 0.75)
print(numpy.mean(Sequence1))
print(numpy.var(Sequence1))

#2
pylab.figure()
n, bins, patches = pylab.hist(Sequence2, 1000, normed=1, histtype='stepfilled')
pylab.setp(patches, 'facecolor', 'y', 'alpha', 0.75)
print(numpy.mean(Sequence2))
print(numpy.var(Sequence2))

#3
pylab.figure()
n, bins, patches = pylab.hist(Sequence3, 1000, normed=1, histtype='stepfilled')
pylab.setp(patches, 'facecolor', 'b', 'alpha', 0.75)
print(numpy.mean(Sequence3))
print(numpy.var(Sequence3))

#1 and 2
print(numpy.cov(Sequence1, Sequence2))

pylab.show()

"""
What is the type of random variable `Sequence1`?
continous variable
What is its mean and variance?
the mean is 0.00153794226134 and the variace is 1.00114986622
What is the type of random variable `Sequence2`?
Continous random variable
What is its mean and variance?
mean is 0.00435700319648 and variance is 1.00156473713
What is the type of random variable `Sequence3`?
Continous random variable
What is its mean and variance?
mean is 2.0027359521 and the variance is 4.00746515898
What is the empirical covariance between `Sequence1` and `Sequence2`?
[[ 1.00305421  0.00135518]
 [ 0.00135518  0.99802861]]
 the covariance is zero 
Do you think they are independent? Justify your answer.
Yes they are both independed because the covariance is zero 
"""

