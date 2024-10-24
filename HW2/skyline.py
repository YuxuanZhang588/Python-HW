"""
A program that calls the Turtle to draw a city skyline.

Authors: AJ Pabst and David Zhang

Time spent: 5 hours

"""

import turtle

     
def background():
    #background color
    turtle.speed(10000000)
    turtle.up()
    turtle.setpos(-1200,1000)
    turtle.down()
    turtle.colormode(255)
    for i in range(100):
        turtle.color((int(21+1.64*i),int(101-0.57*i),int(193-1.54*i)),(int(21+1.64*i),int(101-0.57*i),int(193-1.54*i)))
        #color change from (21,101,193) to (185,44,39)
        drawbox()
    turtle.colormode(1)
    turtle.speed(15)
    turtle.color('black','black')
    turtle.up()
    turtle.setpos(-1200,-650)
    turtle.down()
    drawbottom()
    turtle.up()
    
    #stars
    for i in range(6):
        turtle.up()
        turtle.setpos(0+150*i,200+100*(i**0.5))
        turtle.down()
        drawstar()
        turtle.up()
        
    #moon
    drawmoon()
    
    
    
def drawbox():
    turtle.begin_fill()
    turtle.fd(2400)
    turtle.rt(90)
    turtle.fd(20)
    turtle.rt(90)
    turtle.fd(2400)
    turtle.rt(90)
    turtle.fd(20)
    turtle.bk(20)
    turtle.setheading(0)
    turtle.end_fill()
    turtle.hideturtle()

def drawbottom():
    turtle.begin_fill()
    turtle.fd(2400)
    turtle.rt(90)
    turtle.fd(350)
    turtle.rt(90)
    turtle.fd(2400)
    turtle.rt(90)
    turtle.fd(350)
    turtle.bk(350)
    turtle.setheading(0)
    turtle.end_fill()
    turtle.hideturtle()
    
def drawstar():
    turtle.color('ivory','ivory')
    turtle.begin_fill()
    turtle.seth(85)
    turtle.fd(30)
    turtle.seth(5)
    turtle.fd(30)
    turtle.seth(175)
    turtle.fd(30)
    turtle.seth(95)
    turtle.fd(30)
    turtle.seth(-95)
    turtle.fd(30)
    turtle.seth(185)
    turtle.fd(30)
    turtle.seth(-5)
    turtle.fd(30)
    turtle.seth(-85)
    turtle.fd(30)
    turtle.end_fill()

def drawmoon():
    turtle.up()
    turtle.setpos(700,700)
    turtle.down()
    turtle.color('ivory','ivory')
    turtle.begin_fill()
    turtle.circle(60)
    turtle.end_fill()
    turtle.up()
    turtle.setpos(0,-700)
    turtle.lt(80)
    
def draw_stl_arch():
    """
    Draws a replica of the Gateway Arch Monument in St. Louis, MO
    """
    turtle.up()
    turtle.setpos(200,-700)
    turtle.lt(5)
    turtle.color("grey")
    turtle.begin_fill()
    turtle.down()
    turtle.left(80)
    turtle.fd(300)
    turtle.rt(10)
    turtle.fd(150)
    turtle.rt(10)
    turtle.fd(50)
    turtle.rt(15)
    turtle.fd(30)
    turtle.rt(15)
    turtle.fd(50)
    turtle.rt(15)
    turtle.fd(30)
    turtle.rt(15)
    #left middle
    turtle.fd(30)
    #right middle
    turtle.rt(15)
    turtle.fd(30)
    turtle.rt(15)
    turtle.fd(50)
    turtle.rt(15)
    turtle.fd(30)
    turtle.rt(15)
    turtle.fd(50)
    turtle.rt(10)
    turtle.fd(150)
    turtle.rt(10)
    turtle.fd(300)
    turtle.rt(100)
    turtle.fd(50)
    turtle.rt(90)
    
def draw_arch_filling():
    """
    Fills in color for arch
    """
    
    turtle.lt(8)
    turtle.fd(300)
    turtle.lt(10)
    turtle.fd(150)
    turtle.lt(12)
    turtle.fd(30)
    turtle.lt(12)
    turtle.fd(30)
    turtle.lt(12)
    turtle.fd(30)
    turtle.lt(12)
    turtle.fd(30)
    turtle.lt(24)
    turtle.fd(25) #middle
    turtle.lt(24)
    turtle.fd(30)
    turtle.lt(12)
    turtle.fd(30)
    turtle.lt(12)
    turtle.fd(30)
    turtle.lt(12)
    turtle.fd(30)
    turtle.lt(12)
    turtle.fd(150)
    turtle.lt(10)
    turtle.fd(300)
    turtle.lt(8)
    turtle.rt(90)
    turtle.fd(50)
    turtle.end_fill()
    turtle.up()
    turtle.fd(200)
    turtle.rt(90)
    
def draw_freedom_tower_base():
    """
    Draw the base of the freedom tower
    """
    turtle.lt(90)
    turtle.fd(750)
    turtle.down()
    turtle.color("sky blue")
    turtle.begin_fill()
    turtle.fd(200)
    turtle.rt(90)
    turtle.fd(200)
    turtle.rt(90)
    turtle.fd(200)
    turtle.rt(90)
    turtle.fd(200)
    turtle.end_fill()
    turtle.back(200)
    
def draw_freedom_tower_middle():
    """
    Draw the middle triangle of the freedom tower
    """
    turtle.color("blue")
    turtle.rt(174)
    turtle.begin_fill()
    turtle.fd(950)
    turtle.back(950)
    turtle.lt(84)
    turtle.fd(200)
    turtle.rt(96)
    turtle.fd(950)
    turtle.end_fill()
    
def draw_freedom_tower_outer():
    """
    Draw the left and right triangles of the freedom tower
    """
    turtle.lt(106)
    turtle.color("sky blue")
    turtle.begin_fill()
    turtle.fd(100)
    turtle.lt(80)
    turtle.fd(900)
    turtle.lt(174)
    turtle.fd(925)
    turtle.end_fill()
    turtle.rt(94)
    turtle.begin_fill()
    turtle.fd(100)
    turtle.rt(80)
    turtle.fd(900)
    turtle.rt(174)
    turtle.fd(925)
    turtle.end_fill()
    
def draw_freedom_tower_spire():
    """
    Draw the spire at the top of the freedom tower
    """
    turtle.up()
    turtle.color("white")
    turtle.lt(84)
    turtle.fd(50)
    turtle.lt(90)
    turtle.fd(15)
    turtle.rt(180)
    turtle.begin_fill()
    turtle.down()
    turtle.fd(25)
    turtle.rt(90)
    turtle.fd(100)
    turtle.rt(90)
    turtle.fd(25)
    turtle.rt(100)
    turtle.fd(50)
    turtle.lt(20)
    turtle.fd(50)
    turtle.end_fill()
    turtle.rt(100)
    turtle.fd(25)
    turtle.rt(90)
    turtle.fd(45)
    turtle.begin_fill()
    turtle.lt(88)
    turtle.fd(150)
    turtle.back(150)
    turtle.rt(88)
    turtle.fd(10)
    turtle.lt(92)
    turtle.fd(150)
    turtle.end_fill()
    turtle.up()
    turtle.setpos(0,-700)
    
def draw_freedom_tower():
    """
    Draws the entire freedom tower
    """
    draw_freedom_tower_base()
    draw_freedom_tower_middle()
    draw_freedom_tower_outer()
    draw_freedom_tower_spire()
    
def draw_att_stadium_front():
    """
    Draws the front of AT&T Stadium in Arlington, TX
    """
    turtle.color("navy blue")
    turtle.down()
    turtle.lt(88)
    turtle.fd(100)
    turtle.begin_fill()
    turtle.fd(100)
    turtle.rt(90)
    turtle.fd(100)
    turtle.rt(85)
    turtle.fd(100)
    turtle.rt(10)
    turtle.fd(100)
    turtle.rt(85)
    turtle.fd(100)
    turtle.rt(90)
    turtle.fd(100)
    turtle.end_fill()
    
def draw_att_stadium_sides():
    """
    Draws the sides of AT&T Stadium in Arlington, TX
    """
    turtle.fd(100)
    turtle.color("sky blue")
    turtle.begin_fill()
    turtle.fd(150)
    turtle.rt(65)
    turtle.fd(110)
    turtle.rt(115)
    turtle.fd(197)
    turtle.rt(90)
    turtle.fd(100)
    turtle.end_fill()
    turtle.up()
    turtle.lt(90)
    turtle.fd(200)
    turtle.down()
    turtle.begin_fill()
    turtle.fd(150)
    turtle.lt(65)
    turtle.fd(110)
    turtle.lt(115)
    turtle.fd(197)
    turtle.lt(90)
    turtle.fd(100)
    turtle.end_fill()
    
def draw_att_stadium_upper_sides():
    """
    Draws the top of AT&T Stadium in Arlington, TX
    """
    turtle.up()
    turtle.lt(180)
    turtle.down()
    turtle.color("grey")
    turtle.begin_fill()
    turtle.fd(100)
    turtle.rt(75)
    turtle.fd(175)
    turtle.rt(105)
    turtle.fd(45)
    turtle.rt(90)
    turtle.fd(170)
    turtle.end_fill()
    turtle.up()
    turtle.fd(200)
    turtle.down()
    turtle.begin_fill()
    turtle.rt(15)
    turtle.fd(175)
    turtle.lt(105)
    turtle.fd(45)
    turtle.lt(90)
    turtle.fd(170)
    turtle.end_fill()
    
def draw_att_stadium_roof():
    """
    Draws the non-removeable part of the roof
    """
    turtle.color("light grey")
    turtle.begin_fill()
    turtle.rt(15)
    turtle.back(190)
    turtle.fd(190)
    turtle.lt(20)
    turtle.fd(100)
    turtle.rt(10)
    turtle.fd(100)
    turtle.lt(20)
    turtle.fd(190)
    turtle.lt(135)
    turtle.fd(100)
    turtle.lt(15)
    turtle.fd(100)
    turtle.lt(15)
    turtle.fd(200)
    turtle.lt(15)
    turtle.fd(100)
    turtle.lt(15)
    turtle.fd(100)
    turtle.end_fill()
    
def draw_att_stadium_removeable_roof():
    """
    Draws the removeable part of the roof
    """
    turtle.up()
    turtle.back(100)
    turtle.rt(15)
    turtle.back(100)
    turtle.rt(15)
    turtle.back(10)
    turtle.lt(90)
    turtle.begin_fill()
    turtle.color("white")
    turtle.down()
    turtle.fd(15)
    turtle.lt(95)
    turtle.fd(90)
    turtle.rt(10)
    turtle.fd(90)
    turtle.lt(95)
    turtle.fd(30)
    turtle.lt(85)
    turtle.fd(90)
    turtle.lt(10)
    turtle.fd(90)
    turtle.lt(85)
    turtle.fd(15)
    turtle.end_fill()
    
def draw_att_stadium_accessories():
    """
    Draws some accessories on AT&T Stadium
    """
    turtle.up()
    turtle.color("dark grey")
    turtle.fd(15)
    turtle.pensize(10)
    turtle.down()
    turtle.fd(230)
    turtle.up()
    turtle.lt(90)
    turtle.fd(180)
    turtle.lt(90)
    turtle.down()
    turtle.fd(230)
    turtle.up()
    turtle.pensize(1)
    turtle.color("navy blue")
    turtle.lt(135)
    turtle.fd(75)
    turtle.rt(90)
    turtle.fd(50)
    turtle.lt(150)
    turtle.fd(25)
    turtle.down()
    turtle.begin_fill()
    
    for i in range(5):
        turtle.lt(75)
        turtle.fd(25)
        turtle.rt(146)
        turtle.fd(25)
        
    turtle.rt(20)
    turtle.end_fill()
    turtle.up()
    turtle.setpos(0,-700)
    
def draw_att_stadium():
    """
    Draws the outside of AT&T Stadium in Arlington, TX
    """
    draw_att_stadium_front()
    draw_att_stadium_sides()
    draw_att_stadium_upper_sides()
    draw_att_stadium_roof()
    draw_att_stadium_removeable_roof()
    draw_att_stadium_accessories()
    
def draw_burj_al_arab():
    """
    Draws the Burj Al Arab in Dubai
    """
    turtle.lt(90)
    turtle.fd(935)
    turtle.rt(90)
    turtle.down()
    turtle.speed(50)
    turtle.pensize(30)
    turtle.color('dimgray','papayawhip')
    turtle.begin_fill()
    turtle.setheading(90)
    turtle.fd(760)
    turtle.bk(100)
    turtle.pensize(10)

    turtle.seth(220)
    turtle.fd(100)
    for i in range(5):
        turtle.seth(220 + i * 15)
        turtle.fd(100 + i * 15)
    turtle.fd(20)
    turtle.seth(0)
    turtle.pensize(30)
    turtle.fd(240)
    turtle.end_fill()
    turtle.seth(90)
    turtle.fd(550)
    turtle.seth(-90)
    turtle.pensize(20)
    for i in range(3):
        turtle.rt(90)
        turtle.fd(120+i*45)
        turtle.bk(120+i*45)
        turtle.lt(90)
        turtle.fd(50)
    for i in range(2):
        turtle.rt(90)
        turtle.fd(220+i*25)
        turtle.bk(220+i*25)
        turtle.lt(90)
        turtle.fd(50)
    for i in range(3):
        turtle.rt(90)
        turtle.fd(250+i*10)
        turtle.bk(250+i*10)
        turtle.lt(90)
        turtle.fd(50)
    for i in range(3):
        turtle.rt(90)
        turtle.fd(260-i*10)
        turtle.bk(260-i*10)
        turtle.lt(90)
        turtle.fd(50)
    turtle.up()
    turtle.seth(90)
    turtle.fd(550)
    turtle.down()
    turtle.pensize(10)
    turtle.color('dimgray','midnightblue')
    turtle.begin_fill()
    turtle.lt(90)
    turtle.fd(130)
    turtle.seth(40)
    turtle.fd(100)
    turtle.seth(-90)
    turtle.fd(52.53219888177297)
    turtle.end_fill()
    turtle.up()
    turtle.setpos(0,-700)
    
def draw_oriental_pearl():
    """
    Draws the Oriental Pearl Tower in Shanghai, China
    """
    turtle.up()
    turtle.setpos(-725,-700)
    turtle.color('darkgray','red')
    turtle.speed(50)
    turtle.down()
    turtle.pensize(35)
    turtle.setheading(60)
    turtle.fd(300)
    turtle.setheading(0)
    turtle.fd(20)
    turtle.setheading(-90)
    turtle.fd(259.8076211353316)
    turtle.bk(259.8076211353316)
    turtle.setheading(0)
    turtle.fd(20)
    turtle.setheading(-60)
    turtle.fd(300)
    turtle.bk(300)
    turtle.setheading(180)
    turtle.fd(20)
    turtle.setheading(-90)
    turtle.fd(20)
    turtle.setheading(0)
    turtle.pensize(20)
    turtle.color('darkgray','darkgray')
    turtle.begin_fill()
    turtle.circle(80)
    turtle.end_fill()
    turtle.up()
    turtle.setheading(90)
    turtle.fd(80)
    turtle.rt(90)
    turtle.down()
    turtle.color('red','red')
    turtle.pensize(50)
    turtle.fd(70)
    turtle.bk(140)
    turtle.up()
    turtle.fd(70)
    turtle.lt(90)
    turtle.fd(59)
    turtle.rt(90)
    turtle.fd(60)
    turtle.down()
    turtle.color('darkgray','darkgray')
    turtle.pensize(30)
    turtle.lt(90)
    turtle.fd(399)
    turtle.up()
    turtle.lt(90)
    turtle.fd(120)
    turtle.down()
    turtle.lt(90)
    turtle.fd(399)
    turtle.bk(399)
    turtle.pensize(20)
    for i in range (6):
        turtle.forward(55)
        turtle.lt(90)
        turtle.fd(120)
        turtle.bk(120)
        turtle.setheading(-90)
    turtle.setheading(90)
    turtle.fd(320)
    turtle.rt(90)
    turtle.up()
    turtle.fd(60)
    turtle.down()
    turtle.pensize(20)
    turtle.begin_fill()
    turtle.circle(75)
    turtle.end_fill()
    turtle.up()
    turtle.setheading(90)
    turtle.fd(75)
    turtle.rt(90)
    turtle.pensize(45)
    turtle.color('red','red')
    turtle.down()
    turtle.fd(65)
    turtle.bk(130)
    turtle.up()
    turtle.fd(65)
    turtle.lt(90)
    turtle.fd(75)
    turtle.down()
    turtle.color('darkgray','darkgray')
    turtle.pensize(30)
    turtle.fd(100)
    turtle.pensize(10)
    turtle.rt(90)
    turtle.color('darkgray','red')
    turtle.begin_fill()
    turtle.circle(30)
    turtle.end_fill()
    turtle.lt(90)
    turtle.up()
    turtle.fd(60)
    turtle.down()
    turtle.fd(55)
    turtle.up()
    turtle.setpos(0,-700)

def draw_skyline():
    """
    Draws the entire city skyline
    """
    
    background()
    draw_stl_arch()
    draw_arch_filling()
    draw_freedom_tower()
    draw_att_stadium()
    draw_burj_al_arab()
    draw_oriental_pearl()
    turtle.hideturtle()
    turtle.done()
    
'''
Change the code below, as required, to run the program
'''
def main():
    """
    A wrapper function that calls the functions above
    """
    
    draw_skyline()

'''
Do NOT change the code below
'''
    
if __name__ == "__main__":
    main() 