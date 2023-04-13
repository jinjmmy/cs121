import re
import sys

# The time complexity is O(n) where n is the length of the string s. The open() function is constant,
# read() is linear, lower() is linear, and my for loop is linear with respect to the string size, since it checks every character.
# re.match() is linear with respect to the string size it is matching, but i am only matching it against a single 
# character, which means it has a constant runtime. The append function also has constant runtime, therefore the entire function is linear in time complexity.
def tokenize(filePath):
    listOfTokens = []
    token = ''
    with open(filePath, 'r+', encoding='utf-8') as f:
            text = f.read().lower()
    for character in text:
        if not re.match("[a-zA-Z0-9']",character):
            if len(token) > 0:
                listOfTokens.append(token)
                token = ''
        else:
            token += character
    if len(token) > 0:
        listOfTokens.append(token)
    
    return listOfTokens

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
    for key,value in sorted(dict.items(), key=lambda x:x[1],reverse=True):
        print(key, '->', value)


# The runtime of the main function is O(nlogn).
def main():
    filePath = sys.argv[1]
    listOfTokens = tokenize(filePath)
    dict = computeWordFrequencies(listOfTokens)
    printFrequencies(dict)


if __name__ == '__main__':
    main()