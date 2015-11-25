__NetID__ = "jpdominguez94"
__GitHubID__ = "jpdominguez94"
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

pylab.figure()
n, bins, patches = pylab.hist(Sequence1, 1000, normed=1, histtype='stepfilled')
pylab.setp(patches, 'facecolor', 'k', 'alpha', 0.75)

pylab.figure()
n, bins, patches = pylab.hist(Sequence2, 1000, normed=1, histtype='stepfilled')
pylab.setp(patches, 'facecolor', 'g', 'alpha', 0.75)

pylab.figure()
n, bins, patches = pylab.hist(Sequence3, 1000, normed=1, histtype='stepfilled')
pylab.setp(patches, 'facecolor', 'g', 'alpha', 0.75)

E1 = numpy.mean(Sequence1);
E2 = numpy.mean(Sequence2);
E3 = numpy.mean(Sequence3);

V1 = numpy.var(Sequence1);
V2 = numpy.var(Sequence2);
V3 = numpy.var(Sequence3);


print(str(E1));
print(str(E2));
print(str(E3));
print(str(V1));
print(str(V2));
print(str(V3));


print(numpy.cov(Sequence1,Sequence2))

pylab.show;


"""
What is the type of random variable `Sequence1`?
*It's a Gaussian RV

What is its mean and variance?
*0 and 1 respectively

What is the type of random variable `Sequence2`?
*Gaussian RV

What is its mean and variance?
*0 and 1 respectively

What is the type of random variable `Sequence3`?
*Exponential RV

What is its mean and variance?
*2 and 4 respectively

What is the empirical covariance between `Sequence1` and `Sequence2`?
*roughly 0

Do you think they are independent? Justify your answer.
*Since the covariance is roughly zero, i would think they are independent
 
"""

