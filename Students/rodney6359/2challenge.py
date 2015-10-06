__author__ = "Rodney Siders"
__NetID__ = "rodney6359"
__GitHubID__ = "rodney6359"
__challenge__ = "2"
__version__ = "1.0"
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


print "Part 1\n"

Trials = []
for TrialIndex1 in range(0, NumberTrials):
    Trials.append(geometricflip(ParameterP))
    
solution1 = Trials.count(4)/float(len(Trials))
print("The empirical probability that the  number of flips is 4 is " + repr(solution1) + ".")


EvenTrials = 0
for TrialIndex2 in range(0, NumberTrials):
   if Trials[TrialIndex2]%2 == 0: #multiples of 2 for Trials
        EvenTrials += 1
        
solution2 = Trials.count(4)/ float(EvenTrials)
print("The empirical probability that the number of flips is 4 conditional on number of flips being even is " + repr(solution2) + ".")
    
print "\nPart 2\n"

def BiasedGeometricFlip(p = 0.5,q = 0.5):
    set = 0
    countA = 0
    countB = 0
    count = 0
    while set == 0:
        placeHolderA = biasedcoinflip(p)
        placeHolderB = biasedcoinflip(q)

        if placeHolderA == placeHolderB:
            count +=1
        elif (placeHolderA == 1 - placeHolderB):
            count += 1
            countA += placeHolderA
            countB += placeHolderB
            set = 1

    return(count,countA,countB)

Trials2 = []
FinalA = 0
FinalB = 0
for TrialIndex3 in range(0, NumberTrials):
    Result = BiasedGeometricFlip(ParameterA,ParameterB)
    Trials2.append(Result[0])
    FinalA += Result[1]
    FinalB += Result[2]

solution3 = Trials2.count(2)/ float(NumberTrials)
solution4 = FinalA/ float(NumberTrials)
solution5 = FinalB/ float(NumberTrials)


print ("The empirical probability that the number of flips is 2 is " + repr(solution3) + ".")

print ("The empirical probability that coin Alpha is showing 1 when the stopping condition is met is " + repr(solution4)+ ".")

print ("The empirical probability that coin Beta is showing 1 when the stopping condition is met is " + repr(solution5)+ ".")
