import numpy as np
from scipy import signal
import librosa
import matplotlib.pyplot as plt



def stft(data, window=1024, step=512):
    win_fc = signal.hamming(window)
    for i in range((data.shape[0] - window) // step):
        tmp = data[i*step : i*step + window]
        tmp = tmp * win_fc
        tmp = np.fft.fft(tmp)
        z.append(tmp)
    z  = np.array(z)

    return z

def main():
    path = "/Users/yamanoishu/Downloads/aiueo.wav"
    wav, sr = librosa.load(path, sr=48000)
    ampList = stft(wav)
    plt.xlim([0, len(ampList)])
    plt.imshow(np.abs(ampList[:, : ampList.shape[0]/2+1].T), aspect = "auto", origin = "lower")
    plt.show()

main()





