import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
import soundfile as sf
from scipy.signal import welch

# Read the audio file and get its data and sample rate
data, samplerate = sf.read('Alla_magna.wav')

# Calculate the duration of the audio in seconds
duration = len(data) / samplerate

# Create a time array using np.linspace()
time = np.linspace(0, duration, len(data))

# Check if the audio has multiple channels
if data.ndim == 1:  # If it's a mono audio
    plt.plot(time, data, label='mono audio')
else:  # If it's a stereo audio
    plt.plot(time, data[:, 0], label='left channel')
    plt.plot(time, data[:, 1], label='right channel')

plt.legend()
plt.title("Mono Audio")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.show()

# Calculate the spectrogram
spectrum, freqs, t, im = plt.specgram(data, Fs=samplerate, NFFT=1024, cmap=plt.get_cmap('jet'))
cbar = plt.colorbar(im)
plt.title("Spectrogram")
plt.xlabel('Time (s)')
plt.ylabel('Frequency (Hz)')
cbar.set_label('Intensity (dB)')
plt.show()

# Select a frequency under 1kHz
def find_target_frequency(freqs):
    for x in freqs:
        if x > 1000:
            break
    return x

target_frequency = find_target_frequency(freqs)
index_of_frequency = np.where(freqs == target_frequency)[0][0]
data_for_frequency = spectrum[index_of_frequency]
data_in_db = 10 * np.log10(data_for_frequency)

plt.figure(2)
plt.plot(t, data_in_db, linewidth=1, alpha=0.7, color='#004bc6')
plt.xlabel('Time (s)')
plt.title('Frequency Response')
plt.ylabel('Power (dB)')

# Find the index of the maximum value
index_of_max = np.argmax(data_in_db)
value_of_max = data_in_db[index_of_max]
plt.plot(t[index_of_max], data_in_db[index_of_max], 'go')

# Slice the array from the maximum value
sliced_array = data_in_db[index_of_max:]
value_of_max_less_than_5 = value_of_max - 5

# Find the nearest value less than 5dB
value_of_max_less_5 = np.max(sliced_array[sliced_array <= value_of_max_less_than_5])
index_of_max_less_5 = np.where(data_in_db == value_of_max_less_5)[0][0]
plt.plot(t[index_of_max_less_5], data_in_db[index_of_max_less_5], 'yo')

# Slice array from max - 5dB
value_of_max_less_25 = value_of_max - 25
value_of_max_less_25 = np.max(sliced_array[sliced_array <= value_of_max_less_25])
index_of_max_less_25 = np.where(data_in_db == value_of_max_less_25)[0][0]
plt.plot(t[index_of_max_less_25], data_in_db[index_of_max_less_25], 'ro')

rt20 = (t[index_of_max_less_5] - t[index_of_max_less_25])

plt.grid()
plt.show()
rt60 = 3 * rt20

print(f'The RT60 reverb time at freq {int(target_frequency)}Hz is: {round(abs(rt60), 2)} seconds')

# frequency in sine wave


# Generate time values
t = np.arange(1.5, 1.75, 1/samplerate)  # Generate time values based on the sampling rate

# Generate sine wave based on the audio data
sine_wave = np.sin(2 * np.pi * 47 * t)  # Adjust frequency as needed

# Plot the sine wave
plt.plot(t, sine_wave)
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.title('Sine Wave')
plt.grid(True)
plt.show()

frequencies, power = welch(data, samplerate, nperseg=4096)

# Define frequency bands for low, mid, and high frequencies
low_band = (20, 250)   # Low frequency band (Hz)
mid_band = (250, 2000) # Mid frequency band (Hz)
high_band = (2000, 20000) # High frequency band (Hz)

# Calculate the corresponding indices for frequency bands
low_band_indices = np.where(np.logical_and(frequencies >= low_band[0], frequencies <= low_band[1]))[0]
mid_band_indices = np.where(np.logical_and(frequencies >= mid_band[0], frequencies <= mid_band[1]))[0]
high_band_indices = np.where(np.logical_and(frequencies >= high_band[0], frequencies <= high_band[1]))[0]

# Extract power values for each frequency band
power_low = power[low_band_indices]
power_mid = power[mid_band_indices]
power_high = power[high_band_indices]

# Plot power spectral density for each frequency band
plt.figure(figsize=(10, 6))

# Plot for low frequencies
plt.subplot(3, 1, 1)
plt.plot(frequencies[low_band_indices], power_low)
plt.title('Power Spectral Density - Low Frequencies')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Power')

# Plot for mid frequencies
plt.subplot(3, 1, 2)
plt.plot(frequencies[mid_band_indices], power_mid)
plt.title('Power Spectral Density - Mid Frequencies')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Power')

# Plot for high frequencies
plt.subplot(3, 1, 3)
plt.plot(frequencies[high_band_indices], power_high)
plt.title('Power Spectral Density - High Frequencies')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Power')

plt.tight_layout()
plt.show()

power_low = power[low_band_indices]
power_mid = power[mid_band_indices]
power_high = power[high_band_indices]

plt.figure(figsize=(10, 5))

# Plot for low frequencies
plt.plot(frequencies[low_band_indices], power_low, label='Low Frequencies')

# Plot for mid frequencies
plt.plot(frequencies[mid_band_indices], power_mid, label='Mid Frequencies')

# Plot for high frequencies
plt.plot(frequencies[high_band_indices], power_high, label='High Frequencies')


plt.title('Power Spectral Density')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Power')
plt.legend()
plt.grid(True)

plt.xlim(0, 3500)

plt.show()

