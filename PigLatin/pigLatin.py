#Lilly Hewitt - String Manipulation
def main():
  finished = False
  while not finished:
    word = input("Enter a word: ")
    word = word.lower()
    if word == "done":
      finished = True
    else:
      print(convertToPigLatin(word))

def findFirstVowel(word):
  index = 0
  for index, letter in enumerate(word):
    if letter in "aeiou":
      return index
  return len(word) - 1

def convertToPigLatin(word):
  index = findFirstVowel(word)
  if index == 0:
    return word[1:] + word[0] + "way"
  else:
    return word[index:] + word[:index] + "ay"

main()
