import wave
import numpy 
                                                                                             
ifile = wave.open("./mjRecord2.wav")
samples = ifile.getnframes()
audio = ifile.readframes(samples)

# Convert buffer to float32 using NumPy                                                                                 
audio_as_np_int16 = numpy.frombuffer(audio, dtype=numpy.int16)
audio_as_np_float32 = audio_as_np_int16.astype(numpy.float32)
                                                     
max_int16 = 2**15
audio_normalised = audio_as_np_float32 / max_int16
print(audio_normalised)