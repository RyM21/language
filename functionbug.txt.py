Python 3.5.1 (v3.5.1:37a07cee5969, Dec  6 2015, 01:38:48) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import nltk as n, sqlite3
>>> from n.corpus import brown
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    from n.corpus import brown
ImportError: No module named 'n'
>>> clear
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    clear
NameError: name 'clear' is not defined
>>> from nltk.corpus import brown
>>> from nltk.stem import WordNetLemmatizer as wordnet
>>> def load_corpus():
	global corpus
	corpus = n.corpus.brown
print corpus
SyntaxError: Missing parentheses in call to 'print'
>>> print(corpus)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    print(corpus)
NameError: name 'corpus' is not defined
>>> load_corppus
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    load_corppus
NameError: name 'load_corppus' is not defined
>>> load_corpus()
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    load_corpus()
NameError: name 'load_corpus' is not defined
>>> 
>>> 
>>> load_corpus()
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    load_corpus()
NameError: name 'load_corpus' is not defined
>>> def load_corpus():
	global corpus
	corpus = n.corpus.brown

	
>>> load_corpus; print corpus
SyntaxError: invalid syntax
>>> load_corpus; print(corpus)
<function load_corpus at 0x04873E40>
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    load_corpus; print(corpus)
NameError: name 'corpus' is not defined
>>> print(corpus)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    print(corpus)
NameError: name 'corpus' is not defined
>>> load_corpus
<function load_corpus at 0x04873E40>
>>> print(corpus)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    print(corpus)
NameError: name 'corpus' is not defined
>>> corpus
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    corpus
NameError: name 'corpus' is not defined
>>> def load_corpus():
	global corpus
	corpus = n.corpus.brown
	return corpus

>>> print(corpus)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    print(corpus)
NameError: name 'corpus' is not defined
>>> corpus
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    corpus
NameError: name 'corpus' is not defined
>>> 
