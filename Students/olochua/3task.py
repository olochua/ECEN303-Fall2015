__author__ = "Jui Yen Chua"
__NetID__ = "olochua"
__GitHubID__ = "olochua"

import random

#define the variables
Cardinality = 2
NumberTrials = 1000

#create an empty vector
TrialSequence = []

for TrialIndex in range(0, NumberTrials):
    #associate probability with randomly generated values
    #and append the results to the vector TrialSequence
    if random.random()<0.75: 
        TrialSequence.append(1)
    else:
        TrialSequence.append(0)        

#create an empty vector
EmpiricalDistribution = []

for OutcomeIndex in range(0, Cardinality):
    #calculate the distribution of 0 and 1
    EmpiricalDistribution.append(TrialSequence.count(OutcomeIndex) / float(NumberTrials))

#display the results
print EmpiricalDistribution
