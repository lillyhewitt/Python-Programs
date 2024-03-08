#Credit
text = False

def creditChecker(n):
  creditSum = 0
  productSum = 0
  creditStr = str(n)
    numLen = len(creditStr)
    if numLen == 15:
      print("Number: " , n)
      print("American Express")
    elif numLen == 13:
      print("Number: " , n)
      print("VISA")
    elif numLen == 16:
      n /= 1000000000000000
      n = int(n)
      print("Number: " , n)
      if n == 4:
        print("VISA")
      else:
        print("MasterCard")
  else:
    print("Invalid Number")
  for i in range(numLen-2, -1, -2):
    value = 2 * (int(creditStr[i]))
    creditSum += (value)
    lenC = str(value)
    if lenC == 1:
      productSum += value
    else:
      productSum += value//10
      productSum += value % 10
  for i in range(numLen-1, -1, -2):
    productSum += int(creditStr[i])
  if productSum % 10 == 0:
    print("VALID")
  else:
    print("INVALID")
  print()
  
while not text:
  number = int(input("Enter card number: "))
  creditChecker(number)
  if number == "done":
    text = True
