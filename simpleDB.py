#!/usr/bin/env python
# simpleDB.py
# Simple SQLite3 database creator
# Author: Ryan McCarl
# License: GPL 3

import sqlite3

def make_db_path(lang):
    db_name = r"C:\PythonDatabases\%s.db" % lang
    return db_name

def connect_db(db_name):
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    return c