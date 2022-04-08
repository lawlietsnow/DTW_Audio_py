from scipy.io import wavfile
import noisereduce as nr
# load data
rate, data = wavfile.read("mjRecord2.wav")
# perform noise reduction
reduced_noise = nr.reduce_noise(y=data, sr=rate)
wavfile.write("mywav_reduced_noise2.wav", rate, reduced_noise)