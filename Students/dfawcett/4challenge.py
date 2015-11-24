__NetID__ = "dgf378"
__GitHubID__ = "dfawcett"
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
n, bins, patches = pylab.hist(UniformList, TrialNumber, normed=1, histtype='stepfilled')
pylab.setp(patches, 'facecolor', 'k', 'alpha', 0.75)

uniformmean = sum(UniformList)/len(UniformList)
print("The mean of UniformList is: " + repr(uniformmean))

pylab.figure()
n, bins, patches = pylab.hist(RayleighList, TrialNumber, normed=1, histtype='stepfilled')
pylab.setp(patches, 'facecolor', 'g', 'alpha', 0.75)

rayleighmean = sum(RayleighList)/len(RayleighList)
print("The mean of RayleighList is: " + repr(rayleighmean))

# pylab.show()

Sequence1 = []
Sequence2 = []
Sequence3 = []
sinUniform = []
cosUniform = []
for trial2 in range(0, TrialNumber):
    sinUniform.append(math.sin(UniformList[trial2]))
    cosUniform.append(math.cos(UniformList[trial2]))
    Sequence1.append(math.sin(UniformList[trial2]) * RayleighList[trial2])
    Sequence2.append(math.cos(UniformList[trial2]) * RayleighList[trial2])
    Sequence3.append(Sequence1[trial2]**2 + Sequence2[trial2]**2)

pylab.figure()
n, bins, patches = pylab.hist(Sequence1, TrialNumber, normed=1, histtype='stepfilled')
pylab.setp(patches, 'facecolor', 'g', 'alpha', 0.75)

pylab.figure()
n, bins, patches = pylab.hist(Sequence2, TrialNumber, normed=1, histtype='stepfilled')
pylab.setp(patches, 'facecolor', 'g', 'alpha', 0.75)

pylab.figure()
n, bins, patches = pylab.hist(Sequence3, TrialNumber, normed=1, histtype='stepfilled')
pylab.setp(patches, 'facecolor', 'g', 'alpha', 0.75)

sinuniformmean = sum(sinUniform)/len(sinUniform)
print("The mean of sinUniform is: " + repr(sinuniformmean))

cosuniformmean = sum(cosUniform)/len(cosUniform)
print("The mean of cosUniform is: " + repr(cosuniformmean) + '\n')


mean1 = sum(Sequence1)/len(Sequence1)

secondmoment1 = 0
for index in range(0, TrialNumber):
    secondmoment1 = secondmoment1 + Sequence1[index]**2
secondmoment1 = secondmoment1/len(Sequence1)

variance1 = secondmoment1 - mean1**2


mean2 = sum(Sequence2)/len(Sequence2)

secondmoment2 = 0
for index in range(0, TrialNumber):
    secondmoment2 = secondmoment2 + Sequence2[index]**2
secondmoment2 = secondmoment2/len(Sequence1)

variance2 = secondmoment2 - mean2**2

mean3 = sum(Sequence3)/len(Sequence3)

secondmoment3 = 0
for index in range(0, TrialNumber):
    secondmoment3 = secondmoment3 + Sequence3[index]**2
secondmoment3 = secondmoment3/len(Sequence1)

variance3 = secondmoment3 - mean3**2


print("The mean of Sequence1 is: " + repr(mean1))
print("The secondmoment of Sequence1 is: " + repr(secondmoment1))
print("The variance of Sequence1 is: " + repr(variance1) +'\n')

print("The mean of Sequence2 is: " + repr(mean2))
print("The secondmoment of Sequence2 is: " + repr(secondmoment2))
print("The variance of Sequence2 is: " + repr(variance2) +'\n')

print("The mean of Sequence3 is: " + repr(mean3))
print("The variance of Sequence3 is: " + repr(variance3) +'\n')

list = []
for index in range(0, TrialNumber):
    list.append(Sequence1[index] * Sequence2[index])

listmean = sum(list)/len(list)

covariance = listmean - mean1*mean2

print("The covariance of Sequence1 and Sequence2 is: " + repr(covariance) +'\n')

pylab.show()

"""
What is the type of random variable `Sequence1`?
Gaussian Distribution

What is its mean and variance?
Its mean is 0
Its variance is 1

What is the type of random variable `Sequence2`?
Gaussian Distribution

What is its mean and variance?
Its mean is 0
Its variance is 1

What is the type of random variable `Sequence3`?
Exponential Distribution

What is its mean and variance?
Its mean is 2
Its variance is 4

What is the empirical covariance between `Sequence1` and `Sequence2`?
Very close to zero. Usually around 1/1000

Do you think they are independent? Justify your answer.
Yes. The empirical expectation of the sum of Sequence1^2 + Sequence2^2 is the sum of the expectations of Sequence1^2
and Sequence2^2 which is true if they are independent. The covaraince is also close to zero
which is true if they are independent
