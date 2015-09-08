__author__ = "Jesse Yancy"
__NetID__ = "jpy234"
__GitHubID__ = "jesseyancy23"

import random

Cardinality = 2
NumberTrials = 1000

TrialSequence = []
for TrialIndex in range(0, NumberTrials):
    TrialSequence.append(random.randrange(Cardinality))
   
   def biasedcoinflip(p=0.75):
    

        if random.random() < p:
            return 1
        else:
            return 0

EmpiricalDistribution = []
for OutcomeIndex in range(0, Cardinality):
    EmpiricalDistribution.append(TrialSequence.count(OutcomeIndex) / float(NumberTrials))
print EmpiricalDistribution
