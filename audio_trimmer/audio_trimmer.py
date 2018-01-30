from pydub import AudioSegment


def trim(minuteStart, secondStart, input_file_path, output_file_path, minuteStop, secondStop):
    sound = AudioSegment.from_file(input_file_path, format="mp3")
    trimmed_sound = sound[(minuteStart * 60 + secondStart) * 1000: (minuteStop * 60 + secondStop) * 1000]
    trimmed_sound.export(output_file_path, format="mp3")


data = [
    [5, 20, 7, 27, "01"],
    # [5, 20, 7, 27, "02"],
    # [5, 20, 7, 27, "03"],
    # [5, 20, 7, 27, "04"],
    # [5, 20, 7, 27, "05"],
    # [5, 20, 7, 27, "06"],
    # [5, 20, 7, 27, "07"],
    # [5, 20, 7, 27, "08"],
    # [5, 20, 7, 27, "09"],
    # [5, 20, 7, 27, "10"],
    # [5, 20, 7, 27, "11"],
    # [5, 20, 7, 27, "12"],
    # [5, 20, 7, 27, "13"],
    # [5, 20, 7, 27, "14"],
    # [5, 20, 7, 27, "15"],
    # [5, 20, 7, 27, "16"],
    # [5, 20, 7, 27, "17"],
]

for d in data:
    trim(d[0], d[1], d[2], 'input_files/' + [3] + '.mp3', 'results/' + [3] + '.mp3', d[4])