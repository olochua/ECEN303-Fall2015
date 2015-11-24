__NetID__ = "smadi94"
__GitHubID__ = "smadi94"
__SelfGrade__ = "4"
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
pylab.title("sequence 1")
n, bins, patches = pylab.hist(Sequence1, 1000, normed=1, histtype='stepfilled')
pylab.setp(patches, 'facecolor', 'b', 'alpha', 1)
pylab.figure("sequence 2")
pylab.title("sequence 2")
n, bins, patches = pylab.hist(Sequence2, 1000, normed=1, histtype='stepfilled')
pylab.setp(patches, 'facecolor', 'b', 'alpha', 1)
pylab.figure("sequence 3")
pylab.title("sequence 3")
n, bins, patches = pylab.hist(Sequence3, 1000, normed=1, histtype='stepfilled')
pylab.setp(patches, 'facecolor', 'b', 'alpha', 1)
pylab.show()

mean1 = numpy.mean(Sequence1)
print "mean 1 = %f " %mean1
var1 = numpy.var(Sequence1)
print "var 1 = %f " %var1

mean2 = numpy.mean(Sequence2)
print "mean 2 = %f " %mean2
var2 = numpy.var(Sequence2)
print "var 2 = %f " %var2

mean3 = numpy.mean(Sequence3)
print "mean 3 = %f " %mean3
var3 = numpy.var(Sequence3)
print "var 3 = %f " %var3

cov1 = numpy.cov(Sequence1, Sequence2)[0][1]
print "covariance = "
print cov1

"""
What is the type of random variable `Sequence1`?
It is a gaussian random variable

What is its mean and variance?
The mean is about 0 with little variation in the thousands place and the
average is about 1 with small variation in the thousands place

What is the type of random variable `Sequence2`?
It is a gaussian random variable

What is its mean and variance?
The mean is about 0 with little variation in the thousands place and the
average is about 1 with small variation in the thousands place

What is the type of random variable `Sequence3`?
It is a exponential random variable

What is its mean and variance?
The mean is about 2 with little variation in the thousands place and the
average is about 4 with small variation in the thousands place

What is the empirical covariance between `Sequence1` and `Sequence2`?
Do you think they are independent? Justify your answer.
The covariance must be 0 for the random variables to be independent. The covariance between
sequence 1 and 2 is almost 0, so I think they are independent.
"""

