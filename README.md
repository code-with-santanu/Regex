<h1 align="center">REGEX (Regular Expression)
</h1>

- Regular Expression, also known as regex is a sequence of characters that defines a search pattern.

<h2 align="center">Some Common type of pattern of regex</h2>

1. `Literal Character :` Literal characters are most common types of pattern that can be matched by regex.

   Ex: Pattern= _"**hello**"_

   Text= _Say **hello** to everyone_

2. `Character Classes :` Character classes allow you to match a set of characters.

   Ex: Pattern= _"**[abc]**"_

   Text= _**a**,**b**,**c**_

3. `Anchors :` Anchors(^ and $) or special characters allow you to match any character.

   Ex1: Pattern= _"**.**"_

   Text= _**any character**_

   Ex2: Pattern= _"**^u**"_

   Text= _**u**nique_

   Ex3: Pattern= _"**e$**"_

   Text= _uniqu**e**_

4. `Quantifiers :` Quantifiers allow you to match the specific number of occurance of character.

   Ex: Pattern= _"**a{3}**"_

   Text= _d**aaa**bd_

5. `Alteration :` Alteration allow you to match one pattern or another.

   Ex: Pattern= _"**cat | dog**"_

   Text1= _There is a **dog** behind the tree_

   Text2= _The **cat** is a very adorable animal_

   Text3= _The **cat** chased the playful **dog** around the garden_

---

<h2 align="center">Some Predefined Metacharacters & Alteration</h2>

```
'[abcde]'               : Matches any one of the specified characters.
'[^abcde]'              : Matches any character except the ones specified. It's a negated  character class.


'\d' or  [0-9]          : Matches any digit (0-9).
'\D' or  [^0-9]         : Matches any non-digit character.
'\w' or  [A-Za-z0-9_]   : Matches any alphanumeric including underscore(_)
'\W' or  [^A-Za-z0-9_]  : Matches any non-alphanumeric character excluding underscore(_).
'\s'                    : Matches any whitespace character (spaces, tabs, newlines).
'\S'                    : Matches any non-whitespace character.


'.'                     : Matches any character except a newline.
'^'                     : Anchors the regex at the start of the string.
'$'                     : Anchors the regex at the end of the string.


'a{3}'                  : Matches exactly three consecutive 'a' characters.
'a?'                    : Matches zero or one occurrence of 'a'.
'a+'                    : Matches one or more occurrences of 'a'.
'a*'                    : Matches zero or more occurrences of 'a'.
'(abc)'                 : Groups the characters 'abc' together.
'a|b'                   : Matches either 'a' or 'b'.


'\'                     : Escapes special characters, allowing you to match them literally.
'\b'                    : Matches the string only at a word boundary. Ex1: \bstring\b  Ex2: \b(cat | dog)\b
'\B'                    : Matches the string with more boundary boundary. Ex1: \bstring\b  Ex2: \b(cat | dog)\b


'(?i)case-insensitive'  : Performs a case-insensitive match.
```

---

<h2>Regex in Python</h2>

<p>There is a python built-in module that helps to deal with regex.</p>

Module name: `re`

### Usage:

- To use the module, first install the module using:

```
pip install re
```

- Import the module to your python file:

```
import re
```

- In `re` module offers some methods that are used to find the matching pattern

  1. **findall( pattern, text )** : Returns a list containing all matches

  2. **search( pattern, text, re.IGNORECASE<sub>optional</sub>)** : Returns a Match object if there is a match anywhere in the string. re.IGNORECASE is used to search the pattern of both lower and upper case.

  3. **split( pattern, text, occurrence<sub>optional</sub>)** : Returns a list where the string has been split at each match

  4. **sub( pattern, replace_pattern, text, occurrence<sub>optional</sub>)** : Replaces one or many matches with a string
