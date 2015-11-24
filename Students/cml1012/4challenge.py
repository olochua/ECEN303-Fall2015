__NetID__ = " cml1012 "
__GitHubID__ = " cml1012 "
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

pylab.figure()
n, bins, patches = pylab.hist(Sequence1, 1000, normed = 1, histtype ='stepfilled')
pylab.setup(patches, 'facecolor', 'y', 'alpha', .75)
pylab.title('Sequence 1')

pylab.figure()
n, bins, patches = pylab.hist(Sequence2, 1000, normed = 1, histtype ='stepfilled')
pylab.setup(patches, 'facecolor', 'r', 'alpha', .75)
pylab.title('Sequence 2')

pylab.figure()
n, bins, patches = pylab.hist(Sequence3, 1000, normed = 1, histtype ='stepfilled')
pylab.setup(patches, 'facecolor', 'c', 'alpha', .75)
pylab.title('Sequence 3')

pylab.show()

print("Mean and Variance Sequence 1")
print(numpy.mean(Sequence1))
print(numpy.var(Sequence1))

print(" ")

print("Mean and Variance Sequence 2")
print(numpy.mean(Sequence2))
print(numpy.var(Sequence2))

print(" ")

print("Mean and Variance Sequence 3")
print(numpy.mean(Sequence3))
print(numpy.var(Sequence3))

print(" ")

print("Convariance of Sequence 1 & Sequence 2")
print(numpy.covar(Sequence1, Sequence2))

"""
What is the type of random variable `Sequence1`?
    Continous Random Variable.

What is its mean and variance?
    The mean is about .00062, and the variance is about 1.0040.
    
What is the type of random variable `Sequence2`?
    Continous Random Variable
    
What is its mean and variance?
    The mean is .000005103, and the variance is .99708.
    
What is the type of random variable `Sequence3`?
    Continous Random Variable
    
What is its mean and variance?
    The mean is 2.0084, and the variance is 3.99945
    
What is the empirical covariance between `Sequence1` and `Sequence2`?
    The empirical covariance between the 2 are close to 0.
Do you think they are independent? Justify your answer.
    Yes, because the covariance of sequence 1 and sequence 2 are about 0; therefore, making them independent of each other.
"""

