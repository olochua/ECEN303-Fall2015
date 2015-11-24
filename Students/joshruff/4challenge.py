__NetID__ = ""
__GitHubID__ = ""
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

print(numpy.cov(Sequence1,Sequence2))


pylab.show()

#
# EDIT
#

"""
What is the type of random variable `Sequence1`? 
	-Gaussian
What is its mean and variance?	
	-Mean is 0
	-Variance is 1


What is the type of random variable `Sequence2`? 
	-Gaussian
What is its mean and variance?	
	-Mean is 0
	-Variance is 1


What is the type of random variable `Sequence3`? 
	-Exponential
What is its mean and variance?	
	-Lambda is 0.5 
	-Mean is 1/Lambda = 2
	Variance is 1/Lambda^2 = 4


What is the empirical covariance between `Sequence1` and `Sequence2`? 0
Do you think they are independent? Justify your answer. Yes. The sum of the expectation of sequence 1 and sequence 2 equals the expectation of the sums. 
"""

