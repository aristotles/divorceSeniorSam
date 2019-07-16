#SYNSET/WORDNET
#3.6
#Any letter
#Any letters starting with new capital letter
#P any two vowels t
#Numbers
#Pattern of constenaninent vowel conestent
#Letters or numbers

#3.7 a.
#^a$|^an$|^the$

#3.42
#4.14
def novel10(text):
	length=len(text)
	for w in text1[ninety:length]:
		if w not in text1[0:ninety]:
			print(w)
#4.15
def multiCheck(spot,wordList,count)-> int:
    if(wordList[spot]==wordList[spot+1]):
        multiCheck(spot+1,wordList,count+1)
    else:
        return count/len(wordList)
def sortSentence(string):
	lastPlace=0
	firstOne=True
	currentPlace=0
	wordList=[]
	for w in string:
		if w==' 'or w=='.':
			if firstOne==True:
				wordList.append(string[lastPlace:currentPlace].lower())
				firstOne=False
			else:
				wordList.append(string[lastPlace+1:currentPlace])
			lastPlace=currentPlace
		currentPlace+=1
	wordList.sort()
	oneFrequncy=1/len(wordList)
	for w in wordList:
		print(w+' '+ str(multiCheck(wordList.index(w),wordList,1)))
#4.19
def sortedDis(list, mainSyn):
    #returns closest first
    distanceList= []
    for syn in list:
        distanceList.append(syn.shortest_path_distance(mainSyn))
    dictionary = dict(zip(distanceList, list))
    returnList=[]
    for key in sorted(dictionary):
        returnList.append(dictionary.get(key))
    return returnList
