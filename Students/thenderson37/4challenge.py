__NetID__ = "tyler.henderson07"
__GitHubID__ = "thenderson37"
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

#Sequence 1 plot
pylab.figure()
n, bins, patches = pylab.hist(Sequence1, 1000, normed=1, histtype='stepfilled')
pylab.setp(patches, 'facecolor', 'm', 'alpha', 0.75)
pylab.title('Sequence1')

#Sequence1
print("Sequence 1")
print("Mean= "); print(numpy.mean(Sequence1))
print ("Variance= "); print(numpy.var(Sequence1))
print("")

pylab.figure()
n, bins, patches = pylab.hist(Sequence2, 1000, normed=1, histtype='stepfilled')
pylab.setp(patches, 'facecolor', 'r', 'alpha', 0.75)
pylab.title('Sequence2')

#Sequence2
print("Sequence 2")
print("Mean= "); print(numpy.mean(Sequence2))
print ("Variance= "); print(numpy.var(Sequence2))
print("")

pylab.figure()
n, bins, patches = pylab.hist(Sequence3, 1000, normed=1, histtype='stepfilled')
pylab.setp(patches, 'facecolor', 'c', 'alpha', 0.75)
pylab.title('Sequence3')

#Sequence3
print("Sequence 3")
print("Mean= "); print(numpy.mean(Sequence3))
print ("Variance= "); print(numpy.var(Sequence3))
print("")

print ("Covariance of Sequence 1 and Sequence 2")
print (numpy.cov(Sequence1,Sequence2))

pylab.show()

"""
What is the type of random variable `Sequence1`?
Continuous random variable with a rayleigh distribution dependent on the sine function.

What is its mean and variance?
Mean = 0 Variance = 1

What is the type of random variable `Sequence2`?
Continuous random variable with a rayleigh distribution dependent on the cosine function.

What is its mean and variance?
Mean = 0 Variance = 1

What is the type of random variable `Sequence3`?
Continuous random variable of a uniform distribution.

What is its mean and variance?
Mean = 2 Variance = 4

What is the empirical covariance between `Sequence1` and `Sequence2`?
Covariance is 0

Do you think they are independent? Justify your answer.
Yes because the covariance is  0
"""
