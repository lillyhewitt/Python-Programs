#Multiplication Table
def multiTable(n):
    count = 1
    for i in range(1,n+1):
        for j in range(1,n+1):
            print(j * i, end="\t")
        print()
value = int(input("Enter a number: "))

multiTable(value)
