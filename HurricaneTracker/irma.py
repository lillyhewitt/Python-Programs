import turtle

def irma_setup():
  """Creates the Turtle and the Screen with the map background
  and coordinate system set to match latitude and longitude.
  :return: a tuple containing the Turtle and the Screen
  DO NOT CHANGE THE CODE IN THIS FUNCTION!
  """
  import tkinter
  turtle.setup(965, 600) # set size of window to size of map
  wn = turtle.Screen()
  wn.title("Hurricane Irma")
  # kludge to get the map shown as a background image,
  # since wn.bgpic does not allow you to position the image
  canvas = wn.getcanvas()
  turtle.setworldcoordinates(-90, 0, -17.66, 45) # set the coordinate system to
  match lat/long
  map_bg_img = tkinter.PhotoImage(file="images/atlantic-basin.png")
  # additional kludge for positioning the background image
  # when setworldcoordinates is used
  canvas.create_image(-1175, -580, anchor=tkinter.NW, image=map_bg_img)
  t = turtle.Turtle()
  wn.register_shape("images/hurricane.gif")
  t.shape("images/hurricane.gif")
  return (t, wn, map_bg_img)
def irma():
  """Animates the path of hurricane Irma
  """
  (t, wn, map_bg_img) = irma_setup()
  # your code to animate Irma here
  file = open("data/irma.csv", "r")
  text = file.readlines()
  t.penup()
  cat = ""
  lat = 0
  lon = 0
  wind = 0
  lines = []
  for line in text[1:]:
    lines +=([line.strip().split(",")])
  for parts in lines:
    lat = float(parts[2])
    lon = float(parts[3])
    wind = float(parts[4])
    t.goto(lon, lat)
    t.pendown()
    if wind >= 157:
      t.pensize(30)
      t.color("red")
      t.write("5", font = ("Times New Roman",(20)))
    elif wind >= 130:
      t.pensize(25)
      t.color("orange")
      t.write("4", font = ("Times New Roman",(20)))
    elif wind >= 111:
      t.pensize(20)
      t.color("yellow")
      t.write("3", font = ("Times New Roman",(20)))
    elif wind >= 96:
      t.pensize(15)
      t.color("green")
      t.write("2", font = ("Times New Roman",(20)))
    elif wind >= 74:
      t.pensize(10)
      t.color("blue")
      t.write("1", font = ("Times New Roman",(20)))
    else:
      t.pensize(5)
      t.color("white")
      t.goto(lon, lat)
  turtle.done()
  file.close()

if __name__ == "__main__":
  irma()
