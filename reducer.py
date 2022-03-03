import mapper

wordgenerator=mapper.wordcountmapper()
words={}
word,n=next(wordgenerator)
words[word]=1
for i in range(n-1):
    word,n=next(wordgenerator)
    if word in words.keys():
        words[word]+=1
    else:
        words[word]=1
        
print(words)