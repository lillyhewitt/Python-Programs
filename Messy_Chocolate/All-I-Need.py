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
