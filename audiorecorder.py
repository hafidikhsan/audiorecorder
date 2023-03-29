import sys
import os
import sounddevice as sd
import soundfile as sf
from queue import Queue

SAMPLE_RATE = 24000
OUTPUT_FOLDER = os.path.join("sound")

q = Queue()

def intro():
    print(f"****************************** Recording Audio ******************************")
    print(f"* by Hafid Ikhsan Arifin                                                    *")
    print(f"*****************************************************************************")

def get_avail_device():
    print(f"\nDevice available:")
    print(sd.query_devices())

def get_info_device():
    print(f"\n* Choose input device (1/2 in, 0 out)")
    print(f"* Default microphone (>)")
    try:
        device = int(input(f"\nDevice: "))

        device_info = sd.query_devices()

    except ValueError:
        sys.exit("Input device must be integer (1/2/3/..)")

    if device < len(device_info):
        print(f"\nDevice info:")

        device =  device_info[int(device)]
        device_name = device["name"]
        device_channels = device["max_input_channels"]

        print("Device name:", device_name)
        print("Device input channels:", device_channels, "(Mono)" if device_channels==1 else "(Stereo)")

        return device

    else:
        sys.exit("Device is index out of range")

def filename():
    filename = input(f"\nFile name: ")

    return filename

def get_ready(device, filename):
    filename = filename+".wav"

    print(f"\nDevice name is", device["name"])
    print("Device channels is", device["max_input_channels"])
    print("Sample Rate is", str(SAMPLE_RATE))
    print("File Name is", filename)
    print("File Path is", os.path.join(OUTPUT_FOLDER, filename))

    print(f"\n=======================")
    print(f"Get ready for recording")
    print(f"=======================\n")

    confirmation = input("Type (Y/y) if you ready: ")

    if confirmation=="y" or confirmation=="Y":
        recording(device, filename)
    else:
        sys.exit("Opps, process aborted")

def callback(indata, frames, time, status):
    if status:
        print(f"\nRecording...\n", flush=True)
    q.put(indata.copy())

def recording(device, filename):
    try:
        with sf.SoundFile(os.path.join(OUTPUT_FOLDER, filename), mode='x', samplerate=SAMPLE_RATE,
                        channels=device["max_input_channels"], subtype="PCM_16") as file:
            with sd.InputStream(samplerate=SAMPLE_RATE, device=device["name"],
                                channels=device["max_input_channels"], callback=callback):
                print('*' * 80)
                print(f"\nGet ready for recording...")
                print(f"Control + C for stop recording\n")
                print('*' * 80)
                while True:
                    file.write(q.get())
    except KeyboardInterrupt:
        sys.exit(f"\nYes, Recording finished")
    except Exception as e:
        sys.exit(f"\nOpss, Something went wrong:", str(e))

def main():
    get_avail_device()

    device = get_info_device()

    file_name = filename()

    get_ready(device, file_name)

if __name__ == "__main__":
    main()