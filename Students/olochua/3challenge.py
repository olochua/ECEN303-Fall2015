__author__ = "Jui Yen Chua"  
__NetID__ = "olochua" 
__GitHubID__ = "olochua" 
__SelfGrade__ = "5"  
__Challenge__ = "3"

"""
Random Signals and Systems
Course: ECEN 303-502
Maximum Grade: 5
"""


import random
import math
import matplotlib.pyplot as plt


def biasedcoinflip(p=0.5):
    """
    This method returns a one with probability p and it returns a zero with
    probability (1 - p). The default parameter is p=0.5; this can be changed
    by passing an argument to the method.
    """
    return math.floor(random.random() + p)


def binomialflips(n=1, p=0.5):
    """
    This method returns a binomial random variable with parameters n and p.
    The default parameters are n=1 and p=0.5; this can be changed by passing
    arguments to the method.
    """
    numberones = 0
    for BinomialIndex in range(0,n):
        numberones += biasedcoinflip(p)
    return numberones


def poisson(parameterpoisson=10):
    
	rand_num = random.random() #this is the random value for while loop exit condition
	k = 0 #k in poisson random variable
	sum = 0 #sum of the poisson random variable
	
	while sum < rand_num: #compute poisson random variable with lambda = parameterpoisson
		sum += (pow(parameterpoisson, k)/math.factorial(k))*math.exp(-parameterpoisson)
		rand_num = random.random()
		k += 1 #increment k 
		
	return k-1 #return the last k that makes the sum match with the condition
	


def experiment3(parameterpoisson3=10, p=0.5):
    return binomialflips(poisson(parameterpoisson3), p)
    # return poisson(binomialflips(parameterpoisson3, p))


ParameterPoisson = 10
NumberTrials = 100000
TrialSequence = []

for TrialIndex1 in range(0, NumberTrials):
    TrialSequence.append(experiment3(ParameterPoisson))
print sum(TrialSequence)/len(TrialSequence)

Distribution = []
for OutcomeIndex1 in range(0, 21):
    Distribution.append(TrialSequence.count(OutcomeIndex1) / (1.0 * NumberTrials))

OutcomeIndex2 = range(0, 21)
num_bins = len(OutcomeIndex2)
bar_width = 0.8
XticksIndex = [(outcome + (0.5 * bar_width)) for outcome in OutcomeIndex2]
opacity = 0.4

plt.bar(OutcomeIndex2, Distribution, bar_width, alpha=opacity, color='b')
plt.xlabel("Value")
plt.ylabel("Probability")
plt.xticks(XticksIndex, OutcomeIndex2)
plt.show()

# Question 1: What is the mean of experiment3()?
# Answer 1: The mean of experiment3() is about 3.98.

# Question 2: What is the type of experiment3()?
# Answer 2: Based on the bar graph generated, experiment3() is of type Poisson.

# Question 3: Do the two distributions match?
# Answer 3: The general pattern and scaling of each bar in the graph is very similar to one another, however, the distributions are not identical.
