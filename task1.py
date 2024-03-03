'''
1- Write a python program than takes a text from a user and ask the user to choose one of three choices:
Choice number 1: print tokenized words
Choice number 2: print tokenized sentences
Choice number 3: print output using split function.
'''

import nltk 
from nltk.tokenize import word_tokenize, sent_tokenize

text = input('Enter text you want to tokenize: \n')
choice = int(input('Choose tokeniztion method:\n1-Word tokenization\n2-Sentence tokenization\n3-Split function\nEnter number of your choice: '))

if choice == 1 :
    tokens = word_tokenize(text)
elif choice == 2 :
    tokens = sent_tokenize(text)
elif choice == 3 : 
    tokens = text.split()
else :
    print('Please enter a valid choice')

print(tokens)