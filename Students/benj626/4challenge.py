__author__ = "Ben Johnston"
__NetID__ = "benj626"
__GitHubID__ = "benj626"
__SelfGrade__ = "5pt"
__Challenge__ = "3"

"""
Random Signals and Systems
Course: ECEN 303-502
Maximum Grade: 5pt
"""

import random
import math
import numpy
import pylab

TrialNumber = 10000
UniformList = []
RayleighList = []
for trial1 in range(0, TrialNumber):
    UniformList.append(random.uniform(0, 2*math.pi))
    RayleighList.append(numpy.random.rayleigh(1))

"""pylab.figure()
n, bins, patches = pylab.hist(UniformList, 1000, normed=1, histtype='stepfilled')
pylab.setp(patches, 'facecolor', 'k', 'alpha', 0.75)

pylab.figure()
n, bins, patches = pylab.hist(RayleighList, 1000, normed=1, histtype='stepfilled')
pylab.setp(patches, 'facecolor', 'g', 'alpha', 0.75)

pylab.show()"""

Sequence1 = []
Sequence2 = []
Sequence3 = []
for trial2 in range(0, TrialNumber):
    Sequence1.append(math.sin(UniformList[trial2]) * ExpoList[trial2])
    Sequence2.append(math.cos(UniformList[trial2]) * ExpoList[trial2])
    Sequence3.append(math.sqrt(Sequence1[trial2]**2 + Sequence2[trial2]**2))

#Find and print means and variances
mean_1 = numpy.mean(Sequence1)
mean_2 = numpy.mean(Sequence2)
mean_3 = numpy.mean(Sequence3)
variance_1 = numpy.var(Sequence1)
variance_2 = numpy.var(Sequence2)
variance_3 = numpy.var(Sequence3)

print("Sequence 1 Mean: ",mean_1)
print("Sequence 1 Variance: ",variance_1)
print("Sequence 2 Mean: ",mean_2)
print("Sequence 2 Variance: ",variance_2)
print("Sequence 3 Mean: ",mean_3)
print("Sequence 3 Variance: ",variance_3)

#Covariance b/wn Sequence 1 Sequence 2
Sequence12 = []
for item in range(0,TrialNumber):
    Sequence12.append(Sequence1[item]*Sequence2[item])
done = numpy.mean(Sequence12)-(mean_1*mean_2)
print("Sequence 1,2 Covariance: ", done)

# Graph
pylab.figure()
n, bins,patche = pylab.hist(Sequence1, 1000, normed=1, histtype='stepfilled')
pylab.setp(patches, 'facecolor', 'r', 'alpha', 0.75)

pylab.figure()
n, bins,patche = pylab.hist(Sequence1, 1000, normed=1, histtype='stepfilled')
pylab.setp(patches, 'facecolor', 'r', 'alpha', 0.75)

pylab.figure()
n, bins,patche = pylab.hist(Sequence1, 1000, normed=1, histtype='stepfilled')
pylab.setp(patches, 'facecolor', 'r', 'alpha', 0.75)

pylab.show()

'''
* What is the type of random variable `Sequence1`?
    Gaussian Random Variable.
* What is its mean and variance?
    Mean: 0, Variance: 1
* What is the type of random variable `Sequence2`?
    Gaussian Random Variable
* What is its mean and variance?
    Mean: 0, Variance: 1
* What is the type of random variable `Sequence3`?
    Exponential Random Variable
* What is its mean and variance?
    Mean: 2, Variance: 4
* What is the empirical covariance between `Sequence1` and `Sequence2`?
    Covariance: 0

* Do you think they are independent? Justify your answer.
    The covariance is zero where E[XY] = E[X]E[Y], therefore Sequence1
    and Sequence 2 are independent.
'''
