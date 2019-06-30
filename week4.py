#7.4
def chinker(sentence):
	grammar = r"""
  NP:
    {<.*>+}
    }<VBD|IN>+{
  """
	cp = nltk.RegexpParser(grammar)
	print(cp.parse(sentence))
#VBD and IN will make up the tags of chinks. This works very similair to a normal chunker, except it identies
#	everything not a chunk, instead of what is a chunk.
#7.10
# Yes by turning it into a trigram chunker the accuracy is improved by 3%.
#8.4
#One can use the tree.height to return the depth
def treeDepth(tree):
    return tree.height()
#8.25
def longestSentence(text):
	currentSen=0
	running=0
	sen_list = [1]
	for word in text:
		if(word==" "):
			running+=1
		elif("." in word):
			if(max(sen_list)<currentSen):
				sen_list.append(currentSen)
				print(max(sen_list))
			currentSen=0
			running+=1
		else:
			running+=0
			currentSen+=1
	print(max(sen_list))
#The long sentences seem to be due to conversations or exarts/quote from the book before the text starts.
	
