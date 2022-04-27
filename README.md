# Audio Speed Changer

This Python program adjusts the speed/pitch of audio files using easygui to open a file-manager, soundfile to retreieve the audio file's
data and sample-rate, and wavfile to manipulate the audo file.

Steps:
- Run the program and choose a .wav audio file
- Enter a valid number to slow or speed up the audio file by (Between .1 and 10)

Note:
- Once the program has completed running, the newly-created audio file will be in the same location as the audio file you had originally chosen
- The newly-created audio file will retain the name of the original audio file with the exception of adding "(Speed Changed)" to the title




** There may be encoding issues if the audio file chosen is too big or in an invalid format (not .wav)
