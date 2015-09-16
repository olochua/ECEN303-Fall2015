__author__ = ""
__NetID__ = ""
__GitHubID__ = ""
__challenge__ = "1"
__version__ = "0.0"
__grader__ = ""
__SelfGrade__ = ""
__PeerGrade__ = ""

"""
Random Signals and Systems
Course: ECEN 303-502
Maximum Grade: 5pt
"""

import random
import math
import matplotlib.pyplot as plt


__author__ = 'benjamin'

import random

def biasedcoinflip(p=0.7):
    Record = []
    Cardinality = 1000
    S = 1
    k = 0
    q = int(p*1000)
    NumberTrials = 8

    for TrialIndex in range(0,NumberTrials):
        j = 0
        TrialSequence = []
        TrialSequence.append(random.randrange(Cardinality))

        EmpiricalDistribution = []
        for OutcomeIndex in range(0, Cardinality):
            EmpiricalDistribution.append(TrialSequence.count(OutcomeIndex) / float(S))

        for OutcomeIndex in range(0, q):
            j += EmpiricalDistribution[OutcomeIndex]
            k += EmpiricalDistribution[OutcomeIndex]
        Record.append(j)

    print(Record)
    print('number of 1\'s: '), print(k)
    print('number of 0\'s: '), print(NumberTrials-k)

biasedcoinflip()

## 1.) As the parameter "p" is changed from 0-1, the probability that the coin will land on heads ("1") increases from a 0% to a 100% chance respectively.

## 2.) The most likely outcome will be 5xheads and 3xtails.
