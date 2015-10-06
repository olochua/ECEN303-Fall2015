__author__ = "Charles Wallace"
__NetID__ = "chaswallace3"
__GitHubID__ = "chaswallace3"
__challenge__ = "2"
__version__ = "2.7"
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
ParameterA = 1.0/3.0   # Parameter of digital coin A
ParameterB = 1.0/2.0  # Parameter of digital coin B
NumberTrials = 100000

#defines a coin flip that returns a 1 with probability p

def biasedcoinflip(p=0.5):

    if(random.random()<=p):
        return 1
    else:
        return 0

    return math.floor(random.random() + p)

#defines a coin flip that counts the number of flips until a 1 appears

def geometricflip(p=0.5):

    numberflips = 1
    while biasedcoinflip(p) != 1:
        numberflips += 1
    return numberflips


print "Part 1\n"


Trials = []

#counts the number of flips until a 1 appears for NumberTrials trials
for TrialIndex1 in range(0, NumberTrials):
    Trials.append(geometricflip(ParameterP))
Solution1 = Trials.count(4)/float(NumberTrials)


print ("The empirical probability that the  number of flips is 4 is %.4f." % Solution1)


EvenTrials = 0
Evenand4 = 0

#Calculates the probability that the number of flips is 4 given the condition that the number of flips is even
for TrialIndex2 in range(0, NumberTrials):

   if(Trials[TrialIndex2]%2==0):
    EvenTrials += 1

   if(Trials[TrialIndex2]==4):
    Evenand4 += 1

PrEven = EvenTrials/float(NumberTrials)
#The probability of Even number of trials intersection with number of trials being 4
PrEvenand4 = Evenand4/float(EvenTrials)
#This is the definition of conditional probability
Prcondit4=PrEvenand4/float(PrEven)


print ("The empirical probability that the number of flips is 4 conditional on number of flips being even is %.4f."
%Prcondit4)

print "\nPart 2\n"

Trials2 = []
Afinal = []
Bfinal = []

#Flips two biased coins until the numbers associated with the coins are opposite
for TrialIndex2 in range(0, NumberTrials):
    numberflips2=0
    FinalA = 0
    FinalB = 0

    while(FinalA == FinalB):

        numberflips2 += 1
        FinalA = biasedcoinflip(ParameterA)
        FinalB = biasedcoinflip(ParameterB)

    Trials2.append(numberflips2)

    #Counts the number of times either A or B is one at the end of the Trial
    if(FinalA==1):
        Afinal.append(1)
    if(FinalB==1):
        Bfinal.append(1)

#Calculates all of the probabilities listed to the right of the print statements
Solution2 = Trials2.count(2)/float(NumberTrials)
Solution3 = Afinal.count(1)/float(NumberTrials)
Solution4 = Bfinal.count(1)/float(NumberTrials)


print "The empirical probability that the number of flips is 2 is %.4f." % Solution2
print "The empirical probability that coin A is showing 1 when the stopping condition is met is %.4f." %Solution3
print "The empirical probability that coin B is showing 1 when the stopping condition is met is %.4f." %Solution4