"""
PROJECT 3; CHALLENGE A:
BY: Hunter Charvat

CHALLENGE SPECIFICATIONS:
---------------------------------------------------------------------
Using text2 from the nltk book corpa, create your own version of the
MadLib program.

Requirements:
1) Only use the first 150 tokens
2) Pick 5 parts of speech to prompt for, including nouns
3) Replace nouns 15% of the time, everything else 10%

Deliverables:
1) Print the orginal text (150 tokens)
2) Print the new text
---------------------------------------------------------------------

CITATIONS:
---------------------------------------------------------------------
(1): madlid_generatorp3.py by Jackie Cohen; with revisons from Paul Resnick and Colleen van Lent
        - Inspiration and source for this python-based, madlib generator.
        - https://github.com/cvanlent/SI206/blob/master/madlib_generatorP3.py
(2): stackoverflow users Senthil Kumaran & jamylak
        - how to convert a list to a string in Python
        - http://stackoverflow.com/questions/5618878/how-to-convert-list-to-string
---------------------------------------------------------------------
"""
print("START*******")
import nltk
import random
from nltk.book import *

tokens = text2[:150] # Requirement 1
print('\nCHALLENGE A\n---------------------------------------------------------------------\n')
print('***DELIVERABLE A***\n')
print(tokens, '\n') # Deliverable 1

"""
CODE RESULTS IN SAME VALUE AS SAMPLE ABOVE
---------------------------------------------------------------------
print(sample) #SAMPLE = TOKENS ABOVE
sample_s = ' '.join(sample_lis) #(2)
tokens = nltk.word_tokenize(sample_s)
print(tokens)
---------------------------------------------------------------------
"""

print('***DELIVERABLE B***\n') #(1)

tagged_tokens = nltk.pos_tag(tokens)
tagmap = {"NN":"a noun","NNS":"a plural noun","VB":"a verb","JJ":"an adjective","NNP":"a proper noun"}
substitution_probabilities = {"NN":.15,"NNS":.1,"VB":.1,"JJ":.1, "NNP":.1}

def spaced(word):
	if word in [",", ".", "?", "!", ":"]:
		return word
	else:
		return " " + word

final_words = []


for (word, tag) in tagged_tokens:
	if tag not in substitution_probabilities or random.random() > substitution_probabilities[tag]:
		final_words.append(spaced(word))
	else:
		new_word = input("Please enter %s:\n" % (tagmap[tag]))
		final_words.append(spaced(new_word))

print('\n')
print("".join(final_words))

print("\n\nEND*******")
