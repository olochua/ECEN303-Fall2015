__author__ = "Eloi Fabian Tarango"
__NetID__ = "fabian.tarango"
__GitHubID__ = "fabiantarango"

import random

Cardinality = 2         #number of elements in the set
NumberTrials = 1000

TrialSequence = []
for TrialIndex in range(0, NumberTrials):
    TrialSequence.append(random.randrange(Cardinality))
  
if random.random() <= .75:
      TrialSequence.append(1)           #Probability of outcome of 1.
      
else: TrialSequence.append(0)           #Probability of outcome of 0 is .25.
    

EmpiricalDistribution = []
for OutcomeIndex in range(0, Cardinality):
    EmpiricalDistribution.append(TrialSequence.count(OutcomeIndex) / float(NumberTrials))
print EmpiricalDistribution
