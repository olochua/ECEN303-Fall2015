__author__ = "Alejandro Penaloza Rodriguez"
__NetID__ = "alex23"
__GitHubID__ = "alex23tamu"

import random

Cardinality = 2
NumberTrials = 1000

TrialSequence = []
for TrialIndex in range(0, NumberTrials):
    TrialSequence.append(random.randrange(Cardinality))
   
      if random.random() <= 0.75:
        Trials.append(1) #Probability of Heads 0.75, Heads = 1 (True)

    else:
        Trials.append(0) #Probability of Tails 0.25, Tails = 0 (False)

EmpiricalDistribution = []
for OutcomeIndex in range(0, Cardinality):
    EmpiricalDistribution.append(TrialSequence.count(OutcomeIndex) / float(NumberTrials))
print EmpiricalDistribution
