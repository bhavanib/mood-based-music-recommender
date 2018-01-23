import re

stopwords = []


def getStopWordsList(stopWordListFileName):
    # read the stopwords list file and make a list
    fp = open(stopWordListFileName, 'r')
    line = fp.readline()
    while line:
        word = line.strip()
        stopwords.append(word)
        line = fp.readline()
    fp.close()
    return stopwords


def getfeatureVector(tweet):
    featureVector = []
    stopwords = getStopWordsList('../src/TweetClassifier/stopwords.txt')
    for t in tweet:
        t = t.strip('\'"?,.')
        # print("Inside FE")
        # check if the word starts with an alphabet
        val = re.search(r"^[a-zA-Z][a-zA-Z0-9]*$", t)
        # ignore if it is a stopword
        if t in stopwords or val is None:
            continue
        else:
            # print(t)
            featureVector.append(t.lower())
    return featureVector
