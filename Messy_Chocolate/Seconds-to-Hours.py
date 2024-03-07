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
