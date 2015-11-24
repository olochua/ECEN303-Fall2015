# -*- coding: utf-8 -*-
__author__ = 'Jonathan Moore'
__NetID__ = "spirituallyinsane"
__GitHubID__ = "spirituallyinsane"
__SelfGrade__ = ""
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
pylab.setp(patches, 'facecolor', 'g', 'alpha', 0.75)

pylab.figure()
n, bins, patches = pylab.hist(Sequence3, 1000, normed=1, histtype='stepfilled')
pylab.setp(patches, 'facecolor', 'b', 'alpha', 0.75)

pylab.show()

print("Sequence1 mean = ", numpy.mean(Sequence1) )
print("Sequence1 variance = ", numpy.var(Sequence1) )

print("Sequence2 mean = ", numpy.mean(Sequence2) )
print("Sequence2 variance = ", numpy.var(Sequence2) )

print("Sequence3 mean = ", numpy.mean(Sequence3) )
print("Sequence3 variance = ", numpy.var(Sequence3) )

print("Sequence 1 and 2 covariance:\n", numpy.cov(Sequence1, Sequence2))

"""
What is the type of random variable `Sequence1`?
Sequence1 appears to be a Gaussian random variable.
What is its mean and variance?
Mean is 0.  Variance is 1.

What is the type of random variable `Sequence2`?
Sequence2 also looks like a Gaussian random variable
What is its mean and variance?
Mean is 0.  Variance is 1.

What is the type of random variable `Sequence3`?
This one looks like an exponential random variable
What is its mean and variance?
Mean is 2.  Variance is 4.

What is the empirical covariance between `Sequence1` and `Sequence2`?
 [[  9.93169271e-01  -4.71598801e-04]
 [ -4.71598801e-04   9.93058514e-01]]
 
 Covariance is about 9.93.
 
Do you think they are independent? Justify your answer.
I do not think they are independent, because their covariance is nonzero.
A zero covariance does not imply independence, but is a required condition for it.
"""