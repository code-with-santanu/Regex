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

3. `Anchors :` Anchors or sprecial characters allow you to match any character.

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
