__NetID__ = "kevintbradshaw"
__GitHubID__ = "kevintbradshaw"
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

"EDIT:"
"============================================================================================="
pylab.figure()
n, bins, patches = pylab.hist(Sequence1, 1000, normed=1, histtype='stepfilled')
pylab.setp(patches, 'facecolor', 'y', 'alpha', 0.75)
pylab.title('Sequence 1')
print("Sequence 1: Mean")  
print(numpy.mean(Sequence1))
print("Sequence 1: Variance") 
print(numpy.var(Sequence1))
"============================================================================================="
pylab.figure()
n, bins, patches = pylab.hist(Sequence2, 1000, normed=1, histtype='stepfilled')
pylab.setp(patches, 'facecolor', 'r', 'alpha', 0.75)
pylab.title('Sequence 2')
print("Sequence 2: Mean")  
print(numpy.mean(Sequence2))
print("Sequence 2: Variance")  
print(numpy.var(Sequence2))
"============================================================================================="
pylab.figure()
n, bins, patches = pylab.hist(Sequence3, 1000, normed=1, histtype='stepfilled')
pylab.setp(patches, 'facecolor', 'c', 'alpha', 0.75)
pylab.title('Sequence 3')
print("Sequence 3: Mean")  
print(numpy.mean(Sequence3))
print("Sequence 3: Variance")  
print(numpy.var(Sequence3))
"============================================================================================="
print ("Covariance of Sequence 1 and Sequence 2")
print (numpy.cov(Sequence1,Sequence2))
"============================================================================================="
pylab.show()

"""
What is the type of random variable `Sequence1`?
It's a continuous random variable with a rayleigh distribution dependent on a sinusoidal function.

What is its mean and variance?
The mean is 0 and the variance is 1.

What is the type of random variable `Sequence2`?
It's a continuous random variable with a rayleigh distribution dependent on a cosinusoidal function.

What is its mean and variance?
The mean is 0 and the variance is 1.

What is the type of random variable `Sequence3`?
It's a continuous random variable with a rayleigh distribution dependent on a multiplied sinusoidal and cosinusoidal function.

What is its mean and variance?
The mean is 2 and the variance is 4.

What is the empirical covariance between `Sequence1` and `Sequence2`?
The emperical covariance is 0.

Do you think they are independent? Justify your answer.
Yes because the covariance is zero and this is only true when two random variables distributions are independent. 
"""

