import sys
import sounddevice as sd
import soundfile as sf

SAMPLE_RATE = 24000
OUTPUT_FOLDER = "/sound/"

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

        device_name = device_info[int(device)]["name"]
        device_channels = device_info[int(device)]["max_input_channels"]

        print("Device name:", device_name)
        print("Device input channels:", device_channels, "(Mono)" if device_channels==1 else "(Stereo)")

    else:
        sys.exit("Device is index out of range")
        

def get_ready():
    print(f"\n=======================")
    print(f"Get ready for recording")
    print(f"=======================\n")

    confirmation = input("Type (Y/y) if you ready: ")

    if confirmation=="y" or confirmation=="Y":
        recording()
    else:
        sys.exit("Opps, process aborted")

def recording():
    print("recording")

def main():
    get_avail_device()

    get_info_device()

    get_ready()

if __name__ == "__main__":
    main()