__NetID__ = "augustus1994"
__GitHubID__ = "augustus1994"
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

# Sequence 1 mean and variance
print("Mean and Variance of Sequence 1")
print(numpy.mean(Sequence1))
print(numpy.var(Sequence1))

#Sequence 2 plot
pylab.figure()
n, bins, patches = pylab.hist(Sequence2, 1000, normed=1, histtype='stepfilled')
pylab.setp(patches, 'facecolor', 'r', 'alpha', 0.75)
pylab.title('Sequence2')

# Sequence 2 mean and variance
print("Mean and Variance of Sequence 2")
print(numpy.mean(Sequence2))
print(numpy.var(Sequence2))

#Sequence 3 plot
pylab.figure()
n, bins, patches = pylab.hist(Sequence3, 1000, normed=1, histtype='stepfilled')
pylab.setp(patches, 'facecolor', 'c', 'alpha', 0.75)
pylab.title('Sequence3')

# Sequence 3 mean and variance
print("Mean and Variance of Sequence 3")
print(numpy.mean(Sequence3))
print(numpy.var(Sequence3))

# compare covariance between Sequence 1 and Sequence 2
print ("Covariance of Sequence 1 and Sequence 2")
print (numpy.cov(Sequence1,Sequence2))

pylab.show()

"""
What is the type of random variable `Sequence1`?
Sequence 1 is a continuous random variable with a rayleigh distribution dependent on the sine function.

What is its mean and variance?
The mean is almost zero and the variance is 1

What is the type of random variable `Sequence2`?
Sequence 2 is a continuous random variable with a rayleigh distribution dependent on the cosine function.

What is its mean and variance?
The mean is almost zero and the mean is 1

What is the type of random variable `Sequence3`?
Sequence 3 is a continuous random variable with a rayleigh distribution dependent on the sine function multiplied
another rayleigh distribution dependent on cosine leaving a uniform distribution.

What is its mean and variance?
The mean is 2 and the variance is 4.

What is the empirical covariance between `Sequence1` and `Sequence2`?
The empirical covariance between Sequence 1 and Sequence 2 is almost zero.

Do you think they are independent? Justify your answer.
If two variable are independent then the covariance would be zero such as in Sequence 1 and 2.
They don't effect one another.
"""

