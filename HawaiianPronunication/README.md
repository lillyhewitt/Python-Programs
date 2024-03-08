1 Hawaiian Words
Hawaiian words can be intimidating to attempt to pronounce. Words like hu-
muhumunukunukuapua’a look like someone may have fallen asleep on the key-
board. The language is actually very simple and only contains 12 characters; 5
vowels and 7 consonants. We are going to write a program that allows the user
to enter a hawaiian word and give the pronunciation of the word or words as
output.

For instance, humuhumunukunukuapua’a phonetic guide would be Hoo-moo-
hoo-moo-noo-koo-noo-koo-ah-poo-ah’ah.
The 12 valid characters in the Hawaiian language are a, e, i, o, u, p, k, h, l,
m, n, and w. Let’s learn more about these characters and the way it works.

1.1 Consonants
Consonants are fairly easy to understand. The only exception with consonants
are w’s, which can be pronounced as a ‘w’ or a ‘v’ sound.
p, k, h, l, m, n Pronounced like the english ver-
sions.
w -start of word Either pronounced as a w or a v
sound. We shall pronounce it as
a w sound.
w -after the letter ‘a’ Either pronounced as a w or a v
sound. We shall pronounce it as
a w sound.
w -after ‘i’ or ‘e’ Pronounced as a v sound.
w -after ‘u’ or ‘o’ Pronounced as a w sound.

1.2 Vowels
Basic vowels are also straightforward.

a sounds like ah. eg. Austin -ah-stin
e sounds like eh. eg. egg -eh-gg
i sounds like ee eg. bee
o sounds like oh eg. obey -oh bay
u sounds like oo eg. mood -m oo d
With these rules we create a guide for some simple Hawaiian words. For
instance, aloha would be pronounced as Ah-loh-hah.

1.3 The Catch
Naturally, there’s a bit of a catch. We could just use the replace method to
replace all a’s with ah, all e’s with eh, and so on. Very few things are ever quite
that easy. In a more complex word with many vowels grouped together there
are additional rules.
ai sounds like eye. eg. Ice
ae sounds like eye. Same as ai
ao sounds like ow. eg. How
au Sounds like ow. eg. House.
ei Sounds like ay. eg. Hay
eu Sounds like eh-oo
iu Sounds like ew
oi Sounds like oyo
ou Sounds like ow.
ui Sounds like ooey. Like gooey
The word keiki means child in Hawaiian. The “ei” isn’t pronounced as
separate vowels, but would be pronounced as ay. Kieki sounds like kay-kee.
The island of Maui would be pronounced as MOW-EE.
You’ll notice that all groupings of vowels aren’t represented. For instance
there is no combination for “oa” in a word. In cases like this, each vowel is
pronounced as individual vowel sounds. From the vowel sounds ‘o’ is pronounced
as oh and ‘a’ as ah. So oa would sound like oh-ah. The hawaiian word “Hoaloha”
means friend and would be pronounced as Hoh-ah-loh-hah.
There are words with more than 2 vowels in a row. These are approached
in the same way. If “aia” is in a word, the “ai” would be said like eye. Then
the a would be pronounced as ah. Thus, “aia” sounds like eye-ah. Kaiapuni is
the Hawaiian word for environment and is pronounced Keye-ah-poo-nee.
If there are more than 2 vowels in a row and the first 2 do not have a single
sound, then you would say the first vowel normally, and then check to see if
vowel 2 and 3 have a combined sound. The ua in Huaai does not have a sound.
So you’d just pronounced the u as oo, and then evaluate the aa. Since there is
no sound for aa, you’d just pronounced the first a as ah, and then evaluate ai.
The ai is said like eye. So the word would be said as Hoo-ah-eye.For simplicity
we will ignore accents in words.  ̄a or ˆa is simply an a.

2 Requirements
• The program should validate that the word given by the user only has
valid Hawaiian characters. Spaces and the apostrophe (’) are valid as
well.
• If a word is not valid, warn the user about offending characters and prompt
for a hawaiian word again.
• Spaces are breaks for words and should be kept intact.
• The apostrophe is a hard stop, and should be kept in the word. A word
with a’i is pronounced ah’ee.
• Without the apostrophe it would be eye.
• Ask the user if they want to do another word. Valid responses are Y, YES,
N or NO. If they want to play more, then they can enter another hawaiian
word. If no, then the program ends.

3 Notes
• You won’t be able to just use the .replace() method. You’ll need to eval-
uate the the characters entered one at a time according to the rules.
• Using .upper() or .lower() will change all the characters to the given case.
This will make comparisons easier.
• Using .capitalize() will capitalize the first character in each word. This
will make for a nice output.

4 Example
Enter a hawaiian word to pronounce ==> invalid
V is not a valid hawaiian character
Enter a hawaiian word to pronounce ==> aloha
ALOHA is pronounced Ah-loh-hah
Do you want to enter another word? Y/YES/N/NO ==> humuhumunukunukuapua’a
Enter Y, YES, N or NO
Do you want to enter another word? Y/YES/N/NO ==> y
Enter a hawaiian word to pronounce ==> Kakahiaka
KAKAHIAKA is pronounced Kah-kah-hee-ah-kah
Do you want to enter another word? Y/YES/N/NO ==> y
Enter a hawaiian word to pronounce ==> Mahalo
MAHALO is pronounced Mah-hah-loh
Do you want to enter another word? Y/YES/N/NO ==> y
Enter a hawaiian word to pronounce ==> E komo mai
E KOMO MAI is pronounced Eh koh-moh meye
Do you want to enter another word? Y/YES/N/NO ==> y
Enter a hawaiian word to pronounce ==> maui
MAUI is pronounced Mow-ee
Do you want to enter another word? Y/YES/N/NO ==> y
Enter a hawaiian word to pronounce ==> kane
KANE is pronounced Kah-neh
Do you want to enter another word? Y/YES/N/NO ==> y
Enter a hawaiian word to pronounce ==> HOALOHA
HOALOHA is pronounced Hoh-ah-loh-hah
Do you want to enter another word? Y/YES/N/NO ==> y
Enter a hawaiian word to pronounce ==> makua
MAKUA is pronounced Mah-koo-ah
Do you want to enter another word? Y/YES/N/NO ==> y
Enter a hawaiian word to pronounce ==> keikikane
KEIKIKANE is pronounced Kay-kee-kah-neh
Do you want to enter another word? Y/YES/N/NO ==> y
Enter a hawaiian word to pronounce ==> humuhumunukunukuapua’a
HUMUHUMUNUKUNUKUAPUA’A is pronounced Hoo-moo-hoo-moo-noo-koo-noo-koo-ah-poo-ah’ah
Do you want to enter another word? Y/YES/N/NO ==> y
Enter a hawaiian word to pronounce ==> keiki
KEIKI is pronounced Kay-kee
Do you want to enter another word? Y/YES/N/NO ==> y
Enter a hawaiian word to pronounce ==> Hoaloha
HOALOHA is pronounced Hoh-ah-loh-hah
Do you want to enter another word? Y/YES/N/NO ==> y
Enter a hawaiian word to pronounce ==> kaiapuni
KAIAPUNI is pronounced Keye-ah-poo-nee
Do you want to enter another word? Y/YES/N/NO ==> y
Enter a hawaiian word to pronounce ==> wahine
WAHINE is pronounced Wah-hee-neh
Do you want to enter another word? Y/YES/N/NO ==> y
Enter a hawaiian word to pronounce ==> iwa
IWA is pronounced Ee-vah
Do you want to enter another word? Y/YES/N/NO ==> y
Enter a hawaiian word to pronounce ==> Huaai
HUAAI is pronounced Hoo-ah-eye
Do you want to enter another word? Y/YES/N/NO ==> n


5 References
http://www.oocities.org/olelo.geo/o-pronunciation.html#f http://www.
to-hawaii.com/hawaiian-dictionary.php

