from urllib import urlopen
url = ""
import nltk
import re
wordlist = [w for w in nltk.corpus.words.words('en') if w.islower()]