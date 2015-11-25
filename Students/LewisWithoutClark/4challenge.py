__NetID__ = "justin94lewis"
__GitHubID__ = "LewisWithoutClark"
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

Gaussian Random Variable

What is its mean and variance?

mean: 0    variance: 1

What is the type of random variable `Sequence2`?

Gaussian Random Variable

What is its mean and variance?

mean: 0    variance: 1

What is the type of random variable `Sequence3`?

Exponential Random Variable

What is its mean and variance?

mean: 2    variance: 4

What is the empirical covariance between `Sequence1` and `Sequence2`?

covariance: 0  (6.46376479e-04 for one run, which is roughly zero)

Do you think they are independent? Justify your answer.

by analysis of the covariance, the sequences are likely independent. If two 
sequences are independent, then their covariance is necessarily zero; however,
if the covariance of two random variables is zero, that does NOT necessitate 
that they are independent. They are only independent if they are jointly 
normally distributed. We haven't gone over this yet so I'm guessing they are
actually independent, but one way to know for sure would be to look at
thier joint distribution. 

"""
