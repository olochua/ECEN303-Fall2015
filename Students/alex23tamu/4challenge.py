__NetID__ = "alex23"
__GitHubID__ = "alex23tamu"
__SelfGrade__ = "3"
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

# Sequence 1
pylab.figure()

n, bins, patches = pylab.hist(Seq1, 1000, normed=1, histtype='stepfilled')
pylab.setp(patches, 'facecolor', 'm', 'alpha', 0.75)
pylab.title('Seq1')
print("Mean and Variance Sequence 1")
print(numpy.mean(Seq1))
print(numpy.var(Seq1))

# Sequence 2
pylab.figure()

n, bins, patches = pylab.hist(Seq2, 1000, normed=1, histtype='stepfilled')
pylab.setp(patches, 'facecolor', 'r', 'alpha', 0.75)
pylab.title('Seq2')
print("Mean and Variance Sequence 2")
print(numpy.mean(Seq2))
print(numpy.var(Seq2))

# Sequence 3
pylab.figure()

n, bins, patches = pylab.hist(Seq3, 1000, normed=1, histtype='stepfilled')
pylab.setp(patches, 'facecolor', 'c', 'alpha', 0.75)
pylab.title('Seq3')
print("Mean and Variance Sequence 3")
print(numpy.mean(Seq3))
print(numpy.var(Seq3))

#Variance Comparator

print ("Covariance of Sequences 1 and 2)
print (numpy.cov(Seq1,Seq2))



pylab.show()

"""
What is the type of random variable `Sequence1`?
Continuous random variable with Rayleigh distribution of a sine.

What is its mean and variance? Mean = 0, Var = 1

What is the type of random variable `Sequence2`?
Continuous random variable with Rayleigh distribution of a cosine.

What is its mean and variance? Mean = 0, Var = 1

What is the type of random variable `Sequence3`?
Continuous random variable with Rayleigh distribution of a sine times cosine

What is its mean and variance? Mean = 2, Var = 4

What is the empirical covariance between `Sequence1` and `Sequence2`?
Close to 0
Do you think they are independent? Justify your answer.
If the convariance is close to 0, then it it independent
"""


