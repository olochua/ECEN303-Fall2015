__author__ = "Clarissa Tovias"
__NetID__ = "toviasc"
__GitHubID__ = "toviasc"

import random

Cardinality = 2
NumberTrials = 1000

TrialSequence = []
for TrialIndex in range(0, NumberTrials):
    TrialSequence.append(random.randrange(Cardinality))
    #
    # EDIT
    # Modify code to produce biased binary coin flip that returns one with probability 0.75
    # and zero otherwise
    #
    
    if random.random() <= 0.25:
        TrialSequence.append(0) #Tails 25% of times
        
    else:
        TrialSequence.append(1) #Heads 75% of times
        
EmpiricalDistribution = []
for OutcomeIndex in range(0, Cardinality):
    EmpiricalDistribution.append(TrialSequence.count(OutcomeIndex) / float(NumberTrials))
print EmpiricalDistribution
