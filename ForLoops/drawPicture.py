#3.1 Hourglass      
def drawHourglass():
    print("|\"\"\"\"\"\"\"\"\"\"|")
    n = 5
    m = 8
    for i in range(n):
        print(" " * (i+1), end="")
        print("\\" , end="")
        for j in range(m):
            print(":", end="")
        print("/")
        m -= 2
    print("     ||")
    m = 2
    for i in range(n):
        print(" " * (n-i), end="")
        print("\\" , end="")
        for j in range(2 ,m):
            print(":", end="")
        print("/")
        m += 2
    print("|\"\"\"\"\"\"\"\"\"\"|")
  
drawHourglass()

#3.2 Slash Figure 22
def drawSlash(n):
    initialSlash = 0
    initial = 2 + (4 * (n-1))
    for i in range(1, n+1):
        print("\\" * initialSlash, end="")
        print("!" * initial, end="")
        print("/" * initialSlash, end="")
        print("")
        initialSlash += 2
        initial -= 4
      
drawSlash(4)    
