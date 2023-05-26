x = 1
y = 1
x1 = 500
y1 = 1
img = 0
def setup():
    global img
    size(600,600)
    img = loadImage("Jota.png")
def draw():
    background(random(5,158))
    global x,y,img,x1,y1
    #image(200,200,200)
    fill(random(0,4))
    rect(x,y,200,100)
    fill(random(255,0))
    rect(x1,y1,200,100)
    x = x + 1
    y = y + 1
    x1 = x1 - 1
    y1 = y1 + 1
