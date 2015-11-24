__NetID__ = "jfernandoromoddl"
__GitHubID__ = "FernandoRomo"
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

# EDIT
#PLOT Sequence 1
pylab.figure()
n, bins, patches = pylab.hist(Sequence1, 1000, normed=1, histtype='stepfilled')
pylab.setp(patches, 'facecolor', 'm', 'alpha', 0.75)
pylab.title('Sequence1')
print("Mean and Variance of Sequence 1")
print(numpy.mean(Sequence1))
print(numpy.var(Sequence1))

#PLOT Sequence 2
pylab.figure()
n, bins, patches = pylab.hist(Sequence2, 1000, normed=1, histtype='stepfilled')
pylab.setp(patches, 'facecolor', 'r', 'alpha', 0.75)
pylab.title('Sequence2')
print("Mean and Variance of Sequence 2")
print(numpy.mean(Sequence2))
print(numpy.var(Sequence2))

#PLOT Sequence 3
pylab.figure()
n, bins, patches = pylab.hist(Sequence3, 1000, normed=1, histtype='stepfilled')
pylab.setp(patches, 'facecolor', 'c', 'alpha', 0.75)
pylab.title('Sequence3')
print("Mean and Variance of Sequence 3")
print(numpy.mean(Sequence3))
print(numpy.var(Sequence3))

#Variance comparison of Sequence 1 and Sequence 2
print ("Covariance of Sequence 1 and Sequence 2")
print (numpy.cov(Sequence1,Sequence2))

pylab.show()

"""
What is the type of random variable `Sequence1`?
>> Continuous Random Variable with Rayleigh Distribution of a Sine.
What is its mean and variance?
>> Mean = 0, Variance = 1.

What is the type of random variable `Sequence2`?
>> Continuous Random Variable with Rayleigh Distribution of a Cosine.
What is its mean and variance?
>> Mean = 0, Variance = 1.

What is the type of random variable `Sequence3`?
>> Continuous Random Variable with a Rayleigh Distribution of a Cosine times a Sine.
What is its mean and variance?
>> Mean = 2, Variance = 4.

What is the empirical covariance between `Sequence1` and `Sequence2`?
>> The Empirical Covariance is close to zero.

Do you think they are independent? Justify your answer.
>> When two random variable distributions are independent, then the covariance will be zero therefore independent.
"""
