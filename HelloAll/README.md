1 Part 1
For this assignment you will install Python on your machine and ensure it
is working by writing a basic program in IDLE. Be sure to install Python 3.
Refer to the video on canvas if you need directions. Create a new Python
file called hello.py.

Your program must print out a short ( 3 sentences) biography about a
famous computer scientist who is not Turing, Gates, or Jobs.1 Print out
each sentence on a separate line.
For reference, here is the hello world program below.
print("hello, world!")

If you can successfully complete this task, have your program then ask
the user if they had heard of this person before and read in their input, then
print “They are pretty cool, aren’t they.” no matter what the user puts in.

1.1 Reading text from the user
You can get text from the user by using the input() function. Think of
it as the reverse of the print(). If you put a string inside of input(), it
will display that string and wait for the user to input something. You can
then store what the user inputs.
Here’s an example
text = input("Tell me a secret: ")
print("Your secret was: ")
print(text)
print("Whoops. I’m not good at keeping secrets...")
That would display "Tell me a secret" to the user, who would
then input a string. Try saving this in a program and trying it out.

2 Part 2
The purpose of this assignment is that you start to become comfortable
with a Python programming environment, and to practice with the print()
function.
Write a Python program, which when run, produces a simple drawing by
making multiple calls to Python’s print() function.

Drawings such as these, which produce pictures using simple text are
called ASCII art. There are some amazing examples to be found online, but
for this assignment, feel free to be creative or as non-creative as you’d like.
One thing to be careful about is that in order to print certain special
characters to the screen (what programmers call escape sequences), we use
the backslash character, \. You won’t need to use any of these escape
sequences in your program, and we will learn their use later in the semester.
The only thing that you need to keep in mind for this assignment is that
in order to produce the \character in your drawing, you need to write two
consecutive backslashes in your print function. You can see this done in the
car’s windshield and headlights.


