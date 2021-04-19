import sounddevice as sd
import numpy as np

threshold = 1.420
intensity_metric = 1
# print(intensity_metric)


def print_sound(indata, outdata, frames, time, status):
	global intensity_metric
	volume_norm = np.linalg.norm(indata)*10
	intensity_metric = max(intensity_metric, volume_norm)
	print(volume_norm)
	# print(intensity_metric)


def normalize(a):
	lim = 8.69
	return float(a/lim)

def run():
	with sd.Stream(callback=print_sound):
		sd.sleep(3000)
		print("max value --> ",normalize(intensity_metric))

		
run()
