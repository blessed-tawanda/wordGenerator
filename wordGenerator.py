from itertools import permutations,filterfalse
from math import floor

class WordGenerator():
    def __init__(self,scrambledLetters,wordLength):
        self.foundWords = []
        self.wordLength = wordLength
        self.scrambledLetters = scrambledLetters
        self.dictionaryWords = []
        self.possibleWords = []
        self.getWordsFromDictionary()
        self.createPossibleWords()
        self.findWords()
        

    def getWordsFromDictionary(self):
        wordsObject = open('wordlist.txt','r')
        words = wordsObject.readlines()
        for word in words:
            self.dictionaryWords.append(word.strip())

    def createPossibleWords(self):
        pcombinations = list(permutations(self.scrambledLetters,self.wordLength))
        
        for pcombination in pcombinations:
            self.possibleWords.append(''.join(pcombination))

    def findWords(self):
        for possibleWord in self.possibleWords:
            word = self.binarySearch(self.dictionaryWords,possibleWord,0,69904)
            if word != -1:
                self.foundWords.append(word)

    
    def binarySearch(self,dictionaryWords,word,l,r):
        if int(r) >= int(l):
            mid = floor(l + (r - l)/2)
            # If element is present at the middle itself
            if dictionaryWords[mid] == word:
                return dictionaryWords[mid]
            # If element is smaller than mid, then it 
            # can only be present in left subarray
            elif dictionaryWords[mid] > word:
                return self.binarySearch(dictionaryWords,word,l, mid-1)
            # Else the element can only be present 
            # in right subarray
            else:
                return self.binarySearch(dictionaryWords,word,mid+1, r)
        else:
            # Element is not present in the array
            return -1
    
    def unique(self,iterable, key=None):
        #"List unique elements, preserving order. Remember all elements ever seen."
        # unique_everseen('AAAABBBCCDAABBB') --> A B C D
        # unique_everseen('ABBCcAD', str.lower) --> A B C D
        seen = set()
        seen_add = seen.add
        if key is None:
            for element in filterfalse(seen.__contains__, iterable):
                seen_add(element)
                yield element
        else:
            for element in iterable:
                k = key(element)
                if k not in seen:
                    seen_add(k)
                    yield element


jumbledLetters = ""

def displayMenu():
    print('==================================')
    print('\n1. Change Letters and Number of Letters \n2. Quit')       
    print('==================================')


def userInput():
    jumbledLetters = input("Enter the jumbled letters: ")
    numberOfLettersInWord = int(input("Enter number of letters in words to generate: "))
    wordGen = WordGenerator(jumbledLetters,numberOfLettersInWord)

    for word in wordGen.foundWords:
        print(word)


def main():
    userInput()
    displayMenu()
    response = int(input("Select Operation: "))
    if response == 1:
        main()
    elif response == 2:
        exit()

main()