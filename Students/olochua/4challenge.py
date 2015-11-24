__author__ = 'Jui Yen Chua'
__NetID__ = "olochua"
__GitHubID__ = "olochua"
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
pylab.setp(patches, 'facecolor', 'g', 'alpha', 0.75)

pylab.figure()
n, bins, patches = pylab.hist(Sequence3, 1000, normed=1, histtype='stepfilled')
pylab.setp(patches, 'facecolor', 'b', 'alpha', 0.75)

pylab.show()

print "Mean of Sequence1: "
print sum(Sequence1)/len(Sequence1)
print "Variance of Sequence1: "
print numpy.var(Sequence1)

print "Mean of Sequence2: "
print sum(Sequence2)/len(Sequence2)
print "Variance of Sequence2: "
print numpy.var(Sequence2)

print "Mean of Sequence3: "
print sum(Sequence3)/len(Sequence3)
print "Variance of Sequence3: "
print numpy.var(Sequence3)

print "Empirical Covariance between Sequence1 and Sequence2: "
print numpy.cov(Sequence1,Sequence2)

"""
What is the type of random variable `Sequence1`?
Sequence1 is a continuous random variable. 
It has a sine-dependent Rayleigh distribution.

What is its mean and variance?
The mean of Sequence1 is about 0.0039.
The variance of Sequence1 is about 1.0035.

What is the type of random variable `Sequence2`?
Sequence2 is a continuous random variable. 
It has a cosine-dependent Rayleigh distribution.

What is its mean and variance?
The mean of Sequence2 is about -0.003.
The variance of Sequence2 is about 1.00027.

What is the type of random variable `Sequence3`?
Sequence3 is a continuous random variable. 
It has both sine-dependent and cosine-dependent Rayleigh distributions.
The sine-dependent one is multiplied by another Rayleigh distribution 
that is dependent on a cosine function leaving a uniform distribution.

What is its mean and variance?
The mean of Sequence3 is about 2.004.
The variance of Sequence3 is about 4.028.

What is the empirical covariance between `Sequence1` and `Sequence2`?
The empirical covariance between the two is approximately zero.

Do you think they are independent? Justify your answer.
Yes I think so. By definition, two cases are independent when the corresponding 
covariance is zero, which is what is observed in the previous calculation.

"""
