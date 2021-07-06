# reads in a file and returns list of all the words in the file
# removes punctuations from the strings
# lowercase all the strings
def getWords(filename):
    with open(filename) as f:
        lines = f.read().split()
        # removing punctuations from the list
        removechar = str.maketrans('', '', '.,()!"?;')
        comp = [s.translate(removechar) for s in lines]
        for i in range(len(comp)):
            comp[i] = comp[i].lower()
        return comp

# accepts list of words and counts occurences, returning a dictionary
# each iteration of words to KEY
# each count of words to VALUE
def countWords(wordList):
    word_dictionary = dict((x, wordList.count(x)) for x in set(wordList))
    return word_dictionary


# displays the counts after accepting a dictionary containing those counts from countWords
# take key from dictionary input into list
# sort the list alphabetically
# print the key and it's value(word count)
def display(wordDict):
    makeList = []
    for x in wordDict:
        makeList.append(x)
    makeList.sort()
    for i in makeList:
        print(i + ":", wordDict[i])
      
# main function with filename input
def main(filename):
    listit = getWords(filename)
    dictit = countWords(listit)
    display(dictit)

main('testfile.txt')