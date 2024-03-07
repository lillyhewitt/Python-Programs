#Lilly Hewitt
print("Welcome, this program will state the exact number of chocolate bars you must
consume to maintain your weight.")
candy = 214;
weight = int(input("First, please input your weight in pounds: "))
height = int(input("Next, input your height in inches: "))
age = int(input("Finally, input your age in years: "))
BMRw = 655.1 + (4.35 * weight) + (4.7 * height) - (4.7 * age)
barsF = BMRw / candy
BMRm = 66 + (6.2 * weight) + (12.7 * height) - (6.76 * age)
barsM = BMRm / candy
print("\nFemale BMR =",BMRw , "\nYou must consume", round(barsF,2) , "bars to
maintain your weight.")
print("\nMale BMR =",BMRm , "\nYou must consume", round(barsM,2) , "bars to
maintain your weight.")

print(" ")
def main():
print("Welcome to Debug My Messy Code\nIt’s time to go on a scavenger hunt!")
print("You'd be amazed how many things can go wrong!")
print("Please enter how long you want to travel for: ")
initialPos = 7.0
time = float(input())
velocity = 5.0
acceleration = 1.0
position = initialPos + velocity * time + (1 / 2) *acceleration * time * time
print(position)

main()
print(" ")
print("Welccome to the Celsius to Fahrenheit converter!")
tempC = float(input("Please enter a temperature in Celsius: "))
tempF = (tempC * (9/5) + 32)
print(tempF , " degrees in Fahrenheit")

print(" ")
print("Welcome to the Seconds to Hours Converter!")
total = int(input("Enter the total number of second: "))
intial = total
hour = round(total / 3600)
total %= 3600
minutes = round(total / 60)
total %= 60
print(intial , " seconds =" , hour , "hour(s)," , minutes , "minutes, and" ,
total , "seconds.")
