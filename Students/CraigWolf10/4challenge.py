__author__ = 'Craig Wolf'
__NetID__ = "Dallascowboys10"
__GitHubID__ = "Craigwolf10"
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
pylab.setp(patches, 'facecolor', 'y', 'alpha', 0.75)

pylab.figure()
n, bins, patches = pylab.hist(Sequence3, 1000, normed=1, histtype='stepfilled')
pylab.setp(patches, 'facecolor', 'c', 'alpha', 0.75)

pylab.show()

print "mean1: "
print sum(Sequence1)/len(Sequence1)
print "mean2: "
print sum(Sequence2)/len(Sequence2)
print "mean3: "
print sum(Sequence3)/len(Sequence3)
print "variance1: "
print numpy.var(Sequence1)
print "variance2: "
print numpy.var(Sequence2)
print "variance3: "
print numpy.var(Sequence3)
print "covariance1: "
print numpy.cov(Sequence1,Sequence2)
"""
What is the type of random variable `Sequence1`?
Sequence 1 looks like it is a Gaussian random variable.
What is its mean and variance?
The mean of a Sequence1 is about 0, and it's variance is about 1.
What is the type of random variable `Sequence2`?
Sequence 2 looks like it is a Gaussian random variable.
What is its mean and variance?
The mean of a Sequence2 is about 0, and it's variance is about 1.
What is the type of random variable `Sequence3`?
Sequence3 looks like it is an exponential random variable.
What is its mean and variance?
The mean of a Sequence3 is about 2, and it's variance is about 4.
What is the empirical covariance between `Sequence1` and `Sequence2`?
The empirical covariance between Sequence1 and Sequence2 is very close to zero.
Do you think they are independent? Justify your answer.
I do think that Sequence1 and Sequence 2 are independent. I am led to believe this because
the covariance between the two is almost 0, showing they have little impact on eachother
and are therefore likely independent.
"""
