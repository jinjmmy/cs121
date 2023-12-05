import re
import sys
import os.path

# The time complexity is O(n) where n is the length of the string s. The open() function is constant,
# read() is linear, lower() is linear, and my for loop is linear with respect to the string size, since it checks every character.
# re.match() is linear with respect to the string size it is matching, but i am only matching it against a single 
# character, which means it has a constant runtime. The while loop adds some overhead to the function 
# but the overall time complexity of the function is likely to be better for large files because it avoids reading the entire file into memory at once. 
# The append function also has constant runtime, therefore the entire function is linear in time complexity.
def tokenize(filePath, chunk = 1024):
    listOfTokens = []
    token = ''
    cutoffCharacters = ''
    append = False
    i = 0
    with open(filePath, 'r', encoding='latin-1') as f:
        text = f.read(chunk).lower()
        while text:
            i = 0
            if append and re.match("^[a-zA-Z0-9']+$",text[0]):
                newtext = listOfTokens[-1]
                while re.match("^[a-zA-Z0-9']+$",text[i]):
                    newtext += text[i]
                    i += 1  
                listOfTokens[-1] = newtext
            if re.match("^[a-zA-Z0-9']+$",text[-1]):
                append = True
            else:
                append = False

            token = ''
            for character in text[i:]:
                if not re.match("^[a-zA-Z0-9']+$",character) or character == "'":
                    if len(token) > 0:
                        listOfTokens.append(token)
                        token = ''
                else:
                    token += character
            if len(token) > 0:
                listOfTokens.append(token)
            text = f.read(chunk).lower()

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
    for key,value in sorted(dict.items(), key=lambda x: (-x[1], x[0])):
        print(key, '->', value)


# The runtime of the main function is O(nlogn).
def main():
    try:
        filePath = sys.argv
        if len(sys) == 2:
            filePath = sys.argv[1]
            if filePath[-4:] == '.txt' and os.path.exists(filePath):
                listOfTokens = tokenize(filePath)
                dict = computeWordFrequencies(listOfTokens)
                printFrequencies(dict)
            else:
                raise Exception
        else:
            raise Exception
    except:
        print("Invalid input.")

if __name__ == '__main__':
    main()
