#Chapter 10 Try its:

#N[SEM='Population'] -> 'populations'
#CardN[SEM='1000'] -> '1,000,000' 
#Conj[SEM='AND'] -> 'and'
#TV[SEM=''] -> 'have'
#P[SEM='>'] -> 'above'

# Yes, works very similiar to logic in discrete functions

#Picture: https://docs.google.com/document/d/1PlnQGlxkfaLKDYuh_a9AgOhGHUoRXsrxwPupmYHQ6xk/edit

#v2 = """
#bruce => b
#elspeth => e
#julia => j
#matthew => m
#person => {b, e, j, m}
#admire => {(b, j), (b, e), (b, m),(b,b),(m,b),(m,m),(m,e),(m,j),(e,e),(e,b),(e,j),(e,m),(j,j),(j,e),(j,b),(j,m)}
#"""
#11.11
merchant_file = nltk.data.find('corpora/shakespeare/merchant.xml')
from xml.etree.ElementTree import ElementTree
merchant = ElementTree().parse(merchant_file)
def searchWord(string):
    returnlist=[]
    for i, act in enumerate(merchant.findall('ACT')):
        for j, scene in enumerate(act.findall('SCENE')):
            for k, speech in enumerate(scene.findall('SPEECH')):
                for line in speech.findall('LINE'):
                    if string in str(line.text):
                        newlist=[]
                        newlist.append(i+1)
                        newlist.append(j+1)
                        newlist.append(k+1)
                        returnlist.append(newlist)
    return(returnlist)
#11.12
def searchWord(string,limit):
    speechcount=0
    for i, act in enumerate(merchant.findall('ACT')):
        for j, scene in enumerate(act.findall('SCENE')):
            for k, speech in enumerate(scene.findall('SPEECH')):
                wordcount=0
                for speaker in speech.findall('SPEAKER'):
                    if string in str(speaker.text):
                        for line in speech.findall('LINE'):
                            wordcount+=len(line.text.split())
                        if wordcount == limit:
                            speechcount+=1
    print(speechcount)

