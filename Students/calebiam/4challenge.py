__NetID__ = "calebiam "
__GitHubID__ = "calebiam"
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
    Sequence 1 is a continuous random variable. It has a rayleigh distribution dependent on the sine function.

What is its mean and variance?
    The mean of Sequence 1 is very close to zero (-0.00062) and the variance is close to 1 (1.0040).

What is the type of random variable `Sequence2`?
    Sequence 2 is a continuous random variable. It has a rayleigh distribution dependent on the cosine function.

What is its mean and variance?
    The mean of Sequence 2 is about 0 (5.1033e-06) and the variance is close to 1 (0.99708).

What is the type of random variable `Sequence3`?
    Sequence 3 is a continuous random variable. It has a rayleigh distribution dependent on the cosine and sine functions.
    The rayleigh distribution dependent on a sine function is multiplied by another rayleigh distribution dependent on the
    cosine function leaving a uniform distribution.

What is its mean and variance?
    The mean of Sequence 3 is about 2 (2.0084) and the variance is close to 4 (3.99954).

What is the empirical covariance between `Sequence1` and `Sequence2`?
    The empirical covariance between Sequence 1 and 2 is very close to zero.

Do you think they are independent? Justify your answer.
    To be independent the two variable would need to have the covariance equal to zero. This is the case between
    Sequence 1 and Sequence 2, they do not affect each other. So yes, I think that Sequence 1 and 2 are independent.
"""

