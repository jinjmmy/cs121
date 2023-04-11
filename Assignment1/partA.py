import re
import sys

#the time complexity is O(n)
def tokenize(filePath):
    listOfTokens = []
    try:
        with open(filePath, 'r+') as f:
            text = f.read().lower()
        listOfTokens = re.findall(r'\b\w+\b',text)
        return listOfTokens
    except:
        None

#the time complexity is O(n) or linear since there is only one for loop
#that iterates through N number of tokens
def computeWordFrequencies(listOfTokens):
    newDict = {}
    for key in listOfTokens:
        if key not in newDict:
            newDict[key] = 1
        else:
            newDict[key] += 1
    return newDict

#the ti
def printFrequencies(dict):
    for key,value in sorted(dict.items(), key=lambda i: (-i[1], i[0])):
        print(key, '->', value)


def main():
    filePath = sys.argv[1]
    listOfTokens = tokenize(filePath)
    dict = computeWordFrequencies(listOfTokens)
    printFrequencies(dict)


if __name__ == '__main__':
    main()