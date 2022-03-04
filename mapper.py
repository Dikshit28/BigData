# Big Data Thursday - 1

#read data.txt
""" file=open("data.txt","r")
data=file.read()
print(data)
arr=data.split(",")
print(arr)
output={}
for i in range(0,len(arr)):
    if arr[i] in output.keys():
        output[arr[i]]+=1
    else:
        output[arr[i]]=1
print(output)
file.close() """

def wordcountmapper():
    """
    Reads a file and returns the data
    """
    filename=input("Enter the filename: ")
    with open(filename,"r") as f:
        data=f.read()
    
    wordlist=data.split(",")
    n=len(wordlist)
    for word in wordlist:
        yield word,n