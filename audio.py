import numpy as np
import wave

def audioToMFCC(path):
	ifile = wave.open(path)
	samples = ifile.getnframes()
	audio = ifile.readframes(samples)

	# Convert buffer to float32 using NumPy                                                                                 
	audio_as_np_int16 = np.frombuffer(audio, dtype=np.int16)
	audio_as_np_float32 = audio_as_np_int16.astype(np.float32)
	                                                     
	max_int16 = 2**15
	audio_normalised = audio_as_np_float32 / max_int16
	return list(audio_normalised)
def reduceData(li):
	numItems = 5000
	if(len(li) <= numItems): 
		return li
	print(type(li))
	l = list()
	step = int(len(li) / numItems)
	for x in range(numItems):
		l.append(li[x*step])
	return l


# We define two sequences x, y as numpy array
# where y is actually a sub-sequence from x
x = audioToMFCC("./mywav_reduced_noise.wav")
print(len(x))
y = audioToMFCC("./mywav_reduced_noise2.wav")
print(len(y))

x = reduceData(x)
y = reduceData(y)
print(len(x))
print(len(y))

from dtw import dtw

manhattan_distance = lambda x, y: np.abs(x - y)

d, cost_matrix, acc_cost_matrix, path = dtw(x, y, dist=manhattan_distance)

print("cost: ",d)
# >>> 2.0 # Only the cost for the insertions is kept

# You can also visualise the accumulated cost and the shortest path
import matplotlib.pyplot as plt

plt.imshow(acc_cost_matrix.T, origin='lower', cmap='gray', interpolation='nearest')
plt.plot(path[0], path[1], 'w')
plt.show()