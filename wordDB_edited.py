#!/usr/bin/env python2
# wordDB.py
# Word Frequency Database Generator
# Author: Ryan McCarl
# License: GPL 3

import sqlite3
import nltk as n
from nltk.corpus import brown
from nltk.stem import WordNetLemmatizer as wordnet


corpus = []
table_name = "frequencies"

def makeDbPath(lang):
    dbName = r"C:\PythonDatabases\%s.db" % lang
    return dbName

def connectDb(dbName):
    conn = sqlite3.connect(dbName)
    c = conn.cursor()
    return c

def makeTables(c, lang):
    c.execute(
        "CREATE TABLE IF NOT EXISTS " + table_name + " " +
        "(id INTEGER PRIMARY KEY, freqRank INTEGER, lemma TEXT)"
    )
    query = "INSERT INTO " + table_name + " VALUES (?, ?, ?)"
    testWord = "Hello" # for debugging
    values = (1, 1, testWord)
    c.execute(query, values)
    # c.fetchone().print() # for debugging)

def insert_into_frequencies(c, words_info):
    query = "INSERT INTO {} (lemma, freqRank) VALUES (?, ?)".format(table_name)
    c.executemany(query, words_info)

def loadCorpus():
    global corpus
    corpus = n.corpus.brown

def GetFreq(corpus):
    # global FreqList = []
    words = corpus.words()
    freqList = n.FreqDist(w.lower() for w in words)
    print(freqList)
    freqList = freqList.most_common(10) # Get list of the 500 most common words
    # print(freqList) # for debugging
    return freqList

def main(): 
    lang = raw_input("What language would you like to create a database for?\n")
    # lang = 'eng'
    loadCorpus()
    db_path = makeDbPath(lang)
    cursor = connectDb(db_path)
    makeTables(cursor, lang)

    most_common = GetFreq(corpus)
    insert_into_frequencies(cursor, most_common)
    cursor.execute('SELECT * FROM {}'.format(table_name))
    print(cursor.fetchall())

    cursor.close()

main()
