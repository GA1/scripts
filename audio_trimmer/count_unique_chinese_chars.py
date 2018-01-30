from pydub import AudioSegment


def remove_silence(minuteStart, secondStart, input_file_path, output_file_path, minuteStop, secondStop):
    sound = AudioSegment.from_file(input_file_path, format="mp3")
    trimmed_sound = sound[(minuteStart * 60 + secondStart) * 1000: (minuteStop * 60 + secondStop) * 1000]
    trimmed_sound.export(output_file_path, format="mp3")


remove_silence(5, 20, 'input_files/01 copy.mp3', "results/012 copy.mp3", 7, 27)