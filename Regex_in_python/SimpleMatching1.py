'''
Task:
To locate the character or word you're searching for, just type it directly, much like a regular search. For instance, if you're looking for the word curious in the text, enter it exactly as is.  
'''

# Import the necessary library
import re

text = "I have no special talents.I am only passionately curious."

# Use search function to search for the literal word "curious"
match = re.search(r"curious", text)

# Printing match
print(match)
