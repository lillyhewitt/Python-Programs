#Lilly Hewitt
#Mario
def mario(n):
  initialS = n - 1
  for i in range(1, n+1):
    print(" " * initialS, end="")
    print("#" * i, end="")
    print(" ", end ="")
    print("#" * i, end="")
    print(" " * initialS, end="")
    print("")
    initialS -= 1
  
value = False
while not value:
  text = int(input("Enter a height: "))
  if 0 < text < 9:
    value = True
    
mario(text)
print()
