def isArmstrongNumber(number):
  ones = number % 10
  tens = (number % 100) // 10
  huns = number // 100
  return (ones**3 + tens**3 + huns**3) == number
