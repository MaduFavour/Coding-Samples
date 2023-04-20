import pyaudio
import numpy as np
import time
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle, Polygon

RATE = 44100

def analyze_audio_data(audio_data):
    fft_data = np.fft.fft(audio_data)
    freqs = np.fft.fftfreq(len(fft_data))
    idx = np.argmax(np.abs(fft_data))
    freq = abs(freqs[idx] * RATE)

    fig, axs = plt.subplots(1, 3)

    if 100 <= freq <= 400:
        circle = Circle((0.5, 0.5), 0.25)
        axs[0].add_artist(circle)
        axs[0].set_title("Circle")
    if 401 <= freq <= 800:
        triangle = Polygon([[0.5, 0.9], [0.1, 0.1], [0.9, 0.1]], closed=True)
        axs[1].add_artist(triangle)
        axs[1].set_title("Triangle")
    if freq > 800:
        square = Rectangle((0.25, 0.25), 0.5, 0.5)
        axs[2].add_artist(square)
        axs[2].set_title("Square")

    for ax in axs:
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
        ax.set_aspect('equal', adjustable='box')
        ax.axis('off')

    plt.show()

def record_and_analyze():
    # Set up the audio stream
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RECORD_SECONDS = 5  # Set the time frame for recording

    audio = pyaudio.PyAudio()
    stream = audio.open(format=FORMAT,
                        channels=CHANNELS,
                        rate=RATE,
                        input=True,
                        frames_per_buffer=CHUNK)

    print("Recording...")

    frames = []

    for _ in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        try:
            data = stream.read(CHUNK, exception_on_overflow=False)
            frames.append(np.frombuffer(data, dtype=np.int16))
        except IOError as e:
            print(f"Error while reading data from stream: {e}")

    print("Finished recording.")

    stream.stop_stream()
    stream.close()
    audio.terminate()

    audio_data = np.hstack(frames)
    analyze_audio_data(audio_data)


while True:
    record_and_analyze()
    user_input = input("Press 'q' to quit or any other key to run the program again: ")
    if user_input.lower() == 'q':
        break




