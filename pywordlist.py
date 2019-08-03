'''
 Iterate over the odd number position elements in list using while loop
'''
wordList="Hello Bangladesh I am alone"
i = 0
sizeofList = len(wordList) 
while i < sizeofList :
    if i % 2 == 1 :
        print(wordList[i]) 
    i += 1