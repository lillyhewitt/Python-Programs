Download the StarterFiles.zip Download StarterFiles.zip, and unzip to the directory of your choice

Open the directory in PyCharm or IDLE. You will see a Python file named irma.py. In this file you will fill in the code to use the turtle module to create an animation of hurricane Irma's path. In the file are 2 functions, irma_setup and irma. You are NOT allowed to modify the irma_setup function. Your code is to be limited to the irma function.

In the irma_setup, the following are done for you:

Creating the screen and turtle
The turtle's shape is changed to that of a hurricane
Loading a background image of the Atlantic
Setting the world coordinates of the screen to match the latitude and longitude on the map
In the starter zip file there is a file named irma.csv in the data directory. This data was scraped from https://www.wunderground.com/hurricane/atlantic/2017/hurricane-irma,
last access 9/14/2017. This file contains data about hurricane Irma. Each line contains 6 columns separated by commas (thus the .csv file extension). The file can be opened directly in PyCharm or opened in Excel for a columnar view. The first line of the file describes what each column is. Here are the first 3 lines of the file, separated into their columns:

Date	Time	Lat	Lon	Wind	Pressure
30-Aug	15:00 GMT	16.4	-30.3	50	1004
30-Aug	21:00 GMT	16.4	-31.2	60	1001
The only columns relevant to your code are Lat (the latitude), Lon (the longitude), and Wind (the wind speed in miles per hour).

Using the data in irma.csv, your irma function must show hurricane Irma's path. Your solution must include the following:

Correctly show each point in the data file (together with lines between each point)
At each point, you must display what category the storm is, if it has hurricane strength winds, otherwise, draw no text.
Color code the hurricane strength:
Red for Category 5
Orange for Category 4
Yellow for Category 3
Green for Category 2
Blue for Category 1
White if not hurricane strength
The thickness of the line should change in proportion to the hurricane category.
