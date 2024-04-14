"""
Question (1):
Write a python program that take an input text from the user and tokenize the text itnto sentences using languages
other than English using spacy library.
"""

import spacy

# Load the spaCy Arabic model
nlp = spacy.load("xx_ent_wiki_sm")  # "xx_ent_wiki_sm" is the language code for Arabic
nlp.add_pipe("sentencizer")

# Get input text from the user
text = input("Enter the text in Arabic: ")

# Process the text using the spaCy Arabic model
doc = nlp(text)

# Extract sentences from the processed text
sentences = [sent.text for sent in doc.sents]

# Display the tokenized sentences
print(sentences)

"""
Question (2):
Write a python program that take an input text from the user and apply part-of-speech tagging, 
and return back correct tags per word.
Note: use two different tagset and compare the output.
"""

import nltk
from nltk.tokenize import word_tokenize

# Get input text from the user
text = input("Enter the text: ")

# Tokenize the text
tokens = word_tokenize(text)

# Perform part-of-speech tagging with Universal POS tags
pos_tags_universal = nltk.pos_tag(tokens, tagset="universal")

# Perform part-of-speech tagging with Penn Treebank POS tags
pos_tags_treebank = nltk.pos_tag(tokens)

# Display the tagged words for both tagsets
print("Tagged words with Universal POS tags:")
print(pos_tags_universal)

print("\nTagged words with Penn Treebank POS tags:")
print(pos_tags_treebank)


"""
Question (3): Write a Python NLTK program to get a list of common stop words in various languages in Python.
"""
import nltk

# Download NLTK stopwords corpus
nltk.download("stopwords")

# Get a list of common stop words for various languages
languages = [
    "english",
    "spanish",
    "french",
    "german",
    "italian",
    "dutch",
    "portuguese",
    "russian",
    "arabic",
    "swedish",
]
stopwords_lists = {}

for lang in languages:
    stopwords_lists[lang] = nltk.corpus.stopwords.words(lang)

# Display the list of common stop words for each language
for lang, stopwords_list in stopwords_lists.items():
    print(f"Stop words in {lang.capitalize()}:")
    print(stopwords_list[:10])  # Display the first 10 stop words
    print(f"Total number of stop words: {len(stopwords_list)}\n")
