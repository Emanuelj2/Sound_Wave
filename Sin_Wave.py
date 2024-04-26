import matplotlib.pyplot as plt
import numpy as np
import soundfile as sf

# Read the audio file
data, samplerate = sf.read('Alla_magna.wav')

# Calculate the duration of the audio file
duration = len(data) / samplerate

# Generate time values
t = np.arange(.2, .25, 1/samplerate)  # Generate time values based on the sampling rate

# Generate sine wave based on the audio data
sine_wave = np.sin(2 * np.pi * 440 * t)  # Adjust frequency as needed

# Plot the sine wave
plt.plot(t, sine_wave)
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.title('Sine Wave')
plt.grid(True)
plt.show()
