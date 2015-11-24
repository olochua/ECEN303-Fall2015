__NetID__ = "Shannon Morrissey"
__GitHubID__ = "shmorrissey"
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

#sequence1 plot, mean, variance
pylab.figure()
n, bins, patches = pylab.hist(Sequence1, 1000, normed=1, histtype='stepfilled')
pylab.setp(patches, 'facecolor', 'b', 'alpha', 0.75)
print(numpy.mean(Sequence1))
print(numpy.var(Sequence1))

#sequence2 plot, mean, variance
pylab.figure()
n, bins, patches = pylab.hist(Sequence2, 1000, normed=1, histtype='stepfilled')
pylab.setp(patches, 'facecolor', 'r', 'alpha', 0.75)
print(numpy.mean(Sequence2))
print(numpy.var(Sequence2))

#sequence3 plot, mean, variance
pylab.figure()
n, bins, patches = pylab.hist(Sequence3, 1000, normed=1, histtype='stepfilled')
pylab.setp(patches, 'facecolor', 'y', 'alpha', 0.75)
print(numpy.mean(Sequence3))
print(numpy.var(Sequence3))

#comparison of covarianve between Sequence 1 & 2
print(numpy.cov(Sequence1, Sequence2))

pylab.show()

"""
What is the type of random variable `Sequence1`?
Sequence 1 is a Continuous random variable.
What is its mean and variance?
Its mean is close to 0 and its variance it about 1.
What is the type of random variable `Sequence2`?
Sequence 2 is a Continuous random variable.
What is its mean and variance?
Its mean is around 0 and its variance is about 1.
What is the type of random variable `Sequence3`?
Sequence 3 is a continuous random variable that looks like the conbination of the first two sequences.
What is its mean and variance?
Its mean is about 2 and its variance is close to 4.
What is the empirical covariance between `Sequence1` and `Sequence2`?
The covariance between Sequence 1 & 2 is about 0.
Do you think they are independent? Justify your answer.
I believe these two sequences are independent because the covariance is 0,
which shows that the sequences have little impact on one another.  
"""
