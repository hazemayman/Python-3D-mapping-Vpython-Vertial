from visual  import *
import os
import sqlite3
from sqlite3 import Error

def create_connection():
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    try:
        conn = sqlite3.connect("C:\\Users\\Ultriva\\Dev\\tryDjango\\src\\db.sqlite3")
        return conn
    except Error as e:
        print(e)
 
    return None

def genrateObjects(conn):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM ultrasonicValues_ultrasonic")
 
    rows = cur.fetchall()
    for row in rows:
        leftDistance = row[1]
        frontDistance = row[3]
        rightDistance = row[2]
        direction = row[4]
        distanceTaken = row[5]
        print(leftDistance,rightDistance,distanceTaken,frontDistance , direction)
        mainDraw(leftDistance,rightDistance,distanceTaken,frontDistance , direction)


def convertingToTxt():
    thisFile = "testFile.py"
    base = os.path.splitext(thisFile)[0]
    os.rename(thisFile, base + ".txt")
def convertingToPythonFile():
    thisFile = "testFile.txt"
    
    if(os.path.exists('testFile.py')):
        os.remove('testFile.py')
    base = os.path.splitext(thisFile)[0]
    os.rename(thisFile, base + ".py")   


def savingFiles(boxesArray):
    text =""
    fileObject = open("testFile.txt","a")
    for wallObject in boxesArray:
        pos = wallObject.pos
        pos = "(" + str(pos[0]) + "," + str(pos[1]) + "," + str(pos[2]) + ")"
        color = wallObject.color
        size = wallObject.size
        size = "(" + str(size[0]) + "," + str(size[1]) + "," + str(size[2]) + ")"
        text = "box(pos = {} , color = {} , size = {} ) \n".format(pos,color,size)
        fileObject.write(text)
    fileObject.close()

#convertingToTxt()
fileObject = open("testFile.txt" , "w")
fileObject.write("from visual import * \n")
fileObject.close()

heightOfWalls = 1.0
thicknesOfWalls = .2
posetionLeft = [0,heightOfWalls/2.0,0]
firstPieaceOfData = True
posetionRight = [0,heightOfWalls/2.0,0]
DirectionOfMoving = ["F",0]
average = 0


def determineDerictionOFMoving(direction):
    global DirectionOfMoving

    if(direction == "R"):

        if(DirectionOfMoving[0] == "F"):

            if(DirectionOfMoving[1] == 0):
                DirectionOfMoving[1] = 1

            elif(DirectionOfMoving[1] == -1 ):
                DirectionOfMoving[1] = 0

            elif(DirectionOfMoving[1] == 1):
                DirectionOfMoving[0] = "B"
                DirectionOfMoving[1] = 0

        elif(DirectionOfMoving[0] == "B"):
            if(DirectionOfMoving[1] == 0):
                DirectionOfMoving[0] = "F"
                DirectionOfMoving[1] = -1
    elif(direction == "L"): 
        if(DirectionOfMoving[0] == "F"):

            if(DirectionOfMoving[1] == 0):
                DirectionOfMoving[1] = -1

            elif(DirectionOfMoving[1] == -1 ):
                DirectionOfMoving[0] = "B"
                DirectionOfMoving[1] = 0
                
            elif(DirectionOfMoving[1] == 1):
                DirectionOfMoving[1] = 0

        elif(DirectionOfMoving[0] == "B"):
            if(DirectionOfMoving[1] == 0):
                DirectionOfMoving[0] = "F"
                DirectionOfMoving[1] = 1
        

def settingPostionOfBoxLeft( distanceTaken ):
    global posetionLeft
    global posetionRight
    if(DirectionOfMoving[0] == "F" and DirectionOfMoving[1] == 0):

        posetionLeft[2] = posetionLeft[2] - (distanceTaken/2.0)
        #posetionRight[2] = posetionRight[2] - (distanceTaken/2.0)

    elif(DirectionOfMoving[0] == "F" and DirectionOfMoving[1] == 1):

        posetionLeft[0] = posetionLeft[0] + (distanceTaken/2.0)
        #posetionRight[0] = posetionRight[0] + (distanceTaken/2.0)

    elif(DirectionOfMoving[0] == "F" and DirectionOfMoving[1] == -1):

        posetionLeft[0] = posetionLeft[0] - (distanceTaken/2.0)
        #posetionRight[0] = posetionRight[0] - (distanceTaken/2.0)

    elif(DirectionOfMoving[0] == "B" and DirectionOfMoving[1] == 0):
        
        posetionLeft[2] = posetionLeft[2] + (distanceTaken/2.0)
        #posetionRight[2] = posetionRight[2] + (distanceTaken/2.0)

def settingPostionOfBoxRight( distanceTaken ):
    global posetionLeft
    global posetionRight
    if(DirectionOfMoving[0] == "F" and DirectionOfMoving[1] == 0):

       #posetionLeft[2] = posetionLeft[2] - (distanceTaken/2.0)
        posetionRight[2] = posetionRight[2] - (distanceTaken/2.0)

    elif(DirectionOfMoving[0] == "F" and DirectionOfMoving[1] == 1):

        #posetionLeft[0] = posetionLeft[0] + (distanceTaken/2.0)
        posetionRight[0] = posetionRight[0] + (distanceTaken/2.0)

    elif(DirectionOfMoving[0] == "F" and DirectionOfMoving[1] == -1):

        #posetionLeft[0] = posetionLeft[0] - (distanceTaken/2.0)
        posetionRight[0] = posetionRight[0] - (distanceTaken/2.0)

    elif(DirectionOfMoving[0] == "B" and DirectionOfMoving[1] == 0):
        
        #posetionLeft[2] = posetionLeft[2] + (distanceTaken/2.0)
        posetionRight[2] = posetionRight[2] + (distanceTaken/2.0)

    
def initalization(leftDistance , rightDistance):
    global average
    average = (leftDistance + rightDistance) /2.0

    if(DirectionOfMoving[0] == "F" and DirectionOfMoving[1] == 0):
        posetionLeft[0] = -average - (thicknesOfWalls/2.0)
        posetionRight[0] = average + (thicknesOfWalls/2.0)
    elif(DirectionOfMoving[0] == "F" and DirectionOfMoving[1] == 1):
        posetionLeft[2] = -average - (thicknesOfWalls/2.0)
        posetionRight[2] = average + (thicknesOfWalls/2.0)
    elif(DirectionOfMoving[0] == "F" and DirectionOfMoving[1] == -1):
        posetionLeft[2] = average + (thicknesOfWalls/2.0)
        posetionRight[2] = -average - (thicknesOfWalls/2.0)
    elif(DirectionOfMoving[0] == "B" and DirectionOfMoving[1] == 0):
        posetionLeft[0] = average + (thicknesOfWalls/2.0)
        posetionRight[0]= -average - (thicknesOfWalls/2.0)

def transitions(leftDistance,frontDistance,rightDistance,direction ):
        previousDirectionOfMoving = ["F",1]
        for i in range (0,2):
            previousDirectionOfMoving[i] = DirectionOfMoving[i]
        determineDerictionOFMoving(direction)

        if(previousDirectionOfMoving[0] == "F" and previousDirectionOfMoving[1] == 0):
            if(DirectionOfMoving[1] == 1):
                box(pos = ( posetionLeft[0] + (leftDistance / 2.0),heightOfWalls/2.0 ,posetionLeft[2]-frontDistance - (thicknesOfWalls/2.0) ) , 
                    color = color.red ,  
                    size = ( leftDistance, heightOfWalls, thicknesOfWalls))
                posetionLeft[2] = posetionLeft[2] - frontDistance/2.0
                box(pos = posetionLeft , color = color.red , size = (thicknesOfWalls , heightOfWalls , frontDistance))
                posetionLeft[2] = posetionLeft[2] - frontDistance/2.0 - thicknesOfWalls/2.0
                posetionLeft[0] = posetionLeft[0] + leftDistance + thicknesOfWalls/2.0
                x = (posetionRight[0]+(thicknesOfWalls/2.0) + posetionLeft[0]) /2.0
                posetionLeft[0] = x
                x = (abs(posetionRight[0]-(thicknesOfWalls/2.0)) - abs(posetionLeft[0])) 
                boxesDrawingleft(0,0,abs(x) + 8*thicknesOfWalls)
          

            elif(DirectionOfMoving[1] == -1):
                box         (pos = (posetionRight[0]-(rightDistance/2.0) , heightOfWalls/2.0 ,posetionRight[2] -frontDistance - (thicknesOfWalls/2.0)),
                                color = color.blue,
                                size = (rightDistance , heightOfWalls , thicknesOfWalls) )
                posetionRight[2] = posetionRight[2] - frontDistance/2.0
                box         (pos = posetionRight , color = color.blue  , size = (thicknesOfWalls , heightOfWalls , frontDistance))
                posetionRight[2] = posetionRight[2] - frontDistance/2.0 - thicknesOfWalls/2.0
                posetionRight[0] = posetionRight[0] - rightDistance
                x = (posetionRight[0] + posetionLeft[0]-(thicknesOfWalls/2.0))/2.0
                posetionRight[0] = x
                x = (posetionRight[0]-(thicknesOfWalls/2.0) - posetionLeft[0]) /2.0
                boxesDrawingRight(0,0,abs(2*x) + 8*thicknesOfWalls)
        elif(previousDirectionOfMoving[0] == "F" and previousDirectionOfMoving[1] == 1):
            if(DirectionOfMoving[1] == 0 and DirectionOfMoving[0] == "F"):
                box         (pos = (posetionRight[0] +frontDistance + (thicknesOfWalls/2.0) , heightOfWalls/2.0 ,posetionRight[2]-(rightDistance/2.0)),
                                color = color.blue,
                                size = (thicknesOfWalls , heightOfWalls , rightDistance) )
                posetionRight[0] = posetionRight[0] + frontDistance/2.0
                box         (pos = posetionRight , color = color.blue  , size = (frontDistance , heightOfWalls , thicknesOfWalls))
                posetionRight[0] = posetionRight[0] + frontDistance/2.0 + thicknesOfWalls/2.0
                posetionRight[2] = posetionRight[2] - rightDistance
                z = (posetionRight[2] + posetionLeft[2]-(thicknesOfWalls/2.0))/2.0
                posetionRight[2] = z
                z = (posetionRight[2] - posetionLeft[2]-(thicknesOfWalls/2.0))/2.0
                boxesDrawingRight(0,0,abs(2*z) + 8*thicknesOfWalls )            
            elif(DirectionOfMoving[1] == 0 and DirectionOfMoving[0] == "B"): 
                print("hey")
                box(pos = (posetionLeft[0] + frontDistance + (thicknesOfWalls/2.0),heightOfWalls/2.0 , posetionLeft[2] + (leftDistance / 2.0) ) ,
                    color = color.red ,  
                    size = ( thicknesOfWalls, heightOfWalls, leftDistance))
                posetionLeft[0] = posetionLeft[0] + frontDistance/2.0
                box(pos = posetionLeft , color = color.red , size = (frontDistance , heightOfWalls , thicknesOfWalls))
                posetionLeft[0] = posetionLeft[0] + frontDistance/2.0 + thicknesOfWalls/2.0
                posetionLeft[2] = posetionLeft[2] + leftDistance + thicknesOfWalls/2.0
                z = (posetionRight[2]+(thicknesOfWalls/2.0) + posetionLeft[2]) /2.0
                posetionLeft[2] = z
                z = (posetionRight[2]+(thicknesOfWalls/2.0) - posetionLeft[2]) 
                boxesDrawingleft(0,0,abs(z) + 8*thicknesOfWalls)
        elif(previousDirectionOfMoving[0] == "F" and previousDirectionOfMoving[1] == -1):
            if(DirectionOfMoving[1] == 0 and DirectionOfMoving[0] == "B"):
                box         (pos = (posetionRight[0] -frontDistance - (thicknesOfWalls/2.0) , heightOfWalls/2.0 ,posetionRight[2]+(rightDistance/2.0)),
                                color = color.blue,
                                size = (thicknesOfWalls , heightOfWalls , rightDistance) )
                posetionRight[0] = posetionRight[0] - frontDistance/2.0
                box         (pos = posetionRight , color = color.blue  , size = (frontDistance , heightOfWalls , thicknesOfWalls))
                posetionRight[0] = posetionRight[0] - frontDistance/2.0 - thicknesOfWalls/2.0
                posetionRight[2] = posetionRight[2] + rightDistance + thicknesOfWalls/2.0
                z = (posetionRight[2] + posetionLeft[2]-(thicknesOfWalls/2.0))/2.0
                posetionRight[2] = z
                z = (posetionRight[2] - posetionLeft[2]-(thicknesOfWalls/2.0))/2.0
                boxesDrawingRight(0,0,abs(2*z) + 8*thicknesOfWalls )
            elif(DirectionOfMoving[1] == 0 and DirectionOfMoving[0] == "F"): 
                print("hey")
                box(pos = (posetionLeft[0] - frontDistance - (thicknesOfWalls/2.0),heightOfWalls/2.0 , posetionLeft[2] - (leftDistance / 2.0) ) ,
                    color = color.red ,  
                    size = ( thicknesOfWalls, heightOfWalls, leftDistance))
                posetionLeft[0] = posetionLeft[0] - frontDistance/2.0
                box(pos = posetionLeft , color = color.red , size = (frontDistance , heightOfWalls , thicknesOfWalls))
                posetionLeft[0] = posetionLeft[0] - frontDistance/2.0 - thicknesOfWalls/2.0
                posetionLeft[2] = posetionLeft[2] - leftDistance - thicknesOfWalls/2.0
                z = (posetionRight[2]+(thicknesOfWalls/2.0) + posetionLeft[2]) /2.0
                posetionLeft[2] = z
                z = (posetionRight[2]+(thicknesOfWalls/2.0) - posetionLeft[2]) 
                boxesDrawingleft(0,0,abs(z) + 8*thicknesOfWalls)
        elif(previousDirectionOfMoving[0] == "B" and previousDirectionOfMoving[1] == 0):
            if(DirectionOfMoving[1] == 1 and DirectionOfMoving[0] == "F" ):
                box         (pos = (posetionRight[0]+(rightDistance/2.0) , heightOfWalls/2.0 ,posetionRight[2] +frontDistance + (thicknesOfWalls/2.0)),
                                color = color.blue,
                                size = (rightDistance , heightOfWalls , thicknesOfWalls) )
                posetionRight[2] = posetionRight[2] + frontDistance/2.0
                box         (pos = posetionRight , color = color.blue  , size = (thicknesOfWalls , heightOfWalls , frontDistance))
                posetionRight[2] = posetionRight[2] + frontDistance/2.0 + thicknesOfWalls/2.0
                posetionRight[0] = posetionRight[0] + rightDistance
                x = (posetionRight[0] + posetionLeft[0]-(thicknesOfWalls/2.0))/2.0
                posetionRight[0] = x
                x = (posetionRight[0]-(thicknesOfWalls/2.0) - posetionLeft[0]) /2.0
                boxesDrawingRight(0,0,abs(2*x) + 8*thicknesOfWalls)
            elif(DirectionOfMoving[1] == -1 and DirectionOfMoving[0] == "F" ):
                box(pos = ( posetionLeft[0] - (leftDistance / 2.0),heightOfWalls/2.0 ,posetionLeft[2]+frontDistance + (thicknesOfWalls/2.0) ) , 
                    color = color.red ,  
                    size = ( leftDistance, heightOfWalls, thicknesOfWalls))
                posetionLeft[2] = posetionLeft[2] + frontDistance/2.0
                box(pos = posetionLeft , color = color.red , size = (thicknesOfWalls , heightOfWalls , frontDistance))
                posetionLeft[2] = posetionLeft[2] + frontDistance/2.0 + thicknesOfWalls/2.0
                posetionLeft[0] = posetionLeft[0] - leftDistance - thicknesOfWalls/2.0
                x = (posetionRight[0]+(thicknesOfWalls/2.0) + posetionLeft[0]) /2.0
                posetionLeft[0] = x
                x = (abs(posetionRight[0]-(thicknesOfWalls/2.0)) - abs(posetionLeft[0])) 
                boxesDrawingleft(0,0,abs(x) + 8*thicknesOfWalls)



def boxesDrawingleft(leftDistance , rightDistance , DistancTaken ):
    rightbox = None
    if(DirectionOfMoving[0] == "F" and DirectionOfMoving[1] == 0):
        boxesDrawingleft = box(pos = posetionLeft , color = color.red , size = (thicknesOfWalls,heightOfWalls,DistancTaken))
        #box(pos = posetionRight , color = color.blue , size = (thicknesOfWalls,heightOfWalls,DistancTaken))
    elif(DirectionOfMoving[0] == "F" and DirectionOfMoving[1] == 1):
        boxesDrawingleft = box(pos = posetionLeft , color = color.red , size = (DistancTaken,heightOfWalls,thicknesOfWalls))
        #box(pos = posetionRight , color = color.blue , size = (DistancTaken,heightOfWalls,thicknesOfWalls))
    elif(DirectionOfMoving[0] == "F" and DirectionOfMoving[1] == -1):
        boxesDrawingleft = box(pos = posetionLeft , color = color.red , size = (DistancTaken,heightOfWalls,thicknesOfWalls))
        #box(pos = posetionRight , color = color.blue , size = (DistancTaken,heightOfWalls,thicknesOfWalls))
    elif(DirectionOfMoving[0] == "B" and DirectionOfMoving[1] == 0):
        boxesDrawingleft = box(pos = posetionLeft , color = color.red , size = (thicknesOfWalls,heightOfWalls,DistancTaken))
        #box(pos = posetionRight , color = color.blue , size = (thicknesOfWalls,heightOfWalls,DistancTaken))
    return boxesDrawingleft
def boxesDrawingRight(leftDistance , rightDistance , DistancTaken ):
    boxesDrawingRight = None
    if(DirectionOfMoving[0] == "F" and DirectionOfMoving[1] == 0):
        #box(pos = posetionLeft , color = color.red , size = (thicknesOfWalls,heightOfWalls,DistancTaken))
        boxesDrawingRight = box(pos = posetionRight , color = color.blue , size = (thicknesOfWalls,heightOfWalls,DistancTaken))
    elif(DirectionOfMoving[0] == "F" and DirectionOfMoving[1] == 1):
        #box(pos = posetionLeft , color = color.red , size = (DistancTaken,heightOfWalls,thicknesOfWalls))
        boxesDrawingRight = box(pos = posetionRight , color = color.blue , size = (DistancTaken,heightOfWalls,thicknesOfWalls))
    elif(DirectionOfMoving[0] == "F" and DirectionOfMoving[1] == -1):
        #box(pos = posetionLeft , color = color.red , size = (DistancTaken,heightOfWalls,thicknesOfWalls))
        boxesDrawingRight = box(pos = posetionRight , color = color.blue , size = (DistancTaken,heightOfWalls,thicknesOfWalls))
    elif(DirectionOfMoving[0] == "B" and DirectionOfMoving[1] == 0):
        #box(pos = posetionLeft , color = color.red , size = (thicknesOfWalls,heightOfWalls,DistancTaken))
        boxesDrawingRight = box(pos = posetionRight , color = color.blue , size = (thicknesOfWalls,heightOfWalls,DistancTaken))
    return boxesDrawingRight



def mainDraw(leftDistance  , rightDistance , DistancTaken, frontDistance =0 , direction = " "):
    global firstPieaceOfData
    if(firstPieaceOfData == True):
        initalization(leftDistance , rightDistance)
        firstPieaceOfData = False
    
    if(direction == "L" or direction == "R"):
        transitions(leftDistance,frontDistance,rightDistance,direction)
    else:
        settingPostionOfBoxLeft(DistancTaken)
        settingPostionOfBoxRight(DistancTaken)
        l = boxesDrawingleft(leftDistance , rightDistance , DistancTaken );
        r = boxesDrawingRight(leftDistance , rightDistance , DistancTaken );
        settingPostionOfBoxLeft(DistancTaken)
        settingPostionOfBoxRight(DistancTaken)
        savingFiles([l,r])

for x in range(1,20):
    mainDraw(2,2,3)
mainDraw(2,2,3 , 5 , "R")
for x in range(1,20):
    mainDraw(2,2,3)
mainDraw(2,2,3,3,"L")
for x in range(1,10):
    mainDraw(2,2,3)

convertingToPythonFile()




        

