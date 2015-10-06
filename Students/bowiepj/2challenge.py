__author__ = "Philip Bowie"
__NetID__ = "bowiepj"
__GitHubID__ = "bowiepj"
__challenge__ = "2"
__version__ = "3.4"
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


def biasedcoinflip(p=0.5):
    if(random.random()<=p):
        return 1
    else:
        return 0
    """
    This method returns a one with probability p and it returns a zero with
    probability (1 - p). The default parameter is p=0.5; this can be changed
    by passing an argument to the method.
    """
    return math.floor(random.random() + p)  #will either be 1 or 0, goes until 1


def geometricflip(p=0.5):
    """
    This method returns a natural number that denotes the number of digital
    coin flips needed to obtain a one. It relies on method biasedcoinflip().
    """
    numberflips = 1
    while biasedcoinflip(p) != 1:
        numberflips += 1
    return numberflips


print ("Part 1\n")

Trials = []
for TrialIndex1 in range(0, NumberTrials):
    Trials.append(geometricflip(ParameterP))
Solution1 = Trials.count(4)/(1.0*len(Trials))

print ("The empirical probability that the  number of flips is 4 is %.4f." %Solution1

EvenTrials = 0
Valueof4 = 0
for TrialIndex2 in range(0, NumberTrials):

      if(Trials[TrialIndex2]%2==0):
           EvenTrials += 1

        if(Trials[TrialIndex2]==4):
           Valueof4 += 1
pEven = EvenTrials/float(NumberTrials)  #probability of even numbers
pFour = Valueof4/float(EvenTrials)  #Probability of Even intersection with value of 4
pcondition = pFour/float(pEven) #conditional probability to get the condition of 4

print ("The empirical probability that the number of flips is 4 conditional on number of flips being even is %.4f." %pcondition)


print "\nPart 2\n"

Trials2 = []
FinalA = []
FinalB = []

#Flips two biased coins until the two numbers are opposite because you need one coin to be 1 and the other to be 0
for TrialIndex2 in range(0, NumberTrials):
    Flipcount = 0
    afinal = 0
    bfinal = 0

    while(afinal == bfinal):

       Flipcount += 1
       afinal = biasedcoinflip(ParameterA)
       bfinal = biasedcoinflip(ParameterB)

    Trials2.append(Flipcount)
    #finds the amount of times each value has a 1 for the trial
    if(afinal==1)
       FinalA.append(1)
    if(bfinal==1)
       FinalB.append(1)

#calculate the probabilities required
Solution2 = Trials2.count(2)/float(NumberTrials)
Solution3 = FinalA.count(1)/float(NumberTrials)
Solution4 = FinalB.count(1)/float(NumberTrials)

      
print "The empirical probability that the number of flips is 2 is %.4f." %Solution2 
print "The empirical probability that coin A is showing 1 when the stopping condition is met is %.4f." %Solution3 
print "The empirical probability that coin B is showing 1 when the stopping condition is met is %.4f." %Solution4


