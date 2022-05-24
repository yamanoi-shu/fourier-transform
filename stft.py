import numpy as np
from scipy import signal
from pydub import AudioSegment
import matplotlib.pyplot as plt
import os



def stft(data, window=1024, step=512):
    win_fc = signal.hamming(window)
    z = []
    for i in range((data.shape[0] - window) // step):
        tmp = data[i*step : i*step + window]
        tmp = tmp * win_fc
        tmp = np.fft.fft(tmp)
        z.append(tmp)
    z  = np.array(z)

    return z

def main():
    wd = os.getcwd()
    path = wd + "/aiueo.wav"
    wav = AudioSegment.from_file(path, format="wav")

    data = np.array(wav.get_array_of_samples())

    ampList = stft(data)

    plt.xlim([0, len(ampList)])
    plt.imshow(np.abs(ampList[:, : ampList.shape[0]//2+1].T), aspect = "auto", origin = "lower")
    plt.show()

main()


