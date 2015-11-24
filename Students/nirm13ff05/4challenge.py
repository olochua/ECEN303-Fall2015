__NetID__ = "nirm13ff05"
__GitHubID__ = "nirm13ff05"
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

#Sequence 1 Plot
pylab.figure()
n, bins, patches = pylab.hist(Sequence1, 1000, normed=1, histtype='stepfilled')
pylab.setp(patches, 'facecolor', 'y', 'alpha', 0.75)
pylab.title('Sequence 1')

#Sequence 2 Plot
pylab.figure()
n, bins, patches = pylab.hist(Sequence2, 1000, normed=1, histtype='stepfilled')
pylab.setp(patches, 'facecolor', 'r', 'alpha', 0.75)
pylab.title('Sequence 2')

#Sequence 3 Plot
pylab.figure()
n, bins, patches = pylab.hist(Sequence3, 1000, normed=1, histtype='stepfilled')
pylab.setp(patches, 'facecolor', 'c', 'alpha', 0.75)
pylab.title('Sequence 3')

pylab.show()

print("Mean and Variance of Sequence 1")  #edited print statements to work with updated version of python
print(numpy.mean(Sequence1))
print(numpy.var(Sequence1))

print("  ")

print("Mean and Variance of Sequence 2")
print(numpy.mean(Sequence2))
print(numpy.var(Sequence2))

print("  ")

print("Mean and Variance of Sequence 3")
print(numpy.mean(Sequence3))
print(numpy.var(Sequence3))

print("  ")

print ("Covariance of Sequence 1 and Sequence 2")
print (numpy.cov(Sequence1,Sequence2))
"""
What is the type of random variable `Sequence1`?
    Continuous random variable. 
What is its mean and variance?
    Mean = -0.000623      Variance = 1.0041
What is the type of random variable `Sequence2`?
    Continuous random variable. 
What is its mean and variance?
    Mean = 5.1e-06      Variance = 0.997
What is the type of random variable `Sequence3`?
    Continuous random variable.
What is its mean and variance?
    Mean = 2.008        Variance = 3.999
What is the empirical covariance between `Sequence1` and `Sequence2`?
    Very close to 0. 
Do you think they are independent? Justify your answer.
    They must have a covariance equal to 0 to be independent, which they happen to have. Thuse they seem to independent. 
"""

