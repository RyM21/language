#!/usr/bin/env python2
import nltk
from pprint import pprint
import sys

class A:

    def f(self):
        pass

    def g(self):
        self.f()

a = A()
a.g()

sys.exit(0)

corpus = []

def loadCorpus():
    global corpus
    corpus = nltk.corpus.brown.words()
    # corpus = [x.decode('utf-8') for x in nltk.corpus.brown.words()]

loadCorpus()
frequencies = nltk.FreqDist(corpus)
most_common = frequencies.most_common(10)
pprint(most_common)
