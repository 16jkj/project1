#start here
import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

# Original audio file
audio_file1 = "inputAudiofile.wav"
sr, y1 = wavfile.read(audio_file1)
y1 = y1[:, 0]  # Take only one channel (assuming it's a stereo audio)

# Denoised audio file
audio_file2 = "input_denoised.wav"
sr, y2 = wavfile.read(audio_file2)
y2 = y2[:, 0]  # Take only one channel (assuming it's a stereo audio)

# Create subplots for waveform and spectrogram
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(14, 10))

# Waveform plot - Original
axes[0, 0].plot(np.arange(len(y1)) / sr, y1, color='blue')
axes[0, 0].set_title('Waveform - Original')
axes[0, 0].set_xlabel('Time (s)')
axes[0, 0].set_ylabel('Amplitude')

# Spectrogram plot - Original
axes[0, 1].specgram(y1, Fs=sr, cmap='coolwarm')
axes[0, 1].set_title('Spectrogram - Original')
axes[0, 1].set_xlabel('Time (s)')
axes[0, 1].set_ylabel('Frequency')

# Waveform plot - Denoised
axes[1, 0].plot(np.arange(len(y2)) / sr, y2, color='red', linestyle='--')
axes[1, 0].set_title('Waveform - Denoised')
axes[1, 0].set_xlabel('Time (s)')
axes[1, 0].set_ylabel('Amplitude')

# Spectrogram plot - Denoised
axes[1, 1].specgram(y2, Fs=sr, cmap='coolwarm')
axes[1, 1].set_title('Spectrogram - Denoised')
axes[1, 1].set_xlabel('Time (s)')
axes[1, 1].set_ylabel('Frequency')

plt.tight_layout()
plt.show()

#end here