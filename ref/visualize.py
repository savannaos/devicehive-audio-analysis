import torchaudio
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

filename='dog-bark.wav'

waveform, sample_rate = torchaudio.load(filename)
print("Shape of waveform: {}".format(waveform.size()))
print("Sample rate of waveform: {}".format(sample_rate))
plt.figure()
plt.plot(waveform.t().numpy())
plt.savefig('waveform.png')

specgram = torchaudio.transforms.Spectrogram()(waveform)
print("Shape of spectrogram: {}".format(specgram.size()))

plt.figure()
plt.imshow(specgram.log2()[0,:,:].numpy(), cmap='gray')
plt.savefig('spectrogram.png')
