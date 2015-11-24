__NetID__ = "alexgarcia2013"
__GitHubID__ = "alexgarcia2013"
__SelfGrade__ = "2"
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

#
# EDIT
#

"""
What is the type of random variable `Sequence1`?
Uniform Distribution Random Variable
What is its mean and variance?
Mean is around 3.4 and Var is
What is the type of random variable `Sequence2`?
Looks like a Rayleigh Distributed Continuous Random Variable
What is its mean and variance?
What is the type of random variable `Sequence3`?
I couldn't get this part to work, but judging that I was supposed to somehow combine a 
continuous uniform distribution and Rayleigh, I would guess that it should be a gaussian distribution.
What is its mean and variance?
What is the empirical covariance between `Sequence1` and `Sequence2`?
Do you think they are independent? Justify your answer.
The sequences appear to be dependent as 1 and 2 don't dependend on one another,
but since the 3rd is a combination of the previous two it must be dependent.
"""

