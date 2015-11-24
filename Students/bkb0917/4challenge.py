__author__ = "Bailey Barksdale"
__NetID__ = "bailey13"
__GitHubID__ = "bkb0917"
__SelfGrade__ = "4"
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

print("Sequence 1 Mean: ",numpy.mean(Sequence1))
print("Sequence 1 Variance: ",numpy.var(Sequence1))
print("Sequence 2 Mean: ",numpy.mean(Sequence2))
print("Sequence 2 Variance: ",numpy.var(Sequence2))
print("Sequence 3 Mean: ",numpy.mean(Sequence3))
print("Sequence 3 Variance: ",numpy.var(Sequence3))
print("Covariance of Sequences 1 and 2: ",numpy.cov(Sequence1,Sequence2))

pylab.figure()
n, bins, patches = pylab.hist(Sequence1, 1000, normed=1, histtype='stepfilled')
pylab.setp(patches, 'facecolor', 'k', 'alpha', 0.75)

pylab.figure()
n, bins, patches = pylab.hist(Sequence2, 1000, normed=1, histtype='stepfilled')
pylab.setp(patches, 'facecolor', 'g', 'alpha', 0.75)

pylab.figure()
n, bins, patches = pylab.hist(Sequence3, 1000, normed=1, histtype='stepfilled')
pylab.setp(patches, 'facecolor', 'r', 'alpha', 0.75)

pylab.show()

"""
What is the type of random variable `Sequence1`?
Sequence 1 is a gaussian random variable

What is its mean and variance?
Mean: 0
Variance: 1

What is the type of random variable `Sequence2`?
Sequence 2 is a gaussian random variable

What is its mean and variance?
Mean: 0
Variance: 1

What is the type of random variable `Sequence3`?
Sequence 3 is an exponential random variable

What is its mean and variance?
Mean: 2
Variance: 4

What is the empirical covariance between `Sequence1` and `Sequence2`?
Empirical Covariance: 0
Do you think they are independent? Justify your answer.
Yes, because the covariance of two variables for example X and Y is equivalent to
Cov(X,Y) = E[XY] - E[X]E[Y] and since the covariance is 0, then
E[XY] = E[X]E[Y] and thus the two random variables Sequence1 and
Sequence 2 are independent.
"""

