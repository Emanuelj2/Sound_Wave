import pyaudio
import wave

FRAMES_PER_BUFFER = 3200
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 1600

p = pyaudio.PyAudio()

stream = p.open(
    format=FORMAT
    , channels=CHANNELS
    , rate=RATE
    , input=True
    , frames_per_buffer=FRAMES_PER_BUFFER
)

print("Start recording")

seconds = 3
frames = []
for i in range(0, int(RATE/FRAMES_PER_BUFFER * seconds)):
    data = stream.read(FRAMES_PER_BUFFER)
    frames.append(data)

stream.stop_stream()
stream.close()
p.terminate()


object = wave.open("record.wav", "wb")
object.setnchannels(CHANNELS)
object.setsampwidth(p.get_sample_size(FORMAT))
object.setframerate(RATE)
object.writeframes(b"".join(frames))
object.close()

