from tkinter import *
from math import * 
from time import *
from random import *
from DecimalToHex import*

root = Tk()
s=Canvas(root, width=1000, height=600, background="black")
s.pack()

# Setting up initial values
def setInitialValues():
    global lives, score, xBubble, yBubble, xPlat, yPlat
    global xSpdPlat, ySpdPlat, BubbleDrawings, platDrawings, difficulty
    global yBubbleSpd, radiusBubble, tree, framesLeft, key, numBubbles, platDiffSpd
    global starttime, currenttime, xExplosionStart, yExplosionStart
    global xExplosionSpd, yExplosionSpd, ParticleRadius, ExplosionDrawings, inMenu
    lives=3
    score=0
    xBubble=[]
    yBubble=[]
    xPlat=500
    yPlat=500
    xSpdPlat=0
    radiusBubble=[]
    yBubbleSpd=[]
    BubbleDrawings=[]
    starttime=time()
    currenttime=0
    xExplosionStart=[]
    yExplosionStart=[]
    xExplosionSpd=[]
    yExplosionSpd=[]
    ParticleRadius=[]
    ExplosionDrawings=[]
    framesLeft=[]
    tree=PhotoImage(file="tree.gif")
    key=""
    inMenu=False

# Homescreen
def menuScreen():
    global a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, inMenu
    
    inMenu=True
    
    s.create_rectangle(0,0,1000,600,fill="steelblue")
    for star in range(200):
        xStar=randint(0,993)
        yStar=randint(0,593)
        sizeStar=randint(2,6)
        s.create_oval(xStar, yStar, xStar+sizeStar, yStar+sizeStar, fill="lightblue", outline="lightblue")
    a1 = s.create_rectangle(400,100,600,200,fill="slategray")
    a2 = s.create_text(500,150,text="Start Game", font = "impact 30", fill = "deepskyblue2")
    a3 = s.create_rectangle(400,250,600,350,fill="slategray")
    a4 = s.create_text(500,300, text="Rules", font="impact 30", fill="deepskyblue2")
    a5 = s.create_rectangle(400,400,600,500,fill="slategray")
    a6 = s.create_text(500,450, text="Quit", font="impact 30", fill="deepskyblue2")
    a7 = s.create_text(500,50, text="BUBBLE FLOOD!", font="impact 44", fill="cyan")
    a8 = s.create_image(150,400,image=tree)
    a9 = s.create_image(850,150,image=tree)
    a10= s.create_rectangle(750,485,850,515,fill="limegreen",outline="darkgreen",width=4)
    
    s.bind( "<Button-1>", startMouseClickHandler )

# Mouse code when user is on homescreen
def startMouseClickHandler(event):
    global a1, a2, a3, a4, a5, a6, a7, a8, a9, a10
    
    if inMenu==False:
        return
    
    xMouse = event.x
    yMouse = event.y

    if 400<xMouse<600 and 100<yMouse<200:
        s.delete(a1, a2, a3, a4, a5, a6, a7, a8, a9, a10)
        difficultySetting()

    elif 400<xMouse<600 and 250<yMouse<350:
        s.delete(a1, a2, a3, a4, a5, a6, a7, a8, a9, a10)
        ruleScreen()
        
    elif 400<xMouse<600 and 400<yMouse<500:
        root.destroy()

# Difficulty choosing screen
def difficultySetting():
    global b1, b2, b3, b4, b5, b6, b7, b8, platDiffSpd, numBubbles
    
    s.create_rectangle(0,0,1000,600,fill="steelblue")

    b1 = s.create_rectangle(400,50,600,150,fill="slategray")
    b2 = s.create_rectangle(400,200,600,300,fill="slategray")
    b3 = s.create_rectangle(400,350,600,450,fill="slategray")
    b4 = s.create_text(500,100,text="Easy",font="impact 30",fill="deepskyblue2")
    b5 = s.create_text(500,250,text="Normal",font="impact 30",fill="deepskyblue2")
    b6 = s.create_text(500,400,text="Hard",font="impact 30",fill="deepskyblue2")
    b7 = s.create_rectangle(850,450,950,500,fill="slategray")
    b8 = s.create_text(900,475,text="Back",font="impact 30",fill="deepskyblue2")

    s.bind( "<Button-1>", difficultyMouseClickHandler )

# Mouse code when user is on difficulty choosing screen
def difficultyMouseClickHandler (event):
    global b1, b2, b3, b4, b5, b6, b7, b8, platDiffSpd, numBubbles
    
    if inMenu==False:
        return
    
    xMouse = event.x
    yMouse = event.y
    
    if 400 < xMouse < 600 and 50 < yMouse < 150:
        s.delete(b1, b2, b3, b4, b5, b6, b7, b8)
        numBubbles=4
        platDiffSpd=20
        runGame()

    elif 400 < xMouse < 600 and 200 < yMouse < 300:
        s.delete(b1, b2, b3, b4, b5, b6, b7, b8)
        numBubbles=7
        platDiffSpd=18
        runGame()
        
    elif 400 < xMouse < 600 and 350 < yMouse < 450:
        s.delete(b1, b2, b3, b4, b5, b6, b7, b8)
        numBubbles=9
        platDiffSpd=16
        runGame()
    elif 850 < xMouse < 950 and 450 < yMouse < 500:
        s.delete(b1, b2, b3, b4, b5, b6, b7, b8)
        menuScreen()

# Screen with rules printed on
def ruleScreen():
    global r1, r2, r3, r4, r5, r6, r7, r8, r9, r10, r11, r12, r13, r14, r15, r16
    
    s.create_rectangle(0,0,1000,600,fill="steelblue")
    
    r1 = s.create_text(500,100,text="You must control a deflector near the bottom of the", font="impact 22", fill="black")
    r2 = s.create_text(500,130,text="screen with the left and right arrow keys. The deflector itself moves to the", font="impact 22", fill="black")
    r3 = s.create_text(500,160,text="left and right on the screen. Bubbles will start moving down the screen,", font="impact 22", fill="black")
    r4 = s.create_text(500,190,text="and the user is supposed get in between the bubbles and the trees", font="impact 22", fill="black")
    r5 = s.create_text(500,220,text="before the bubbles hit the trees. If the user is successful,", font= "impact 22", fill="black")
    r6 = s.create_text(500,250,text="then the bubbles will hit the deflector and change direction", font="impact 22", fill="black")
    r7 = s.create_text(500,280,text="and move away from the trees. The user starts with 3 lives and if a", font="impact 22", fill="black")
    r8 = s.create_text(500,310,text="bubble hits the trees at the bottom, you lose a life. Your score is", font="impact 22", fill="black")
    r9 = s.create_text(500,340,text="determined by the number of bubbles you divert in 1 minute. You", font="impact 22", fill="black")
    r10 = s.create_text(500,370,text="win if you don’t lose 3 lives in one minute, you lose if you let", font="impact 22", fill="black")
    r11 = s.create_text(500,400,text="3 bubbles hit the ground, causing you to lose 3 lives.", font="impact 22", fill="black")          
    r12 = s.create_text(500,460,text="LEFT/RIGHT: move Bubble Deflector left and right", font="impact 22", fill="darkblue")
    r13 = s.create_text(500,500,text="'q': Quit | 'r': Restart", font="impact 24", fill="darkblue")
    r14 = s.create_text(500,50,text="The Rules", font="impact 30", fill="cyan")
    r15 = s.create_rectangle(850,525,950,575,fill="slategray")
    r16 = s.create_text(900,550,text="Back",font="impact 25",fill="deepskyblue2")
    s.bind( "<Button-1>", ruleMouseClickHandler )
    
# Mouse when user is on rules screen
def ruleMouseClickHandler(event):
    global r1, r2, r3, r4, r5, r6, r7, r8, r9, r10, r11, r12, r13, r14, r15, r16
    
    if inMenu==False:
        return
    
    xMouse = event.x
    yMouse = event.y

    if 850 < xMouse < 950 and 525 < yMouse < 575:
        s.delete(r1, r2, r3, r4, r5, r6, r7, r8, r9, r10, r11, r12, r13, r14, r15, r16)
        menuScreen()

# Background
def backgroundGradient():
    R1=0
    G1=38
    B1=77
    R2=179
    G2=240
    B2=255
    dr=(R2-R1)/256
    dg=(G2-G1)/256
    db=(B2-B1)/256
    dx=1000/256
    for i in range(256):
        r=round(R1+i*dr)
        g=round(G1+i*dg)
        b=round(B1+i*db)
        c=getPythonColor(r,g,b)
        s.create_rectangle(0,i*dx,1000,(i+1)*dx,fill=c,outline=c)
    for star in range(200):
        xStar=randint(0,1000)
        yStar=randint(0,600)
        sizeStar=randint(2,6)
        s.create_oval(xStar, yStar, xStar+sizeStar, yStar+sizeStar, fill="white", outline="white")
    for t in range(50,1000,150):
        treeImage=s.create_image(t,650,image=tree)

# Make/update time
def updateTimer():
    global currenttime, starttime, Time
    currenttime=starttime+60-time()

# Draw the timer
def drawTimer():
    global currenttime, starttime, Time
    Time=s.create_text(130,150,text="Time Left: " + str(round(currenttime,1)), font="Times 30", fill="turquoise1")

# Delete the timer
def deleteTimer():
    global currenttime, starttime, Time
    s.delete(Time)
    
# Drawing the platform
def drawPlatform():
    global Platform,xSpdPlat, xPlat
    Platform=s.create_rectangle(xPlat-50,yPlat-15,xPlat+50,yPlat+15,fill="limegreen",outline="darkgreen",width=4)

# Updating the platforms position
def updatePlatPosition():
    global xPlat,xSpdPlat
    xPlat = min(950,max(50,xPlat + xSpdPlat))

# Creating Bubbles
def createBubble():
    global xBubble, yBubble, radiusBubble, yBubbleSpd, BubbleDrawings, numBubbles
    for i in range(numBubbles):
        xBubble.append(randint(0,1000))
        yBubble.append(randint(-200,0))
        radiusBubble.append(randint(10,30))
        yBubbleSpd.append(uniform(0.5,4))
        BubbleDrawings.append(0)

# Drawing Bubbles
def drawBubble():
    global xBubble, yBubble, radiusBubble, BubbleDrawings, numBubbles
    for b in range(numBubbles):
        BubbleDrawings[b]=s.create_oval(xBubble[b]-radiusBubble[b],yBubble[b]-radiusBubble[b],xBubble[b]+radiusBubble[b], yBubble[b]+radiusBubble[b],outline="lightseagreen", width=6)
                                
# Update bubble position
def updateBubblePosition():
    global yBubble,yBubbleSpd, numBubbles
    for b in range(numBubbles):
        yBubble[b]=yBubble[b]+yBubbleSpd[b]
        
# Deleteing Bubbles
def deleteBubble():
    global BubbleDrawings, numBubbles
    for b in range(numBubbles):
        s.delete(BubbleDrawings[b])

# Left and right arrow keys to move platform
def keyDownHandler(event):
    global key, xSpdPlat, platDiffSpd
    if event.keysym == "Left":
        xSpdPlat = -platDiffSpd
        
    elif event.keysym == "Right":
        xSpdPlat = platDiffSpd
    
    elif lives<=0 or currenttime<=0:
        if event.keysym.lower()=="r":
            key="r"
        elif event.keysym.lower()=="q":
            key="q"

# When you stop pressing the arrow keys
def keyUpHandler(event):
    global xSpdPlat
    if event.keysym == "Left":     
        xSpdPlat = 0  
        
    elif event.keysym == "Right":  
        xSpdPlat = 0
        
# Distance of a line equation
def distanceBetweenPoint(x1,y1,x2,y2):
    return sqrt((x2-x1)**2+(y2-y1)**2)

# Checking if Bubble is on the platforms current coordinates
def pointInPlatform(x,y):
    global xExplosionSpd, yExplosionSpd, ParticleRadius, ExplosionDrawings
    if xPlat-50<=x<=xPlat+50 and yPlat-15<=y<=yPlat+15:
        return True
    else:
        return False

# Minimum distance between bubble and all 4 corners
def minDistToCorners(x,y):
    global xPlat, yPlat
    a=distanceBetweenPoint(x,y,xPlat-50,yPlat-15)
    b=distanceBetweenPoint(x,y,xPlat-50,yPlat+15)
    c=distanceBetweenPoint(x,y,xPlat+50,yPlat-15)
    d=distanceBetweenPoint(x,y,xPlat+50,yPlat+15)
    return min(a,b,c,d)

# Checking if the bubble is colliding using previous functions
def bubbleCollision(index):
    global xBubble, yBubble, radiusBubble, score
    isBubbleColliding=False
    points=((0,-1),(1,0),(0,1),(-1,0)) #x,y possibilities of bubble edges
    for p in points:
        x=xBubble[index]+radiusBubble[index]*p[0]
        y=yBubble[index]+radiusBubble[index]*p[1]
        if pointInPlatform(x,y)==True:
            isBubbleColliding=True

    if minDistToCorners(xBubble[index],yBubble[index])<=radiusBubble[index]:
        isBubbleColliding=True

    if isBubbleColliding==True:
        xC=xBubble[index]
        yC=yBubble[index]
        createExplosion(xC,yC)
        xBubble[index]=randint(0,1000)
        yBubble[index]=randint(-600,0)
        score=score+1

# Checking all bubbles to see if they are hitting the platform in a for-loop
def checkCollision():
    global BubbleDrawings
    for i in range(len(BubbleDrawings)):
        bubbleCollision(i)

# Calculates the number of lives left
def livesLeft():
    global lives
    for i in range(len(yBubble)):
        if yBubble[i]>600:
            if lives>=1:
                xBubble[i]=randint(0,1000)
                yBubble[i]=randint(-600,0)
                lives=lives-1

# Lives on screen
def livesBoard():
    global lives, LifeBoard
    LifeBoard=s.create_text(100,50,text="Lives: " + str(lives), font="Times 30", fill="turquoise1")

# Deleting Lifeboard
def deleteLivesBoard():
    global lives, LifeBoard
    s.delete(LifeBoard)

# Drawing score board
def drawScoreBoard():
    global ScoreBoard, score
    ScoreBoard=s.create_text(100,100,text="Score: " + str(score), font="Times 30", fill="turquoise1")

# Deleting score board
def deleteScoreBoard():
    global ScoreBoard, score
    s.delete(ScoreBoard)
    
# Create bubble explosion
def createExplosion(xC,yC):
    r=[]
    xSpd=[]
    ySpd=[]
    x=[]
    y=[]
    ED=[]
    for i in range(30):
        xSpd.append(gauss(0,5))
        ySpd.append(gauss(0,5))
        r.append(randint(4,7))
        ED.append(0)
        x.append(xC)
        y.append(yC)

    xExplosionStart.append(x)
    yExplosionStart.append(y)
    xExplosionSpd.append(xSpd)
    yExplosionSpd.append(ySpd)
    ParticleRadius.append(r)
    ExplosionDrawings.append(ED)
    framesLeft.append(15)

# Draws an explosion
def drawExplosion():
    global xExplosionStart, yExplosionStart, xExplosionSpd, yExplosionSpd, ParticleRadius, ExplosionDrawings
    for e in range(len(ExplosionDrawings)):
        for p in range(30):
            ExplosionDrawings[e][p]=s.create_oval(xExplosionStart[e][p],yExplosionStart[e][p],xExplosionStart[e][p]+ParticleRadius[e][p],yExplosionStart[e][p]+ParticleRadius[e][p],fill="skyblue",outline="lightblue")

# Updates the explosion
def updateExplosion():
    global xExplosionStart, yExplosionStart, xExplosionSpd, yExplosionSpd
    for i in range(len(ExplosionDrawings)):
        for p in range(30):
            xExplosionStart[i][p]=xExplosionStart[i][p]+xExplosionSpd[i][p]
            yExplosionStart[i][p]=yExplosionStart[i][p]+yExplosionSpd[i][p]

# Deletes the explosion
def deleteExplosion():
    global ExplosionDrawings
    for e in range(len(ExplosionDrawings)-1,-1,-1):
        for p in range(30):
            s.delete(ExplosionDrawings[e][p])
        if framesLeft[e] == 0:
            xExplosionStart.pop(e)
            yExplosionStart.pop(e)
            xExplosionSpd.pop(e)
            yExplosionSpd.pop(e)
            ParticleRadius.pop(e)
            ExplosionDrawings.pop(e)
            framesLeft.pop(e)
        else:
            framesLeft[e] = framesLeft[e] - 1

# End game prompts
def showPrompt():
    global endgame1, promptGood, promptBad, prompt2, prompt3
    endgame1=s.create_rectangle(0,0,1000,600,fill="steelblue")
    prompt2=s.create_text(500,300,text="If you would like to restart, press 'r'\n If you would like to quit, press 'q'",font="Times 30", fill="turquoise1")
    prompt3=s.create_text(500,400,text="Your final score was: " + str(score), font="Times 30", fill="turquoise1")
    if currenttime<=0 and lives>0:
        promptGood=s.create_text(515,150,text="YOU WON!",font="Times 50", fill="skyblue")
    else:
        promptBad=s.create_text(515,150,text="PATHETIC...",font="Times 50", fill="skyblue")
    
# Update prompts  
def deleteShowPrompt():
    global endgame1,promptGood, promptBad ,prompt2, prompt3
    s.delete(endgame1, prompt2, prompt3)
    if currenttime<=0 and lives>0:
        s.delete(promptGood)
    else:
        s.delete(promptBad)
                        
def runGame():
    setInitialValues()
    createBubble()
    backgroundGradient()
    s.update()

    while lives>0 and currenttime>=0:
        drawPlatform()
        livesLeft()
        livesBoard()
        drawScoreBoard()
        drawTimer()
         
        drawBubble()
        checkCollision()
        drawExplosion()

        s.update()
        sleep(0.03)
        s.delete(Platform)

        updatePlatPosition()
        updateBubblePosition()
        updateExplosion()
        updateTimer()

        deleteBubble()
        deleteExplosion()
        deleteLivesBoard()
        deleteScoreBoard()
        deleteTimer()
    while key != "r" and key != "q":
        showPrompt()
        s.update()
        deleteShowPrompt()
    if key == "r":
        menuScreen()
    elif key == "q":
        root.destroy()
setInitialValues()

root.after( 0, menuScreen )

s.bind( "<KeyPress>", keyDownHandler )
s.bind( "<KeyRelease>", keyUpHandler )

s.pack()
s.focus_set()
root.mainloop()
