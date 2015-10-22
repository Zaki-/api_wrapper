#!/usr/bin/python3
import ctypes
import api
import os
import time
import sys
import struct

#Socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def Main():
	#api.ServoShutdown()
	try:
		if api.Initialize():
			print("Initalized")
		else:
			print("Intialization failed")
		#api.ServoShutdown()
		#api.PlayAction(8)
		global Socket
		#value = int(input("Turn head to"))
		#api.SetMotorValue(20, value)
	#Socket.sl_connect()
		print("Atempting to connect to socket")
		#Socket.connect(("10.0.0.112", 9001))
		print("Connected")
		#api.PlayAction(8)
		Run()
	except (KeyboardInterrupt):
		api.ServoShutdown()
		sys.exit()
	except():
		api.ServoShutdown()
		sys.exit()

def Run():
	global Socket
	#api.Walk(True)
	print("Running...")
	#packet = Socket.recv(8)
	print("Packet recieved")
	#command = struct.unpack('B', packet[1])[0]
	command = 0
	#move foward
	print(command)
	if(command == 6):
		api.WalkMove(0)
		api.Walk(True)
		api.WalkMove(20)
	#move back
	elif(command == 7):
		print("supposed to move backwards")
	#move right
	elif(command == 8):
		api.WalkMove(0)
		api.WalkTurn(20)
	#move left
	elif(command == 9):
		api.WalkMove(0)
		api.WalkTurn(-20)
	elif(command == 5):
		api.WalkMove(0)
	elif(command == 0):
		api.SetMotorValue(19,400)
#		api.SetMotorValue(20,500)
		print(api.GetMotorValue(19))

		print(api.GetMotorValue(20))
	api.ServoShutdown()
	
		
	#Run()

if __name__ == "__main__": Main()
