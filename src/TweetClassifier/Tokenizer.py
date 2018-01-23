# Text pre-processing
import json
import re  # used for tockenizing the tweet

emoticons_str = r"""
				(?:
					[:=;] #Eyes
					[oO\-]? #Nose
					[D\)\]\(\]/\\OpP] # Mouth
				)"""
regex_str = [
    emoticons_str,
    r'<[^>]+>',  # HTML Tags
    r'(?:@[\w_]+)',  # @-mentions
    r"(?:\#+[\w_]+[\w\'_\-]*[\w_]+)",  # Hashtags
    r'http[s]?://(?:[a-z]|[0-9]|[$-_@.&amp;+]|[!*\(\),]|(?:%[0-9a-f][0-9a-f]))+',  # URLs
    r'(?:(?:\d+,?)+(?:\.?\d+)?)',  # numbers
    r"(?:[a-z][a-z'\-_]+[a-z])",  # words with - and '
    r'(?:[\w_]+)',  # other words
    r'(?:\S)'  # anything else
]

tokens_re = re.compile(r'(' + '|'.join(regex_str) + ')', re.VERBOSE | re.IGNORECASE)
emoticon_re = re.compile(r'^' + emoticons_str + '$', re.VERBOSE | re.IGNORECASE)


def tokenize(s):
    return tokens_re.findall(s)


def preprocess(s, lowercase=False):
    tokens = tokenize(s)
    if lowercase:
        tokens = [token if emoticon_re.search(token) else token.lower() for token in tokens]
    return tokens


sample_tweet = 'Never knew Glorious by Macklemore official music video was this sweet.😭'  # 'RT @imHarishRaman: just an example! :D http://example.com #NLP'
print(preprocess(sample_tweet))
