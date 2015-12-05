#import ctypes
import api
#import os 
#import time 
import sys
#import struct

from pixy import *
from ctypes import *


speedInc=0
timer = 0

def RoboWalk(color, trackX):   # X,Y are the center of the object that is deteced by pixy, color green move, color red stop
    global sit, walk, speedInc, timer
 #   timer = timer +1
  #  print  timer
    if (color == 'green') and (walk == False): #if the color is green and the robot is not walking let it walk

        api.Walk(True)       # set the robot in walk ready mode
        if (timer<1000):
#		speedInc = 2
	elif ((timer>=1000) and (timer <2000)):
#		speedInc = 6
	elif ((timer>=2000) and (timer <4000)):
#		speedInc = 8
	elif (timer >=4000):
#		speedInc = 13
	speed =10
        api.WalkMove(speed)  #the robot start to move for the given speed
        walk = True          #indicate that the robot is walikg
        sit=0                #flag that the robot is not in sit position
        #HeadMove = False     
    elif (color == 'red') and (walk == True):  #
       walk = False         #indicate that the robot not walking
       if (sit == 0):       #if the robot is not in sit position make it sit
        api.Walk(False)    #stop the walk ready mode
        api.PlayAction(15) #call the sit position - page 15
        sit=1              # flag that the robot is in sit position

#def RoboTurn(trackX):
    # Turn while walking
    if (walk == True): #if the robot is walking check the direction 
        if (trackX>10):
    	    api.WalkTurn(-5)
	    
	    print 'left'
        elif(trackX<-10):
            api.WalkTurn(5)
	    print 'right'
        else :
            api.WalkTurn(0)
#	End of RoboWalk()

def RoboInit():
    try:
                if api.Initialize():
                        print("Initalized")
                else:
                        print("Intialization failed")

    except (KeyboardInterrupt):
                api.ServoShutdown()
                sys.exit()
    except():
        api.ServoShutdown()
        sys.exit()

# End of RoboInit()
# set the Global variables
def centerX(x):
	return x-160

sit = 0
walk = False
X=0  # 0 - 320
color = 'red'

#initialize Pixy interpreter thread
pixy_init()

#initialize the Robot movements
RoboInit()

#Blocks
class Blocks (Structure):
      _fields_ = [ ("type", c_uint),
                   ("signature", c_uint),
                   ("x", c_uint),
                   ("y", c_uint),
                   ("width", c_uint),
                   ("height", c_uint),
                   ("angle", c_uint) ]

blocks = BlockArray(100)
frame = 0
battryLim = 107
#wait for blocks
try:
  while 1:
     count = pixy_get_blocks(100, blocks)
     if (int(api.BatteryVoltLevel()) <= battryLim):
      if (int(api.BatteryVoltLevel()) <= battryLim):
       if (int(api.BatteryVoltLevel()) <= battryLim):

	print 'Low Battery'
	api.Walk(False)
	api.PlayAction(15)
	api.ServoShutdown()
	sys.exit()
     else:
#       print 'Battery power', int(api.BatteryVoltLevel())
       if count > 0:
#	 print 'count' , count
	 #print 'block' , blocks
         #blocks found
         #print 'frame %3d:' % (frame)
         frame = frame +1
         for index in range(0, count):
	     
             #print '[Block_type=%d  Sig=%d  X=%3d  Y=%3d   W=%3d   H=%3d]' % (blocks[index].type, blocks[index].signature, blocks[index].x, blocks[index].y, blocks[index].width, blocks[index].height)
             if ((blocks[index].signature == 4) or (blocks[index].signature == 4)):
             # detect the screen color (green)
#		print 'start'
		#x=blocks[index].x
		#y=blocks[index].y
		color = 'green'
             if (blocks[index].signature == 1):
             # detect the screen color (red)
#		print 'stop'
		#x=blocks[index].x
		#y=blocks[index].y
		color='red'
#		speedInc = 0
#		timer = 0
	     if (((blocks[index].signature == 4) or (blocks[index].signature == 4)) and (walk == True)):
#		print 'track'
		X = centerX(blocks[index].x)
		print 'X track', X
#		RoboTurn(Y)	 

    #call the walk function
	     RoboWalk(color, X)
except (KeyboardInterrupt):
   api.ServoShutdown()
   sys.exit()
