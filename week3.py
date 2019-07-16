#5.19
#a. It should assign a property the value of the input to compare the new tagged data to
#b. Take a key from the input list and compare its value to the new list, then total up the correct right divided by total number of keys

#5.30
brown_news_tagged = brown.tagged_words(categories='news', tagset='universal')
vocab = nltk.FreqDist(brown_news_tagged)
v1000 = [word for (word, _) in vocab.most_common(1000)]
mapping = defaultdict(lambda: 'UNK')
for v in v1000:
    mapping[v] = v
news2 = [mapping[v] for v in brown_news_tagged]
news2[:100]
brown_tagged_sents = brown.tagged_sents(categories='news')
size = int(len(brown_tagged_sents) * 0.9)
train_sents = brown_tagged_sents[:size]
bigram_tagger = nltk.BigramTagger(train_sents)
bigram_tagger.tag(news2[:100])
# The bigram tagger does not work now because alot of words are UNK so its context of the previous word to tag words is mess up, same with unigram.
#6.8
#import wordnet, random
def generalizeWord(string):
    if not wn.synsets(string):
        return string
    sset= wn.synsets(string)[0]
    if len(sset.hypernyms())>0:
        newWord= str(sset.hypernyms()[0]).split("'")[1].split(".")[0]
        return newWord
    return string
def document_features(document):
    document_words = set(document)
    features = {}
        for word in word_features:
            features['contains({})'.format(word)] = (word in document_words)
    return features

word_features = list(all_words)[:2000]
featuresets = [(document_features(d), c) for (d,c) in documents]
train_set, test_set = featuresets[100:], featuresets[:100]
classifier = nltk.NaiveBayesClassifier.train(train_set)
print(nltk.classify.accuracy(classifier, test_set))
def document_features(document):
    document_words = set(document)
    features = {}
        for word in word_features:
            word= generalizeWord(word)
            features['contains({})'.format(word)] = (word in document_words)
    return features
word_features = list(all_words)[:2000]
featuresets = [(document_features(d), c) for (d,c) in documents]
train_set, test_set = featuresets[100:], featuresets[:100]
classifier = nltk.NaiveBayesClassifier.train(train_set)
print(nltk.classify.accuracy(classifier, test_set))
#increases match by 2%
