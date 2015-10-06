__author__ = "Jose Pablo Dominguez"
__NetID__ = "jpdominguez94"
__GitHubID__ = "jpdominguez94"
__challenge__ = "2"
__version__ = "1.0"
__grader__ = ""
__SelfGrade__ = "5"
__PeerGrade__ = ""

"""
Random Signals and Systems
Course: ECEN 303-502
Maximum Grade: 5pt
"""

#Using Pythin 3.x

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
  
Solution1= 1.0*Trials.count(4) / len(Trials)    #times of event / total occurrences (added 1.0 to get the decimals)

print("The empirical probability that the  number of flips is 4 is " + format(Solution1, '.5f' ))

EvenTrials = []
for TrialIndex2 in range(0, NumberTrials):
    EvenTrials_temp = []    #temp array to determine the even flips 
    EvenTrials_temp.append(geometricflip(ParameterP)) #add all the trials to array
    if EvenTrials_temp[0] % 2 == 0:     #if it's even add it to the main array
        EvenTrials.append(EvenTrials_temp[0])

Solution2= 1.0*EvenTrials.count(4) / len(EvenTrials)    #times of event / total occurrences

print("The empirical probability that the number of flips is 4 conditional on number of flips being even is "  
    + format(Solution2, '.5f') + " ")

print "\nPart 2\n"

Trials2 = []
TrialsA = []
TrialsB = []
for TrialIndex2 in range(0, NumberTrials):
    FinalA = 0
    FinalB = 0
    counter = 0   #used to count the number of flips it takes
            
    while FinalA + FinalB != 1:  #keep flipping the coin until one of them is one and the other one isnt
        FinalA = biasedcoinflip(ParameterA)
        FinalB = biasedcoinflip(ParameterB)
        counter += 1        
    if FinalA == 1: #check to see if coin A is showing the 1
        TrialsA.append(1)
    else:            #check to see if coin B is showing the 1
        TrialsB.append(1)
    Trials2.append(counter)  #add the number of flips to the array

Solution3 = 1.0*Trials2.count(2) / len(Trials2) 
Solution4 = 1.0*len(TrialsA) / len(Trials2)
Solution5 = 1.0*len(TrialsB) / len(Trials2)


print ("The empirical probability that the number of flips is 2 is " + format(Solution3, '.5f' ))
print ("The empirical probability that coin A is showing 1 when the stopping condition is met is " + format(Solution4, '.5f' ))
print ("The empirical probability that coin B is showing 1 when the stopping condition is met is " + format(Solution5, '.5f' ))
