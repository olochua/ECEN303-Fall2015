__author__ = "Chu Liang"
__NetID__ = "cml1012"
__GitHubID__ = "cml1012"
__challenge__ = "2"
__version__ = "0.0"
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
Trial1 = 4
Trial2 = 2

def biasedcoinflip(p=0.5):
    for TrialIndex in range(0, NumberTrials):
        TrialSequence.append(random.randrange(2))
        if (sum(TrialSequence)/ (1.0 *len(TrialSequence))) < ParameterP:
            TrialSequence[len(TrialSequence)-1] = 1
            return 1
        else:
            TrialSequence[len(TrialSequence)-1] = 0
            return 0
    return math.floor(random.random() + p)


def geometricflip(p=0.5):
    
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
            numberflips += 1 
        else:
                break
    if(coin1):
        count1 += 1
    elif(coin2):
        count2 += 1
    else:
            break
    return (numberflips, count1, count2)

print "Part 1\n"

Trials = []
for TrialIndex1 in range(0, NumberTrials):
    Trials.append(geometricflip(ParameterP))
    Solution1 = round(Trials.count(Part1)/float(EvenTrials),3)
    
EvenTrials = 0
for TrialIndex1 in range(0, NumberTrials):
    if(Trials[i]%2 == 0):
         EvenTrials += 1
    Solution2 = round(Trials.count(Part1)/float(EvenTrials), 3)

print "The empirical probability that the  number of flips is 4 is " 
print(repr(Solution1))
print "The empirical probability that the number of flips is 4 conditional on number of flips being even is " 
print(repr(Solution2))


print "\nPart 2\n"

Trials2 = []
FinalA = 0
FinalB = 0
for TrialIndex2 in range(0, NumberTrials):
    result_a = doubleflip(ParameterA, ParameterB)
    Trial2.append(result_a[0])
    FinalA += result_a[1]
    FinalB += result_a[2]

Solution3 = round(Trials.count(Part1)/float(EvenTrials), 3)
Solution4 = round(FinalA/float(NumberTrials),3)
Solution5 = round(FinalB/float(NumberTrials),3)

print "The empirical probability that the number of flips is 2 is " 
print(repr(Solution3))    
print "The empirical probability that coin A is showing 1 when the stopping condition is met is " 
print(repr(Solution4))   
print "The empirical probability that coin B is showing 1 when the stopping condition is met is " 
print(repr(Solution5))    
