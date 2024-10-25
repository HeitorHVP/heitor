
def setup():
    fullScreen()

x = 0
y = 0

def draw():
    global x
    global y 
    
    # rect(x, y, largura altura)
    # ellipse(x, y, largura altura)
    # line(x1, y1, x2, y2)
    # fill(RED, GREEN, BLUE)
    fill(255, 243, 0)
    rect(500, 200, 200, 200)
    fill(255, 255, 255)
    ellipse(550, 250, 50, 50)
    ellipse(550, 350, 50, 50)
    fill(255,3,3)
    rect(650, 250, 10, 100)
    fill(3, 3, 3,)
    ellipse(550, 250, 10,10)
    ellipse(550, 350, 10,10)
   
    fill(0)
    textSize(50)
    text(key, width/3, height/2)

    rect(x, y , 200, 100)
   
    if key == 'w':
        y-=5
    elif key == 'd':
        x+=5
    elif key == 's':
        y+=5
    elif key == 'a':
        x-=5
