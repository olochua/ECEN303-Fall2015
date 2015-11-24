__NetID__ = "chaswallace3"
__GitHubID__ = "chaswallace3"
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
pylab.setp(patches, 'facecolor', 'b', 'alpha', 0.75)

pylab.figure()
n, bins, patches = pylab.hist(Sequence3, 1000, normed=1, histtype='stepfilled')
pylab.setp(patches, 'facecolor', 'k', 'alpha', 0.75)

pylab.show()

print("Mean of sequence 1:")
print(sum(Sequence1)/len(Sequence1))
print("Variance of sequence 1:")
print(numpy.var(Sequence1))

print("Mean of sequence 2:")
print(sum(Sequence2)/len(Sequence2))
print("Variance of sequence 2:")
print(numpy.var(Sequence2))

print("Mean of sequence 3:")
print(sum(Sequence3)/len(Sequence3))
print("Variance of sequence 3:")
print(numpy.var(Sequence3))

print("Covariance between Sequence 1 and Sequence 2:")
print(numpy.cov([Sequence1,Sequence2]))

"""
What is the type of random variable `Sequence1`?
'Sequence1' appears to be a gaussian random variable

What is its mean and variance?
The mean of Sequence1 appears to be very close to 0, and its
variance is close to 1

What is the type of random variable `Sequence2`?
'Sequence2' appears to be a gaussian random variable

What is its mean and variance?
The mean of Sequence2 appears to be very close to 0 and its
variance is close to 1

What is the type of random variable `Sequence3`?
'Sequence3' appears to be an exponential random variable

What is its mean and variance?
The mean of Sequence3 appears to be close to 2 while the
variance is close to 4

What is the empirical covariance between `Sequence1` and `Sequence2`?
The empirical covariance matrix appears to be the unit matrix. This indicates a
covariance of 0.

Do you think they are independent? Justify your answer.
Yes, since the coariance matrix is very close to the identity matrix, it
is safe to assume that Sequence1 and Sequence2 are independent.
"""

