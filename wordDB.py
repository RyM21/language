# wordDB.py
# Word Frequency Database Generator
# Author: Ryan McCarl
# License: GPL 3

import sqlite3
from sqlite3 import connect
import nltk as n
from nltk.corpus import brown
from nltk.stem import WordNetLemmatizer as wordnet

    

def makeDb(lang):
    dbName = str(r"C:\PythonDatabases\%s.db" % lang)
    print(dbName)
    
def connectDb(dbName)
    conn = sqlite3.connect(dbName)
    c = conn.cursor()
    return c, dbName

def makeTables():
    c.execute(
    "CREATE TABLE IF NOT EXISTS " + lang + "(id, freqRank, lemma)")
    prefix = "INSERT INTO " + lang + " values "
    testWord = "Hello" # for debugging
    c.execute(prefix + r"1,  1, testWord") 
    c.fetchone().print() # for debugging)
    
def getCorpus():
    global corpus = "brown"
    return corpus

def GetFreq(corpus):
    global FreqList = []
    words = corpus.words().decode('utf-8')
    freqList = n.FreqDist(w.lower() for w in words)
    freqList = freq.most_common(500) # Get list of the 500 most common words
    # print(freqList) # for debugging
    return FreqList

def main(): 
    lang = input("What language would you like to create a database for?\n")
    makeDb(lang)
    makeTables(c)
    # getCorpus()
    # getFreq()

main()
