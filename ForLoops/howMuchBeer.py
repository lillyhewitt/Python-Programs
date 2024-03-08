#How Much Beer on the Wall
def howMuchBeer(beer):
    for i in range(beer, -1, -1):
        print(i, "bottles of beer on the wall," , i , "bottles of beer")
        print("Take one down, pass it around," , (i-1) , "bottles of beer on the wall")
beer = int(input("How many bottles of beer are there? "))

howMuchBeer(beer)
