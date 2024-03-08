def numVowels(text):
  vowelCount = 0
  #listOfVowels = ["a","e","i","o","u"]
  vowels = "aeiou"
  for letter in text:
    if letter in vowels:
      vowelCount = vowelCount + 1
  return vowelCount
