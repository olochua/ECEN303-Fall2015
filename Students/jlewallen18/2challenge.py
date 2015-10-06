__author__ = "Jordan Lewallen"
__NetID__ = "922009210"
__GitHubID__ = "jlewallen18"
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

import random
import math
import matplotlib.pyplot as plt


ParameterP   = 1.0/3.0     # Parameter of digital coin
ParameterA   = 1.0/3.0     # Parameter of digital coin A
ParameterB   = 1.0/2.0    # Parameter of digital coin B
NumberTrials = 100000
first_trial      = 4
second_trial     = 2


def biasedcoinflip( p = 0.5 ):
    """
    This method returns a one with probability p and it returns a zero with
    probability (1 - p). The default parameter is p=0.5; this can be changed
    by passing an argument to the method.
    """
    return math.floor(random.random() + p)


def geometricflip( p = 0.5 ):
    """
    This method returns a natural number that denotes the number of digital
    coin flips needed to obtain a one. It relies on method biasedcoinflip().
    """
    numberflips = 1
    while biasedcoinflip(p) != 1:
        numberflips += 1
    return numberflips

def doublegeometricflip( pr_A = 0.5 , pr_B = 0.5 ):
	# this will calculate a double flip experiment
	numberflips = 1
	numberA = 0
	numberB = 0

	while (1):
		coin_A = biasedcoinflip(pr_A)
		coin_B = biasedcoinflip(pr_B)
		if (coin_A == coin_B):				# statement to flip the coins
			numberflips += 1
		else:
			break
	if (coin_A):
		numberA += 1					# set when A is 1
	elif(coin_B):
		numberB += 1					# set when B is 1
	else:
		print ("\nThis is an ERROR\n")
	return (numberflips, numberA, numberB)


print "\nPart 1"
print "(ParameterP = " \
	  + repr(float(round(ParameterP,4))) \
	  + ")"

Trials = []
for TrialIndex1 in range(0, NumberTrials):
    Trials.append(geometricflip(ParameterP))

Solution1 = round(Trials.count(first_trial)/float(NumberTrials), 4)

# observe the even results
EvenTrials = 0
for i in range(0, NumberTrials):
	if (Trials[i]%2 == 0):
		EvenTrials += 1


Solution2 = round(Trials.count(first_trial)/float(EvenTrials), 4)

#print the first set of results here
print "\nEmpirical probability that:"	\
	+ "\n\tNumber of flips is " \
	+ repr(first_trial) \
	+ ": \t" \
    + repr(Solution1) \
	+ "\n\tNumber of flips is " \
	+ repr(first_trial) \
	+ ", given that number of flips is even: " \
	+ repr(Solution2)


#print second set of results here
print "\nPart 2"
print "(ParameterA = " \
	  + repr(float(round(ParameterA,4))) \
	  + ", ParameterB = " \
	  + repr(float(round(ParameterB,4))) \
	  + ")"

Trials2 = []	
FinalA = 0		
FinalB = 0		

for TrialIndex2 in range(0, NumberTrials):
	results_i = doublegeometricflip(ParameterA, ParameterB)		
	Trials2.append(results_i[0])
	FinalA += results_i[1]
	FinalB += results_i[2]

#below are the other set of tests!
Solution3 = round(Trials2.count(second_trial)/float(NumberTrials), 3)
Solution4 = round(FinalA/float(NumberTrials),4)
Solution5 = round(FinalB/float(NumberTrials),4)

# Print the answers
print "\nEmpirical probability that:" \
      + "\n\tNumber of trials is " \
      + repr(second_trial) \
      + ": \t" \
      + repr(Solution3) \
      + "\n\tCoin A is showing 1 when the stopping condition is met: " \
      + repr(Solution4) \
      + "\n\tCoin B is showing 1 when the stopping condition is met: " \
      + repr(Solution5)

print "\n"
