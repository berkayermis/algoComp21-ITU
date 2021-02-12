import math

theSentence = input()
theWordsList = theSentence.split()

def main(theSentence):
    wordLen = {}

    for i in theWordsList:
        if len(i) not in wordLen:
            wordLen[len(i)] = 1
        else:
            wordLen[len(i)] += 1


    finalProb = 1

    for key, value in wordLen.items():
        finalProb *= math.factorial(value)

    return (finalProb * (1 / (math.factorial(len(theWordsList)))))

main(theSentence)