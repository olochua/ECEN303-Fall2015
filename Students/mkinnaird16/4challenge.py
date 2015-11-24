__NetID__ = "421008718"
__GitHubID__ = ""
__SelfGrade__ = "4"
__Challenge__ = "4.2"

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

pylab.show()

pylab.figure()
n, bins, patches = pylab.hist(RayleighList, 1000, normed=1, histtype='stepfilled')
pylab.setp(patches, 'facecolor', 'r', 'alpha', 0.75)

pylab.figure()
n, bins, patches = pylab.hist(RayleighList, 1000, normed=1, histtype='stepfilled')
pylab.setp(patches, 'facecolor', 'y', 'alpha', 0.75)

pylab.figure()
n, bins, patches = pylab.hist(RayleighList, 1000, normed=1, histtype='stepfilled')
pylab.setp(patches, 'facecolor', 'b', 'alpha', 0.75)


print("What is the type of random variable `Sequence1`?")
print("continuous")
print("What is its mean and variance?")
print(numpy.mean(Sequence1))
print(numpy.var(Sequence1))
print("What is the type of random variable `Sequence2`?")
print("Continuous")
print("What is its mean and variance?")
print(numpy.mean(Sequence2))
print(numpy.var(Sequence2))
print("What is the type of random variable `Sequence3`?")
print("Continuous")
print("What is its mean and variance?")
print(numpy.mean(Sequence3))
print(numpy.var(Sequence3))
print("What is the empirical covariance between `Sequence1` and `Sequence2`?")
print(numpy.cov(Sequence1,Sequence2))
print("Do you think they are independent? Justify your answer.")
print("Yes. They both dip near zero in the middle.")
