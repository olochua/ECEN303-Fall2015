__author__ = "Rodney Siders"
__NetID__ = "Rodney6359"
__GitHubID__ = "rodney6359"
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

Sequence1 = []
Sequence2 = []
Sequence3 = []
for trial2 in range(0, TrialNumber):
    Sequence1.append(math.sin(UniformList[trial2]) * RayleighList[trial2])
    Sequence2.append(math.cos(UniformList[trial2]) * RayleighList[trial2])
    Sequence3.append(Sequence1[trial2]**2 + Sequence2[trial2]**2)

pylab.figure()#the graph of Sequence1
n, bins, patches = pylab.hist(Sequence1, 1000, normed=1, histtype='stepfilled')
pylab.setp(patches, 'facecolor', 'g', 'alpha', 0.75)

pylab.figure()#the graph of Sequence2
n, bins, patches = pylab.hist(Sequence2, 1000, normed=1, histtype='stepfilled')
pylab.setp(patches, 'facecolor', 'y', 'alpha', 0.75)

pylab.figure()#the graph of Sequence3
n, bins, patches = pylab.hist(Sequence3, 1000, normed=1, histtype='stepfilled')
pylab.setp(patches, 'facecolor', 'b', 'alpha', 0.75)

pylab.show()
#compute the mean and var of Sequence 1, 2, 3
print 'Sequence1'
print 'mean = ',numpy.mean(Sequence1)
print 'variance = ',numpy.var(Sequence1)
print 'Sequence2'
print 'mean = ',numpy.mean(Sequence2)
print 'variance = ',numpy.var(Sequence2)
print 'Sequence3'
print 'mean = ',numpy.mean(Sequence3)
print 'variance = ',numpy.var(Sequence3)
print 'Covariance of sequence 1&2'
print numpy.cov(Sequence1,Sequence2)

"""
What is the type of random variable `Sequence1`?
Sequence1 is a Continuous Random Variable with Rayleigh Distribution of a sine.

What is its mean and variance?
The mean is about 0.
The variance is about 1.

What is the type of random variable `Sequence2`?
Sequence2 is a CRV with Rayleigh Distribution of a cosine.

What is its mean and variance?
The mean is about 0.
The variance is about 1.

What is the type of random variable `Sequence3`?
Sequence3 is a CRV with Rayleigh Distribution of a cosine multiplied with a sine.

What is its mean and variance?
The mean is about 2.
The variance is about 4.

What is the empirical covariance between `Sequence1` and `Sequence2`?
It is very close 0.

Do you think they are independent? Justify your answer.
Yes. When the covariance is 0 then Sequence1 and Sequence2 are independant.
"""

