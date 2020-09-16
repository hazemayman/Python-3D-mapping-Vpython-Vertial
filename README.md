# Python-3D-mapping-Vpython-Vertial
using python and VPython vertual to create 3d mapping to draw any maze on computer 
# How it works
there are 2 main functions you have to know how to use : 
- first function is mainDraw() function which takes three necessary arguments and two optional
mainDraw(leftDistance  , rightDistance , DistancTaken, frontDistance =0 , direction = " ") , the last two arguments frontDistance takes the distance in front of the RC car and the direction argument
takes 'R' or 'L' for the RC to turn
- second function is convertingToPythonFile() which is optional when you use it another file will be created containg just the drawing code so that you can take it anywhere or jsonfiy it and send it to servers
and this will allow you to use the mainDraw function as the process algorithm and you will have the actual 3D map on other file 
