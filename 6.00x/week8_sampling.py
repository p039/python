'''
STOCHASTIC PROCESSES
An ongoing process where the next state might depend on both the previous states and some random element.
Rolling a die is non-deterministic process.
'''


import random

def rollDie():
    return random.choice([1,2,3,4,5,6])

def rollN(n):
    result = ''
    for i in range(n):
        result = result + str(rollDie())
    return result

'''
Which of this more random? Each of this is equaly likely because the 
value of each roll is independant of the previous roll. That is to say 
the fact that I rolled a 1 the first time has no impact on whether or 
not I will roll a 1 the second time.

In general, when we talk about the probability of a result having some
property, for example, being all ones, we're asking, what fraction of all
possible results has the property?
That tells us that we need to start with the question, how many different

And we saw that given n binary digits, there were 2^n
possible binary numbers.
When we looked at decimal digits, we saw that it was 10^n .
And now, with the dice, we're looking at digits base 6.
So the number of possibilities are going to be 6^n.

Result: Possible sequence of length 5 is 6^5 = 7776 possible seqeunces.
'''

rollN(5)
>>>'24353'
>>>'53532'

'''
Probability there all ones '11111' is 1/6^5. It's approximately equal to 0.0001286,
or a simpler way to think about it - 1 out of 7,776 possibilities.

Pretty low value, but no lower than the probability of any other particular
sequence of five rolls. Let's see the probability is the same in sim model.
'''

def getTarget(goal):
    numTries = 0
    numRolls = len(goal)
    while True:
        numTries += 1
        result = rollN(numRolls)
        if result == goal:
            return numTries

def runSim(goal, numTrials):
    total = 0
    for i in range(numTrials):
        total += getTarget(goal)
    print 'Average number of tries =', total/float(numTrials)

runSim('11111', 100)
runSim('54324', 100)
