__author__ = "Derek Heidtke"
__NetID__ = "622001748"
__GitHubID__ = "derekheidtke"
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
Part1_N      = 4
Part2_N      = 2


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

def doublegeometricflip( pA = 0.5 , pB = 0.5 ):
	# performs one double flip experiment
	numberflips = 1
	countA = 0
	countB = 0

	while (1):
		coinA = biasedcoinflip(pA)
		coinB = biasedcoinflip(pB)
		if (coinA == coinB):				# flip tha coins
			numberflips += 1
		else:
			break
	if (coinA):
		countA += 1					# record when A was only ONE
	elif(coinB):
		countB += 1					# record when B was only ONE
	else:
		print ("\nERROR: Should not happen.\n")
	return (numberflips, countA, countB)

#====================================================================
print "\nPart 1"
print "(ParameterP = " \
	  + repr(float(round(ParameterP,3))) \
	  + ")"

Trials = []
for TrialIndex1 in range(0, NumberTrials):
    Trials.append(geometricflip(ParameterP))

Solution1 = round(Trials.count(Part1_N)/float(NumberTrials), 3)

# count the number of even results
EvenTrials = 0
for i in range(0, NumberTrials):
	if (Trials[i]%2 == 0):
		EvenTrials += 1

# from definition of conditional probability (number_of_4s/number_of_Evens)
Solution2 = round(Trials.count(Part1_N)/float(EvenTrials), 3)

# Print Solution1 and Solution2
print "\nEmpirical probability that:"	\
	+ "\n\tNumber of flips is " \
	+ repr(Part1_N) \
	+ ": \t\t\t\t\t\t" \
    + repr(Solution1) \
	+ "\n\tNumber of flips is " \
	+ repr(Part1_N) \
	+ ", given that number of flips is even: \t" \
	+ repr(Solution2)


#====================================================================
print "\nPart 2"
print "(ParameterA = " \
	  + repr(float(round(ParameterA,3))) \
	  + ", ParameterB = " \
	  + repr(float(round(ParameterB,3))) \
	  + ")"

Trials2 = []	# list of number of flips it took to stop in each trial
FinalA = 0		# number of times A was ONE when stopped
FinalB = 0		# number of times B was ONE when stopped

for TrialIndex2 in range(0, NumberTrials):
	results_i = doublegeometricflip(ParameterA, ParameterB)		# defined above
	Trials2.append(results_i[0])
	FinalA += results_i[1]
	FinalB += results_i[2]

# count number of times that 2 was the result
Solution3 = round(Trials2.count(Part2_N)/float(NumberTrials), 3)

# calculate the fraction of A over the sum, A+B
Solution4 = round(FinalA/float(NumberTrials),3)
# calculate the fraction of B over the sum, A+B
Solution5 = round(FinalB/float(NumberTrials),3)

# Print Solution3, Solution4, and Solution5
print "\nEmpirical probability that:" \
      + "\n\tNumber of trials is " \
      + repr(Part2_N) \
      + ": \t\t\t\t\t\t" \
      + repr(Solution3) \
      + "\n\tCoin A is heads when the stopping condition is met: \t\t" \
      + repr(Solution4) \
      + "\n\tCoin B is heads when the stopping condition is met: \t\t" \
      + repr(Solution5)

print "\n"