import pyaudio
import numpy as np

p = pyaudio.PyAudio()

def play_audio(freq):
    volume = 1    
    fs = 44100      
    duration = 1.0   
    f = freq  

    samples = (np.sin(2*np.pi*np.arange(fs*duration)*f/fs + f)).astype(np.float32)

    stream = p.open(format=pyaudio.paFloat32,
                    channels=1,
                    rate=fs,
                    output=True)

    stream.write(volume*samples)

    stream.stop_stream()

    stream.close()



p.terminate()