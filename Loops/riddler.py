def riddler():
  for number in range(1001,10000,2):
    ones = number % 10
    tens = (number % 100) // 10
    huns = (number % 1000) // 100
    thos = number // 1000
    if ones != tens and ones != huns and ones != thos and tens != huns and tens
    != thos and huns != thos:
      if thos == tens * 3:
        if ones + tens + huns + thos == 27:
          print(number)
