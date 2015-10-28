import api
import ctypes


def Run():
   api.Walk(True)
   print ('stand up')
   Run()
if __name__ == "__main__":
	api.Initialize()
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
	Run()
