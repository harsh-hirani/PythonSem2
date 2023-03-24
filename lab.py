# p5 6 - comment a code
# function to check the sequence in given string in order of pattern
# given code can be written in a different way like this:
from collections import OrderedDict
def checkOrder(input, pattern):
    # dict = OrderedDict.fromkeys(input)
    ptrlen = 0 # later to evalute how many pattern aplphabet are in order
    # for key,value in dict.items():
    for key in input:
        if (key == pattern[ptrlen]):
            ptrlen = ptrlen + 1 # if we have a pattern alphabet in string then by adding it by one we go to the next pattern alphabet
        if (ptrlen == (len(pattern))):# if we have a pattern means we have all the pattern alphabet in string in order like pattern
            return 'true'
    return 'false'
if __name__ == "__main__":
    input = 'engineers rock'
    pattern = 'er'
    print (checkOrder(input,pattern)) 