#---------------------
# Tokenizer Functions
#---------------------

from nltk.tokenize import word_tokenize as english_word_tokenize
from hazm import word_tokenize as persian_word_tokenize

#Whitespace Tokenizer
def whitespace_tokenizer(text):
    tokens = text.split()
    return tokens

#English Tokenizer
def english_tokenizer(text):
    import nltk
    nltk.download('punkt')
    nltk.download('punkt_tab')
    tokens = english_word_tokenize(text)
    return tokens

# Persian Tokenizer
def persian_tokenizer(text):
    tokens = persian_word_tokenize(text)
    return tokens
#----------------------------------
