__NetID__ = "bnn292 "
__GitHubID__ = "bnn292"
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
pylab.title('Uniform List')

pylab.figure()
n, bins, patches = pylab.hist(RayleighList, 1000, normed=1, histtype='stepfilled')
pylab.setp(patches, 'facecolor', 'g', 'alpha', 0.75)
pylab.title('Rayleigh List')

Sequence1 = []
Sequence2 = []
Sequence3 = []
for trial2 in range(0, TrialNumber):
    Sequence1.append(math.sin(UniformList[trial2]) * RayleighList[trial2])
    Sequence2.append(math.cos(UniformList[trial2]) * RayleighList[trial2])
    Sequence3.append(Sequence1[trial2]**2 + Sequence2[trial2]**2)

#Sequence 1
pylab.figure()
n, bins, patches = pylab.hist(Sequence1, 1000, normed=1, histtype='stepfilled')
pylab.setp(patches, 'facecolor', 'r', 'alpha', 0.75)
pylab.title('Sequence 1')

#Sequence 2
pylab.figure()
n, bins, patches = pylab.hist(Sequence2, 1000, normed=1, histtype='stepfilled')
pylab.setp(patches, 'facecolor', 'g', 'alpha', 0.75)
pylab.title('Sequence 2')

#Sequence 3
pylab.figure()
n, bins, patches = pylab.hist(Sequence3, 1000, normed=1, histtype='stepfilled')
pylab.setp(patches, 'facecolor', 'b', 'alpha', 0.75)
pylab.title('Sequence 3')

pylab.show()

print("Values for Mean and Var, Sequence 1") #fixed for Python 3.4
print(numpy.mean(Sequence1))
print(numpy.var(Sequence1))
print("  ")
print("Values for Mean and Var, Sequence 2")
print(numpy.mean(Sequence2))
print(numpy.var(Sequence2))
print("  ")
print("Values for Mean and Var, Sequence 3")
print(numpy.mean(Sequence3))
print(numpy.var(Sequence3))
print("  ")
print ("Covariance for Sequence 1 and Sequence 2")
print (numpy.cov(Sequence1,Sequence2))

"""
What is the type of random variable `Sequence1`?
    Continuous
What is its mean and variance?
    Mean = ~0, Var = ~1
What is the type of random variable `Sequence2`?
    Continuous
What is its mean and variance?
    Mean = ~0, Var = ~1
What is the type of random variable `Sequence3`?
   Continuous
What is its mean and variance?
    Mean = ~2, Var = ~4
What is the empirical covariance between `Sequence1` and `Sequence2`?
    ~0
Do you think they are independent? Justify your answer.
    Yes, covariance equals zero.
"""
