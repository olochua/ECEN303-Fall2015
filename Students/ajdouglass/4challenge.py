__author__ = "Andrew Douglass"
__NetID__ = "adoulgas"
__GitHubID__ = "ajdouglass"
__SelfGrade__ = "5pt"
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

UniformList = []     # hold values for the uniform distribution
RayleighList = []    # hold values for the rayleigh distribution
for trial1 in range(0, TrialNumber):     # add 100000 elements to each list
    UniformList.append(random.uniform(0, 2*math.pi))
    RayleighList.append(numpy.random.rayleigh(1))

"""pylab.figure()
n, bins, patches = pylab.hist(UniformList, 1000, normed=1, histtype='stepfilled')
pylab.setp(patches, 'facecolor', 'k', 'alpha', 0.75)

pylab.figure()
n, bins, patches = pylab.hist(RayleighList, 1000, normed=1, histtype='stepfilled')
pylab.setp(patches, 'facecolor', 'g', 'alpha', 0.75)

pylab.show()   """

Sequence1 = []   # hold the values for the first continuous random variable
Sequence2 = []   # hold the values for the second continuous random variable
Sequence3 = []   # hold the values for the third continuous random variable
for trial2 in range(0, TrialNumber):     # add 100000 elements to each list
    Sequence1.append(math.sin(UniformList[trial2]) * RayleighList[trial2])
    Sequence2.append(math.cos(UniformList[trial2]) * RayleighList[trial2])
    Sequence3.append(Sequence1[trial2]**2 + Sequence2[trial2]**2)

mean1 = numpy.mean(Sequence1)   # Calculate the mean of sequence1
mean2 = numpy.mean(Sequence2)   # Calculate the mean of sequence2
mean3 = numpy.mean(Sequence3)   # Calculate the mean of sequence3

var1 = numpy.var(Sequence1)     # Calculate the variance of sequence1
var2 = numpy.var(Sequence2)     # Calculate the variance of sequence2
var3 = numpy.var(Sequence3)     # Calculate the variance of sequence3

# Print mean and variance of sequence 1
print("Mean of Sequence 1: ",mean1)
print("Variance of Sequence 1: ",var1)
# Print mean and variance of sequence 2
print("Mean of Sequence 2: ",mean2)
print("Variance of Sequence 2: ",var2)
# Print mean and variance of sequence 3
print("Mean of Sequence 3: ",mean3)
print("Variance of Sequence 3: ",var3)

# Calculate the covariance between sequence1 and sequence2
total = []    # Hold the value of (Sequence1)(Sequence2)
for item in range(0, TrialNumber):    # iterate across all elements in the sequences
    total.append(Sequence1[item]*Sequence2[item])
end = numpy.mean(total) - (mean1*mean2)     # calculate the covariance
"""
   Sequence1 = X
   Sequence2 = Y
   o(X,Y) = E[XY] - E[X]E[Y]
"""
print("Covariance: ",end)

# Graph of the distribution of Sequence1
pylab.figure()
n, bins, patches = pylab.hist(Sequence1, 1000, normed=1, histtype='stepfilled')
pylab.setp(patches, 'facecolor', 'k', 'alpha', 0.75)

# Graph of the distribution of Sequence2
pylab.figure()
n, bins, patches = pylab.hist(Sequence2, 1000, normed=1, histtype='stepfilled')
pylab.setp(patches, 'facecolor', 'r', 'alpha', 0.75)

# Graph of the distribution of Sequence3
pylab.figure()
n, bins, patches = pylab.hist(Sequence3, 1000, normed=1, histtype='stepfilled')
pylab.setp(patches, 'facecolor', 'b', 'alpha', 0.75)

pylab.show()

"""
What is the type of random variable `Sequence1`?
   It is a continuous random variable with a normal random variable distribution.
   This is also known as the standard Gaussian random variable.
What is its mean and variance?
   Mean: ~0
   Variance: ~1

What is the type of random variable `Sequence2`?
   It is a continuous random variable with a normal random variable distribution.
   This is also known as the standard Gaussian random variable.
What is its mean and variance?
   Mean: ~0
   Variance: ~1

What is the type of random variable `Sequence3`?
   It is a continuous random variable with an exponential random variable distribution.
What is its mean and variance?
   Mean: ~2
   Variance: ~4

What is the empirical covariance between `Sequence1` and `Sequence2`?
   The empirical covariance as calculated in the program is 0.

Do you think they are independent? Justify your answer.
   Because the covariance is zero and with the calculation done above
   where E[XY] = E[X]E[Y], Sequence1 and Sequence2 must independent.

"""

