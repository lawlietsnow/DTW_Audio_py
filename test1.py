file1 = "E:/DTW_Audio_py/mjRecord1.wav"
file2= "E:/DTW_Audio_py/mjRecord2.wav"
import wave
import numpy as np
import matplotlib.pyplot as plt
#audio 1
signal_wave = wave.open(file1, 'r')
sample_rate = 16000
sig = np.frombuffer(signal_wave.readframes(sample_rate), dtype=np.int16)
sig = sig[25000:32000]
plt.figure(1)

plot_a = plt.subplot(211)
plot_a.plot(sig)
plot_a.set_xlabel('sample rate * time')
plot_a.set_ylabel('energy')

#audio 2
signal_wave2 = wave.open(file2, 'r')
sample_rate2 = 16000
sig2 = np.frombuffer(signal_wave2.readframes(sample_rate), dtype=np.int16)
sig2 = sig2[25000:32000]
plt.figure(1)

plot_a2 = plt.subplot(212)
plot_a2.plot(sig2)
plot_a2.set_xlabel('sample rate * time')
plot_a2.set_ylabel('energy')

plt.show()