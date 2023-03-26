from pvrecorder import PvRecorder

def main():
    for index, device in enumerate(PvRecorder.get_audio_devices()):
        print(f"[{index}] {device}")

if __name__ == "__main__":
    main()