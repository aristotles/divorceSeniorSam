import nltk
#nltk.download()
from nltk.book import *
from nltk.corpus import brown
#1.25
sent=['she', 'sells', 'sea', 'shells', 'by', 'the', 'sea', 'shore']
for string in sent:
    if len(string)>3or string[:2]=='sh':print(string)
#1.27

def vocab_size(text):
    print(len(set(text)))
#1.28
print("hello world")
def percent(word, text):
    print(100 * text.count(word) / len(text))
#2.17
def nonStop50(text):
    stopwords = nltk.corpus.stopwords.words('english')
    texts50 = FreqDist(text).most_common(50)
    for w in texts50:
        if w[0].lower() not in stopwords:
            print(w[0])
#2.18 text4.collocations() this function keeps creating an error and I need it to do this problem
#2.19
cfd = nltk.ConditionalFreqDist(
    (genre, word)
    for genre in brown.categories()
    for word in brown.words(categories=genre))
genres = ['fiction', 'adventure', 'science_fiction', 'romance', 'mystery']
modals = ['love', 'problem', 'mystery', 'betray', 'death', 'murder']
cfd.tabulate(conditions=genres, samples=modals)
