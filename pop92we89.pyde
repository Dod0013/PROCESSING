x = 1
y = 1
img = 0
def setup():
    global img
    size(600,600)
    img = loadImage("Jota.png")
def draw():
    global x,y,img
    image(100,100,100)
    rect(x,y,200,100)
    x = x + 1
    y = y + 1
