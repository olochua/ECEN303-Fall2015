__NetID__ = "gardegi059"
__GitHubID__ = "ggardea66"
__SelfGrade__ = "4"
__Challenge__ = "4"

"""
Random Signals and Systems
Course: ECEN 303-502
Maximum Grade: 5pt
"""

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

pylab.title('Rayleigh List')

Sequence1 = []
Sequence2 = []
Sequence3 = []
for trial2 in range(0, TrialNumber):
    Sequence1.append(math.sin(UniformList[trial2]) * RayleighList[trial2])
    Sequence2.append(math.cos(UniformList[trial2]) * RayleighList[trial2])
    Sequence3.append(Sequence1[trial2]**2 + Sequence2[trial2]**2)


pylab.figure()
n, bins, patches = pylab.hist(Sequence1, 1000, normed=1, histtype='stepfilled')
pylab.setp(patches, 'facecolor', 'y', 'alpha', 0.75)
pylab.title('Sequence 1')

pylab.figure()
n, bins, patches = pylab.hist(Sequence2, 1000, normed=1, histtype='stepfilled')
pylab.setp(patches, 'facecolor', 'r', 'alpha', 0.75)
pylab.title('Sequence 2')

pylab.figure()
n, bins, patches = pylab.hist(Sequence3, 1000, normed=1, histtype='stepfilled')
pylab.setp(patches, 'facecolor', 'c', 'alpha', 0.75)
pylab.title('Sequence 3')

pylab.show()


print("Mean and Variance of Sequence 1")
print(numpy.mean(Sequence1))
print(numpy.var(Sequence1))

print("Mean and Variance of Sequence 2")
print(numpy.mean(Sequence2))
print(numpy.var(Sequence2))

print("Mean and Variance of Sequence 3")
print(numpy.mean(Sequence3))
print(numpy.var(Sequence3))

print ("Covariance of Sequence 1 and Sequence 2")
print (numpy.cov(Sequence1,Sequence2))

"""
What is the type of random variable `Sequence1`?
This is a continuous random variable with a Rayleigh distribution.
What is its mean and variance?
The mean is about -.0006 and the variance is about 1.005.
What is the type of random variable `Sequence2`?
This is a continuous random variable with Rayleight distribution.
What is its mean and variance?
The mean is about 5.11*10^-6 and the varience is about .997
What is the type of random variable `Sequence3`?
This is a continuous random variable with a Rayleigh distribution.
What is its mean and variance?
The mean is about 2.008 and the varience is about 4.
What is the empirical covariance between `Sequence1` and `Sequence2`?
It is around 1
Do you think they are independent? Justify your answer.
Sequence 1 and sequence 2 are independent because both of the results are close to 
"""

