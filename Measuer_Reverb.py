import numpy as np
import matplotlib.pyplot as plt


def calculate_rt60(signal, fs):
    # Calculate the energy decay curve (EDC)
    EDC = np.cumsum(signal[::-1] ** 2)[::-1]

    # Normalize the EDC
    EDC = EDC.astype(float)  # Convert to floating-point type
    EDC /= np.max(EDC)

    # Calculate the time vector
    time = np.arange(len(EDC)) / fs

    # Find the 60 dB decay point
    threshold = -60  # dB
    idx_rt60 = np.argmax(EDC <= threshold)

    # Interpolate to find the exact time
    rt60 = np.interp(threshold, 20 * np.log10(EDC), time)

    return rt60, time, EDC


# Example usage:
if __name__ == "__main__":
    # Load impulse response from a WAV file (make sure to replace 'your_file.wav' with your file path)
    from scipy.io import wavfile

    fs, ir = wavfile.read('Alla_magna.wav')

    # Calculate RT60
    rt60, time, EDC = calculate_rt60(ir, fs)

    # Plot the energy decay curve
    plt.plot(time, 20 * np.log10(EDC))
    plt.xlabel('Time (s)')
    plt.ylabel('Energy (dB)')
    plt.title('Energy Decay Curve')
    plt.grid(True)
    plt.show()

    print(f"RT60: {rt60:.3f} seconds")

