# Importing the mapper module.
import mapper

# Creating a dictionary of words and their counts.
wordgenerator=mapper.wordcountmapper()
words={}
word,n=next(wordgenerator)
words[word]=1
# This is the code that is used to count the number of times a word appears in the text.
for i in range(n-1):
    word,n=next(wordgenerator)
    if word in words.keys():
        words[word]+=1
    else:
        words[word]=1

# `print(words)` is printing the dictionary of words and their counts.
print(words)