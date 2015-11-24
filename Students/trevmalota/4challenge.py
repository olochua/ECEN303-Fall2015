__NetID__ = "TrevorMalota"
__GitHubID__ = "trevmalota"
__SelfGrade__ = "2"
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

print(numpy.mean(Sequence1))
print(numpy.var(Sequence1))

print(numpy.mean(Sequence2))
print(numpy.var(Sequence2))

print(numpy.mean(Sequence3))
print(numpy.var(Sequence3))

"""
I can't get the numpy library file to work properly so the program won't run.
What is the type of random variable `Sequence1`?
Continuous (sine)
What is its mean and variance?
Since Sequence 1 is a sin function the mean should be 0 and the variance should be 1
What is the type of random variable `Sequence2`?
Continuous (cosine)
What is its mean and variance?
Since it is cosine the mean should be 0 and variance 1
What is the type of random variable `Sequence3`?
What is its mean and variance?
What is the empirical covariance between `Sequence1` and `Sequence2`?
Do you think they are independent? Justify your answer.
They should be independent because they do not rely on each other
"""
