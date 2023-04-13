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

#the time complexity is O(n) or linear with respect to the length of the token list since there is only one for loop that iterates through N number of tokens
#The for loop is linear with respect to the token list size, and updating the dict is constant.
def computeWordFrequencies(listOfTokens):
    newDict = {}
    for key in listOfTokens:
        if key not in newDict:
            newDict[key] = 1
        else:
            newDict[key] += 1
    return newDict

# printFrequencies time complexity is O(nlogn) since we sort the tokens dictionary by descending values. 
# Then, the for loop is linear with respect to the dictionary size. 
def printFrequencies(dict):
    for key,value in sorted(dict.items(), key=lambda i: (-i[1], i[0])):
        print(key, '->', value)


# The runtime of the main function is O(nlogn).
def main():
    filePath = sys.argv[1]
    listOfTokens = tokenize(filePath)
    dict = computeWordFrequencies(listOfTokens)
    printFrequencies(dict)


if __name__ == '__main__':
    main()