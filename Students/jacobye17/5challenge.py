__NetID__ = "jacobye17"
__GitHubID__ = "jacobye17"
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

print numpy.mean(GaussianList)
print numpy.var(GaussianList)

print numpy.mean(BernoulliList)
print numpy.var(BernoulliList)

print numpy.mean(ExpovariateList)
print numpy.var(ExpovariateList)

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
What is the type of random variable `GaussianList`? Gaussian RV
What is its mean and variance? Mean = 0.000534112130383     Variance = 0.000991433113328

What is the type of random variable `BernoulliList`? Bernoulli RV
What is its mean and variance? Mean = 0.5002133         Variance = 0.00025491580311

What is the type of random variable `ExpovariateList`? Poisson RV
What is its mean and variance? Mean = 0.999780887256    Variance = 0.00100225112311

What is going on with `ParetoList`? A Pareto distribution is skewed to the right. It is defined by two variables, xm,
the lowest value the RV can take and alpha, which is the degree of concentration of the distribution. The smaller alpha
the heavier the tail of distribution
"""

