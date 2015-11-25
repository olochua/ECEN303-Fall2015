__NetID__ = "lgn_barnard"
__GitHubID__ = "lgnbarnard"
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


Sequence1 = []
Sequence2 = []
Sequence3 = []
for trial2 in range(0, TrialNumber):
    Sequence1.append(math.sin(UniformList[trial2]) * RayleighList[trial2])
    Sequence2.append(math.cos(UniformList[trial2]) * RayleighList[trial2])
    Sequence3.append(Sequence1[trial2]**2 + Sequence2[trial2]**2)



#Sequence 1
pylab.figure()
n, bins, patches = pylab.hist(Sequence1, 1000, normed=1, histtype='stepfilled')
pylab.setp(patches, 'facecolor', 'm', 'alpha', 0.75)
pylab.title('Sequence 1')

#S1 Mean and Var
E1 = numpy.mean(Sequence1);
V1 = numpy.var(Sequence1);



#Sequence 2
pylab.figure()
n, bins, patches = pylab.hist(Sequence2, 1000, normed=1, histtype='stepfilled')
pylab.setp(patches, 'facecolor', 'r', 'alpha', 0.75)
pylab.title('Sequence 2')

#S2 Mean and Var
E2 = numpy.mean(Sequence2);
V2 = numpy.var(Sequence2);



#Sequence 3
pylab.figure()
n, bins, patches = pylab.hist(Sequence3, 1000, normed=1, histtype='stepfilled')
pylab.setp(patches, 'facecolor', 'c', 'alpha', 0.75)
pylab.title('Sequence 3')

#S3 Mean and Var
E3 = numpy.mean(Sequence3);
V3 = numpy.var(Sequence3);



#Print
print(str(E1));
print(str(V1));
print(str(E2));
print(str(V2));
print(str(E3));
print(str(V3));

print(numpy.cov(Sequence1,Sequence2))

pylab.show()

"""
What is the type of random variable `Sequence1`?
Gaussian Random Variable

What is its mean and variance?
mean is about 0 and variance is about 1

What is the type of random variable `Sequence2`?
Gaussian Random Variable

What is its mean and variance?
mean is about 0 and variance is about 1

What is the type of random variable `Sequence3`?
Exponential Random Variable

What is its mean and variance?
mean is about 2 variance is about 4

What is the empirical covariance between `Sequence1` and `Sequence2`?
close to 0

Do you think they are independent? Justify your answer.
With the covariance close to 0 I am able to infer that they are independent
"""
