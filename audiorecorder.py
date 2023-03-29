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
    filepath = OUTPUT_FOLDER+filename+".wav"

    print(f"\nDevice name is", device["name"])
    print("Device channels is", device["max_input_channels"])
    print("Sample Rate is", str(SAMPLE_RATE))
    print("File Name is", filename)
    print("File Path is", filepath)

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

    device = get_info_device()

    file_name = filename()

    get_ready(device, file_name)

if __name__ == "__main__":
    main()