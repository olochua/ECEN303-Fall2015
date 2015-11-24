__NetID__ = "gka243"
__GitHubID__ = "gka243"
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

pylab.figure()
n, bins, patches = pylab.hist(Sequence1, 1000, normed=1, histtype='stepfilled')
pylab.setp(patches, 'facecolor', 'r', 'alpha', 0.75)

pylab.figure()
n, bins, patches = pylab.hist(Sequence2, 1000, normed=1, histtype='stepfilled')
pylab.setp(patches, 'facecolor', 'b', 'alpha', 0.75)

pylab.figure()
n, bins, patches = pylab.hist(Sequence3, 1000, normed=1, histtype='stepfilled')
pylab.setp(patches, 'facecolor', 'y', 'alpha', 0.75)

pylab.show()

print(numpy.mean(Sequence1)) #"Mean of Sequence1"
print(numpy.var(Sequence1)) #"Variance of Sequence1"
print(numpy.mean(Sequence2)) #"Mean of Sequence2"
print(numpy.var(Sequence2)) #"Variance of Sequence2"
print(numpy.mean(Sequence3)) #"Mean of Sequence3"
print(numpy.var(Sequence3)) #"Variance of Sequence3"
print(numpy.cov(Sequence1,Sequence2)) #Covariance of Sequence one and two (top right and bottom left values)

"""
What is the type of random variable `Sequence1`?
Gaussian Distribution
What is its mean and variance?
Mean = -0.008
Var = 0.997
What is the type of random variable `Sequence2`?
Gaussian Distribution
What is its mean and variance?
Mean = -0.004
Var = 1.002
What is the type of random variable `Sequence3`?
Exponential Distribution
What is its mean and variance?
Mean = 1.999
Var = 4.015
What is the empirical covariance between `Sequence1` and `Sequence2`?
Covariance = 0.001
Do you think they are independent? Justify your answer.
Yes, because the covariance of sequence1, sequence2 is very close to zero, it is possible for them to be independent. 
It is farther proven that they show independence because the sum of the expectations for Sequence1^2 and Sequence2^2 is
equal to the expectation of the sum Sequence1^2 + Sequence2^2.
"""

