
Messy Chocolate

Complete each of the four following parts as separate Python programs.

1. Chocolate is All I Need
The Harris-Benedict equation estimates the number of calories your body
needs to maintain your weight if you do no exercise. This is called your basal
metabolic rate, or BMR. The formula for the calories needed for a woman
to maintain her weight is:

BM R = 655.1 + (4.35 · weight) + (4.7 · height) − (4.7 · age)

The formula for the calories needed for a man to maintain his weight is

BM R = 66 + (6.2 · weight) + (12.7 · height) − (6.76 · age)

A typical chocolate bar contains 214 calories. Write a program that
allows the user to input weight in pounds, height in inches, age in years.
The program should then output the number of chocolate bars that should
be consumed to maintain one’s weight for person of the input height, weight,
and age for both a male and a female. You don’t need to ask for the
user’s gender, as we haven’t learned if statements yet. Again, print out
the result of both equations and be sure to print which is which.

2. Debug My Messy Code
Create a python file called Messy.py. Copy and paste the following code
in there and correct the errors so that it will run. Please also format it make
it readable. The code should output 139.0 when 12 is entered.

def main():
  print(’It’s time to go on a scavenger hunt!’’)
  print("You"d be amazed how many things can go wrong!")
  print(’Please enter how long you want to travel for:’)
  initialPos = 7.0;
  time = float(input());
  velocity == 5.0;
  acceleration = 1.0;
  # there is a math error in here causing
  # an incorrect answer in the line below
  position = initialPos + velocity * time + (1 // 2) *acceleration*time*time;
  #if you are stuck on the math error, look at the footnote
  print(position);

main()

3. Temperature
Write a program that converts a temperature from Celsius to Fahrenheit.
It should (1) prompt the user for input, (2) read a floating point value from
the keyboard, and (3) calculate the result.
Here is the formula. Be careful not to use integer division!
F = C × 9
5 + 32

4.  Seconds to Hours
Write a program that converts a total number of seconds to hours, minutes,
and seconds. It should (1) prompt the user for input, (2) read an integer from
the keyboard, (3) and calculate the result. For example, "5000 seconds = 1 hours, 23 minutes, and 20 seconds".
Hint: Use the modulus operator.
