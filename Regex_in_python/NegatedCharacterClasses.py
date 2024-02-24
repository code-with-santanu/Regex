'''
Task: 
Create a regular expression pattern that matches words like "hog," "dog," "jog," "log," etc., but exclude the words "bog" and "tog".
 Utilize a negated character class to accomplish this "[^ ]"
'''
# Import the necessary library
import re


pattern = r"^[^bt].*"

text = ["hog", "dog", "jog", "bog", "log", "tog"]

for word in text:
    if re.search(pattern, word) != None:
        print(word + ": " + "matched ", re.search(pattern, word))
    else:
        print(word + ": " + "Not Matched ", re.search(pattern, word))
