#Summation of Squares
def sumSquares(n):
    total = 0
    for i in range(1,n+1):
        print(i , "^ 2 +" , end=" ")
        total = total + (i ** 2)
    print("=" , total)
squares = int(input("Enter an integer: "))
sumSquares(squares)
