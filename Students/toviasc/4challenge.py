__NetID__ = "toviasc"
__GitHubID__ = "toviasc"
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
pylab.setp(patches, 'facecolor', 'b', 'alpha', 0.75)
print "Mean 1: "
print(numpy.mean(Sequence1))
print "Variance 1: "
print(numpy.var(Sequence1)), "\n"


pylab.figure()
n, bins, patches = pylab.hist(Sequence2, 1000, normed=1, histtype='stepfilled')
pylab.setp(patches, 'facecolor', 'r', 'alpha', 0.75)
print "Mean 2: "
print(numpy.mean(Sequence2))
print "Variance 2: "
print(numpy.var(Sequence2)), "\n"


pylab.figure()
n, bins, patches = pylab.hist(Sequence3, 1000, normed=1, histtype='stepfilled')
pylab.setp(patches, 'facecolor', 'y', 'alpha', 0.75)
print "Mean 3: "
print(numpy.mean(Sequence3))
print "Variance 3: "
print(numpy.var(Sequence3)), "\n"

print "Covariance: "
print(numpy.cov(Sequence1, Sequence2))

pylab.show()

"""
What is the type of random variable `Sequence1`?
Sequence 1 is a Gaussian random variable.
What is its mean and variance?
The mean is approx. 0 and the variance is approx. 1.


What is the type of random variable `Sequence2`?
Sequence 2 is a Gaussian random variable.
What is its mean and variance?
The mean is approx. 0 and the variance is approx. 1.


What is the type of random variable `Sequence3`?
Sequence 3 is an exponential random variable.
What is its mean and variance?
The mean is approx. 2 and the variance is approx. 4.


What is the empirical covariance between `Sequence1` and `Sequence2`?
The empirical covariance is approx. zero. 
Do you think they are independent? Justify your answer.
Yes, because the covariance is zero sequence 1 and sequence 2 are independent. 

"""

