#Lilly Hewitt
value = False
badWords = ["N", "NO"]
goodWords = ["Y", "YES"]
text = ""

def checkText(text):
  newText = ""
  temp = ""
  valid = True
  textLen = len(text)
  c = 0
  validChars = [ "a", "e", "i", "o", "u", "p", "k", "h", "l", "m", "n", "w"]
  unvalidChar = ""
  hawaiianSounds = {"a": "ah", "e":"eh", "i":"ee", "o":"oh", "u":"oo",
  "p":"p", "k":"k", "h":"h", "l":"l", "m":"m",
  "n":"n", "w":"w"}
  hawaiianSpecials = { "ai":"eye", "ae":"eye", "ao":"ow", "au":"ow", "ei":"ay",
  "eu":"eh-oo", "iu":"ew", "oi":"oyo", "ou":"ow",
  "ui":"ooey", "iw":"v", "ew":"v", "uw":"w", "ow":"w"}
  for char in text:
    if char not in validChars:
      value = True
      valid = False
      unvalidChar = char
  if valid:
    while c < textLen:
      char = text[c]
      if c < textLen-1 and char in validChars[:5]:
        temp = char + text[c+1]
        if temp in hawaiianSpecials:
          if text[c+1] == "w" or text[c+1] == "v":
            newText += hawaiianSounds[char] + "-"
          if (c < textLen-2 and text[c+2] == " ") or (temp == "iw" or temp == "ew" or temp == "uw" or temp == "ow") or (c == textLen-2):
            newText += hawaiianSpecials[temp]
          else:
            newText += hawaiianSpecials[temp] + "-"
          c += 1
        else:
          if (c < textLen-1 and text[c+1] == " ") or c == textLen:
            newText += hawaiianSounds[char]
          else:
            newText += hawaiianSounds[char] + "-"
      elif char == " " or char == "'":
        newText += char
      else:
        newText += hawaiianSounds[char]
      c += 1
    print(text.capitalize(), "is pronounced" , newText.capitalize())
  else:
    print(unvalidChar.capitalize() , "is not a valid hawaiian character.")
    
while value == False:
  text = input("\nEnter a Hawaiian word to pronounce:\t")
  text = text.lower()
  checkText(text)
  playAgain = input("\nDo you want to enter another word? Y/YES/N/NO.\t")
  if playAgain in badWords:
    value = True
  if playAgain not in badWords and playAgain not in goodWords:
    print("Input is invalid.")
    playAgain = input("\nDo you want to enter another word? Y/YES/N/NO.\t")
  else:
    value = False
