'''
Task:
Create a regular expression pattern that can simultaneously match these words:

"Plans" | "Plank" | "plant" | "plane" using character classes
'''

# Import the necessary library
import re

# Change the pattern to match the words: "Plans","Plank","plant","plane"
pattern = r'[pP]lans|[pP]lank|[pP]lant|[pP]lane'

text = ["Plans", "Plank", "plant", "plane"]

for word in text:
    match = re.search(pattern, word)
    print(match)
