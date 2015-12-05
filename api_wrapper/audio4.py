#!/usr/bin/python3
import sys
#appends api directory path to sys path
#sys.path.append("/home/pi/Human_Robots_Interaction_Fall15")

#!/usr/bin/python
import pyaudio
import audioop
import wave

import api

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

def RoboWalk(speed):
        global walk
        print 'Robo walking'
        api.Walk(True)
        api.WalkMove(speed)
        walk = True
# End of RoboWalk

def RoboStop():
        global walk
        print 'Robo stop and sitting'
        api.Walk(False)
        api.PlayAction(16)
        walk = False
# End of RoboStop


RoboInit()

CHUNK = 4096
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 48000
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "output.wav"
THRESHOLD = 600
walk = False


p = pyaudio.PyAudio()

for i in range(p.get_device_count()):
        dev = p.get_device_info_by_index(i)
        print((i, dev['name'],dev['maxInputChannels']))

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                input_device_index = 2,
                frames_per_buffer=CHUNK)

print("* recording")
try:
 while True:
    try:
        data = stream.read(CHUNK)
    except IOError as ex:
        stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                input_device_index = 2,
                frames_per_buffer=CHUNK)

        data = stream.read(CHUNK)

    rms = audioop.rms(data, 2)
    print(rms)
    if(rms>THRESHOLD):
        if (walk == True):
          print 'Robot stop Walking'
          RoboStop()

        else:
          print 'Robot start walking'
          RoboWalk(10)

except (KeyboardInterrupt):
        print 'stoped by user ...'
        stream.stop_stream()
        stream.close()
        p.terminate()
        api.ServoShutdown()
        sys.exit()


stream.stop_stream()
stream.close()
p.terminate()

