__NetID__ = "tort115"
__GitHubID__ = "westort"
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
## creating figures for each sequence using same method as above code
##where n = num of counts, bins = left edge, and patches = individual units
pylab.figure()
pylab.title("sequence 1")
n, bins, patches = pylab.hist(Sequence1, 1000, normed=1, histtype='stepfilled')
pylab.setp(patches, 'facecolor', 'b', 'alpha', 1)
pylab.figure("sequence 2")
pylab.title("sequence 2")
n, bins, patches = pylab.hist(Sequence2, 1000, normed=1, histtype='stepfilled')
pylab.setp(patches, 'facecolor', 'b', 'alpha', 1)
pylab.figure("sequence 3")
pylab.title("sequence 3")
n, bins, patches = pylab.hist(Sequence3, 1000, normed=1, histtype='stepfilled')
pylab.setp(patches, 'facecolor', 'b', 'alpha', 1)
pylab.show()
#calculating the means
mean1 = numpy.mean(Sequence1)
mean2 = numpy.mean(Sequence2)
mean3 = numpy.mean(Sequence3)
print "mean 1 = %f " %mean1
print "mean 2 = %f " %mean2
print "mean 3 = %f " %mean3
#calculating the variances
var1 = numpy.var(Sequence1)
var2 = numpy.var(Sequence2)
var3 = numpy.var(Sequence3)
print "var 1 = %f " %var1
print "var 2 = %f " %var2
print "var 3 = %f " %var3

"Calculations to check expectations for independence check"
#sum = 0
#for i in range (0, len(Sequence1)):
#    sum += ((Sequence1[i-1]*(i)))
#expectation1 = sum
#sum = 0
#for i in range (0, len(Sequence1)):
#    sum += ((Sequence2[i-1]*(i)))
#expectation2 = sum
#sum = 0
#for i in range (0, len(Sequence1)):
#    sum += (((Sequence1[i-1]*Sequence1[i-1])*(i)))
#expectation3 = sum
#multExp = expectation1*expectation2
#Expmult = expectation3
#print "multExp = %f" %multExp
#print "Expmult = %f" %Expmult


"computing covariance of Seq1,Seq2"
cov1 = numpy.cov(Sequence1, Sequence2)[0][1]

#alternate method for checking covariance
#sum = 0
#for i in range(0, len(Sequence1)):
#    sum += ((Sequence1[i] - mean1) * (Sequence2[i] - mean2))
#    cov2 = sum/(len(Sequence1)-1)

print "covariace = "
print cov1


"""
What is the type of random variable `Sequence1`?
Sequence 1 is a gaussian random variable

What is its mean and variance?
the mean of sequence 1 approx = 0 with small variation in the thousandths place
the variance of sequence 1 approx = 1 with small variation in the thousandths place

What is the type of random variable `Sequence2`?
Sequence 2 is a gaussian random variable

What is its mean and variance?
the mean of sequence 2 approx = 0 with small variation in the thousandths place
the variance of sequence 2 approx = 1 with small variation in the thousandths place

What is the type of random variable `Sequence3`?
Sequence 3 is an exponential random variable

What is its mean and variance?
the mean of sequence 3 approx = 2 with small variation in the thousandths place
the variance of sequence 3 approx = 4 with small variation in the hundredths place

What is the empirical covariance between `Sequence1` and `Sequence2`?
The empirical covariance of sequence1 and sequence2 is close to 0

Do you think they are independent? Justify your answer.
Yes, I think they are independent, for two random variables to be independent they must 
have covariance of 0, but that does not quite prove independence, so the commented 
out calculations show that E[X*Y] = E[X] * E[Y], which proves independence

"""

