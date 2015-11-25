__NetID__ = "Steph1995"
__GitHubID__ = "stephaniedemco"
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

pylab.figure()
n , bins , patches = pylab.hist(Sequence1 , 1000 , normed=1 , histtype='stepfilled')
pylab.setp(patches , 'facecolor' , 'b' , 'alpha' , 0.75)
print(numpy.mean( Sequence1 ) )
print(numpy.var( Sequence1 ) )

pylab.figure()
n , bins , patches = pylab.hist(Sequence1 , 1000 , normed=1 , histtype='stepfilled')
pylab.setp(patches , 'facecolor' , 'b' , 'alpha' , 0.75)
print(numpy.mean( Sequence2 ) )
print(numpy.var( Sequence2 ) )

pylab.figure()
n , bins , patches = pylab.hist(Sequence1 , 1000 , normed=1 , histtype='stepfilled')
pylab.setp(patches , 'facecolor' , 'b' , 'alpha' , 0.75)
print(numpy.mean( Sequence3 ) )
print(numpy.var( Sequence3 ) )

print( numpy.cov( Sequence1 , Sequence2 ) )

pylab.show()


"""
What is the type of random variable `Sequence1`?
continuous random variable
What is its mean and variance?
mean is very small, close to 0
var is 1
What is the type of random variable `Sequence2`?
continuous random variable
What is its mean and variance?
mean is 0
var is 1
What is the type of random variable `Sequence3`?
continuous random variable
What is its mean and variance?
mean is 2
var is 4
What is the empirical covariance between `Sequence1` and `Sequence2`?
covariance is close to 0
Do you think they are independent? Justify your answer.
yes, they are independant because the covariance is almost 0
"""

