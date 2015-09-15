__author__ = "Fernando Romo"
__NetID__ = "jfernandoromoddl"
__GitHubID__ = "FernandoRomo"

#Task3 the code produces a biased binary coin flip that returns one with probability 0.75 and zero otherwise.
import random

Cardinality = 2
NumberTrials = 1000

TrialSequence = []
for TrialIndex in range(0, NumberTrials):
   #TrialSequence.append(random.randrange(Cardinality))

    if random.random() <= 0.75:
        TrialSequence.append(1) #Probability of Heads 0.75, Heads = 1 (True)

    else:
        TrialSequence.append(0) #Probability of Tails 0.25, Tails = 0 (False)

EmpiricalDistribution = []
for OutcomeIndex in range(0, Cardinality):
    EmpiricalDistribution.append(TrialSequence.count(OutcomeIndex) / float(NumberTrials))
print EmpiricalDistribution
