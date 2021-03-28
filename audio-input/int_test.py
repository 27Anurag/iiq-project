import sounddevice as sd
import numpy as np

threshold = 1

def print_sound(indata, outdata, frames, time, status):
    volume_norm = np.linalg.norm(indata)*10
    if(volume_norm>threshold):
    	print("Too loud!")
    else:
    	print(volume_norm)


with sd.Stream(callback=print_sound):
    sd.sleep(10000)