__NetID__ = "dgf378"
__GitHubID__ = "dfawcett"
__SelfGrade__ = "5"
__Challenge__ = "5"

"""
Random Signals and Systems
Course: ECEN 303-502
Maximum Grade: 5pt
"""

import random
import math
import numpy
import pylab

TrialNumber = 10000
SampleNumber = 1000

GaussianList = []
BernoulliList = []
ExpovariateList = []
ParetoList = []

for trial1 in range(0, TrialNumber):
    RunGaussian = 0.0
    RunBernoulli = 0.0
    RunExpovariate = 0.0
    RunParetoList = 0.0
    for sampl1 in range(0, SampleNumber):
        RunGaussian += random.gauss(0, 1)
        RunBernoulli += random.getrandbits(1)
        RunExpovariate += random.expovariate(1)
        RunParetoList += random.paretovariate(1.5)
    GaussianList.append(RunGaussian/(1.0*SampleNumber))
    BernoulliList.append(RunBernoulli/(1.0*SampleNumber))
    ExpovariateList.append(RunExpovariate/(1.0*SampleNumber))
    ParetoList.append(RunParetoList/(1.0*SampleNumber))

pylab.figure()
n, bins, patches = pylab.hist(GaussianList, 1000, normed=1, histtype='stepfilled')
pylab.setp(patches, 'facecolor', 'k', 'alpha', 0.75)

pylab.figure()
n, bins, patches = pylab.hist(BernoulliList, 1000, normed=1, histtype='stepfilled')
pylab.setp(patches, 'facecolor', 'b', 'alpha', 0.75)

pylab.figure()
n, bins, patches = pylab.hist(ExpovariateList, 1000, normed=1, histtype='stepfilled')
pylab.setp(patches, 'facecolor', 'r', 'alpha', 0.75)

pylab.figure()
n, bins, patches = pylab.hist(ParetoList, 1000, normed=1, histtype='stepfilled')
pylab.setp(patches, 'facecolor', 'c', 'alpha', 0.75)

pylab.show()

"""
What is the type of random variable `GaussianList`?
A Gaussian Random Variable
What is its mean and variance?
Its mean is zero and its variance is one

What is the type of random variable `BernoulliList`?
A Bernoulli Random Variable
What is its mean and variance?
The mean is .5 and the variance is .25

What is the type of random variable `ExpovariateList`?
An exponential random variable
What is its mean and variance?
Its mean is one and its variance is one

What is going on with `ParetoList`?
The ParetoList is a Pareto Random variable. Its graph takes on a Pareto
distribution with alpha = 1.5 and Xm = 1. 
"""
