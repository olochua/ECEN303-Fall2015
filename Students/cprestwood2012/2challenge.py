__author__ = "Colbie Prestwood"
__NetID__ = "cprestwood2012"
__GitHubID__ = "cprestwood2012"
__challenge__ = "2"
__version__ = "4.5"
__grader__ = ""
__SelfGrade__ = "4"
__PeerGrade__ = ""

"""
Random Signals and Systems
Course: ECEN 303-502
Maximum Grade: 5pt
"""

import random
import math
import matplotlib.pyplot as plt


ParameterP = 1.0/3.0    # Parameter of digital coin
ParameterA = 1.0/3.0    # Parameter of digital coin A
ParameterB = 1.0/2.0    # Parameter of digital coin B
NumberTrials = 100000
Trial1      = 4
Trial2      = 2


def biasedcoinflip(p=0.5):
 
    """
    This method returns a one with probability p and it returns a zero with
    probability (1 - p). The default parameter is p=0.5; this can be changed
    by passing an argument to the method.
    """
    return math.floor(random.random() + p)


def geometricflip(p=0.5):
    """
    This method returns a natural number that denotes the number of digital
    coin flips needed to obtain a one. It relies on method biasedcoinflip().
    """
    numberflips = 1
    while biasedcoinflip(p) != 1:
        numberflips += 1
    return numberflips

def doubleflip(p1=0.5 , p2= 0.5):
    numberflips = 1
    count1 = 0
    count2 = 0
    
    while (1):
        coin1 = biasedcoinflip(p1)
        coin2 = biasedcoinflip(p2)
        if (coin1 == coin2):
            numberflips += 1 s
        else:
                break
    if(coin1):
        count1 += 1
    elif(coin2):
         count2 += 1
     else:
       break
     return (numberflips, count1, count2)
     
        

print ("Part 1\n")

Trials = []
for TrialIndex1 in range(0, NumberTrials):
    Trials.append(geometricflip(ParameterP))
    
Sol1 = round(Trials.count(Part1)/float(EvenTrials),3)

EvenTrials = 0
for TrialIndex1 in range (0, NumberTrials):
      if(Trials[i]%2 == 0):
         EvenTrials += 1
       
 Sol2 = round(Trials.count(Part1)/float(EvenTrials),3)

print("The empirical probability that the  number of flips is 4 is") 
print(repr(Sol1))
print "The empirical probability that the number of flips is 4 conditional on number of flips being even is " \
print(repr(Sol2))


print ("Part 2\n")
Trials2 = []
FinalA = 0
FinalB = 0
for TrialIndex2 in range(0, NumberTrials):
	  results_i = doubleflip(ParameterA, ParameterB)		
	  Trials2.append(results_i[0])
	  FinalA += results_i[1]
	  FinalB += results_i[2]

Sol3 = round(Trials2.count(Part2)/float(NumberTrials), 3)
Sol4 = round(FinalA/float(NumberTrials),3)
Sol5 = round(FinalB/float(NumberTrials),3)

print ("Empirical probability that:")
print("\n Number of flips is")
print(repr(Part2))
print(repr(Sol3))
print ("Coin A is heads when the stopping condition is met:")
print(repr(Sol4) )
print("Coin B is heads when the stopping condition is met:")
print(repr(Sol5))



