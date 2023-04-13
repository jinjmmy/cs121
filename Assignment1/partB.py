import sys
import partA

#
def intersection(fileA,fileB):
    fileA_tokens = partA.tokenize(fileA)
    fileB_tokens = partA.tokenize(fileB)
    dictA = partA.computeWordFrequencies(fileA_tokens)
    dictB = partA.computeWordFrequencies(fileB_tokens)

    setA = set(dictA.keys())
    setB = set(dictB.keys())

    intersect = setA.intersection(setB)


# The time complexity of the main() is linear.
def main():
    files  = sys.argv
    fileA = files[1]
    fileB = files[2]
    intersection(fileA,fileB)