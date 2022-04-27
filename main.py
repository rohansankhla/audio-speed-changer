import easygui
from playsound import playsound
import soundfile as sf
from scipy.io import wavfile


def read_wav():
    # Checks if the audio file is in .wav format
    checker_list = [".wav"]
    file = easygui.fileopenbox()
    string_length = len(file)
    a = file[(string_length - 4):string_length]
    while a not in checker_list:
        print("Only .wav files allowed. PLease choose a different file.")
        file = easygui.fileopenbox()
        string_length = len(file)
        a = file[(string_length - 4):string_length]

    # Edits the file path name to include two backslashes after the directory disk name
    first_three = file[0:3]
    new_start = first_three[0:2] + "\\\\"
    file = new_start + file[3:]
    return file


def speed_change(file):
    # Finds the data and sample rate of the audio file
    data, samplerate = sf.read(file)

    # Adjusts the speed of the audio file and downloads it as a new file in the same directory of the original file
    wavfile.write(new_file, int(samplerate * speed), data)


if __name__ == '__main__':
    file = read_wav()

    # Extracts and prints the song name from the file path name
    index = file.rfind("\\")
    song_name = file[(index + 1):]
    index = song_name.rfind(".")
    song_name = song_name[:index]
    print("Uploaded Song: " + song_name)

    # Receives the user's desired speed input and checks its values
    speed = input("\nInput Desired Speed (Number Between .1 and 10): ")
    speed = float(speed)
    while speed < .1 or speed > 5.0:
        print("Speed Value Must Be Between .1 and 5\n")
        speed = input("Input Desired Speed (Number Between .1 to 10): ")
        speed = float(speed)

    # Produces the output audio file's name
    new_file = file.replace(song_name, song_name + " (Speed_Changed)")

    speed_change(file)
    print("\nSong saved in same directory as: " + song_name + " (Speed_Changed)")
