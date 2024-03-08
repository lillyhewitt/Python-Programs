def numEvenDigits(number):
  digitCount = 0
  if number == 0:
    return 1
  if number < 0:
    number = number * -1
  while number != 0:
    lastDigit = number % 10
    if number %2 == 0:
      digitCount += 1
    number = number // 10
  return digitCount

