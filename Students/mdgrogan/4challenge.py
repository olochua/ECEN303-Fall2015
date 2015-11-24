__NetID__ = "grogab2122"
__GitHubID__ = "mdgrogan"
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
pylab.title('UniformList')

pylab.figure()
n, bins, patches = pylab.hist(RayleighList, 1000, normed=1, histtype='stepfilled')
pylab.setp(patches, 'facecolor', 'g', 'alpha', 0.75)
pylab.title('RayleighList')

Sequence1 = []
Sequence2 = []
Sequence3 = []
for trial2 in range(0, TrialNumber):
    Sequence1.append(math.sin(UniformList[trial2]) * RayleighList[trial2])
    Sequence2.append(math.cos(UniformList[trial2]) * RayleighList[trial2])
    Sequence3.append(Sequence1[trial2]**2 + Sequence2[trial2]**2)

pylab.figure()
n, bins, patches = pylab.hist(Sequence1, 1000, normed=1, histtype='stepfilled')
pylab.setp(patches, 'facecolor', 'g', 'alpha', 0.75)
pylab.title('Sequence1')

pylab.figure()
n, bins, patches = pylab.hist(Sequence2, 1000, normed=1, histtype='stepfilled')
pylab.setp(patches, 'facecolor', 'g', 'alpha', 0.75)
pylab.title('Sequence2')

pylab.figure()
n, bins, patches = pylab.hist(Sequence3, 1000, normed=1, histtype='stepfilled')
pylab.setp(patches, 'facecolor', 'g', 'alpha', 0.75)
pylab.title('Sequence3')

print('Sequence1: mean={:f}, variance={:f}'.format(numpy.mean(Sequence1),numpy.var(Sequence1)))
print('Sequence2: mean={:f}, variance={:f}'.format(numpy.mean(Sequence2),numpy.var(Sequence2)))
print('Sequence3: mean={:f}, variance={:f}'.format(numpy.mean(Sequence3),numpy.var(Sequence3)))
print('Covariance between 1 and 2:')
print(numpy.cov(Sequence1,Sequence2))

pylab.show()

"""
What is the type of random variable `Sequence1`?
    looks like a Gaussian
What is its mean and variance?
    0, 1
What is the type of random variable `Sequence2`?
    looks like another Gaussian
What is its mean and variance?
    0, 1
What is the type of random variable `Sequence3`?
    exponential
What is its mean and variance?
    2, 4
What is the empirical covariance between `Sequence1` and `Sequence2`?
    0
Do you think they are independent? Justify your answer.
    yes, due to an empirical covariance of 0.
"""
