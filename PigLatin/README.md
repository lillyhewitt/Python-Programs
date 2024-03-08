Abstract
The object of this programming assignment is to gain familiarity with
writing static functions and manipulating String objects.
Read all the directions to succeed!

1 Objective
Your goal is to write a program that allows a user to input words and see them
transformed into their Pig Latin form. We will be using simplified rules for Pig
Latin.
You’ll run your program, which will prompt the user to input words. When
the user inputs a word and hits enter, the system will print out the word trans-
formed into Pig Latin, then maybe some extra credit stuff. The program will
repeat doing this (eg use a while loop) until the user types in the string done.
The following is the console from my code. Your code should produce identical
output when the same inputs are used.
letter
etterlay
foo
oofay
bar
arbay
spam
amspay
eggs
ggseway
Andrew
ndrewaway
Alakazam
lakazamaway
Charizard
arizardchay
done
When I start by typing in “letter” and then press enter, the program prints
“etterlay”. The program terminates when I input “done”.
But how do I know how to transform stuff into Pig Latin? Read on!

2 How To Do it, or the Part Where I Give You Hints
Write a program called StringManipulation that contains the functions in the
list below. Think about how you can combine each of these pieces, how each
function can call one another to do what you need to do. This will require some
reading about Strings in the book.
• The main function. The main function runs a loop, asking the user to
input a word. Covert your input to lowercase. The program prints out
the input converted to Pig Latin and the input reversed. If the input is
“done”, the loop stops and the program ends.
• findFirstVowel, which takes in a String and returns an int. The re-
turned int is the location of the first vowel in the String. If there is no
vowel, just return the index of last character of the String. This function
is essential to helping you with convertToPigLatin. How? Read on!
• convertToPigLatin, which takes in a String and returns a String. The re-
turned String is the Pig Latin form of the input word. A word is converted
to Pig Latin via the following mutually exclusive rules:
– If the word starts with a vowel, move the vowel to the end of the
word and additionally add “way” to the end of the word.
– Otherwise move all the letters before the first vowel to the end of the
word and additionally add “ay” to the end of the word.
If there is no vowel, just return the string completely unchanged. Think
about how findFirstVowel can tell you which rule to use.

3 More Hints
Here are some things to keep in mind:
1. ‘y’ is not a vowel.
2. Check your program against the examples above!
3. String has a bunch of functions that make your life easier. For example,
toLowercase and slicing are needed to write the program.
4. https://docs.python.org/3/library/string.html has everything you
would need to know about String functions. Your book will help too.
5. String concatenation, or “adding” two Strings with the + sign will help.

Extra Credit: Reverse (3 points)
Write and call an additional function called reverse. reverse which takes in
a String and returns the mirror-image of the String, so the first letter is now
the last, the second is now second to last, and so on. If you do this, the above
input should look like:
letter
etterlay
rettel
foo
oofay
oof
bar
arbay
rab
spam
amspay
maps
eggs
ggseway
sgge
Andrew
ndrewaway
werdna
Alakazam
lakazamaway
mazakala
Charizard
arizardchay
drazirahc
done

Extra Credit: ROT13 (7 points)
Write an additional function that encrypts the input using ROT13. Details
here: http://en.wikipedia.org/wiki/ROT13
