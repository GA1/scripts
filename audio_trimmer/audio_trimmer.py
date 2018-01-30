from pydub import AudioSegment


def trim(minute_start, second_start, minute_stop, second_stop, input_file_path, output_file_path):
    sound = AudioSegment.from_file(input_file_path, format="mp3")
    trimmed_sound = sound[(minute_start * 60 + second_start) * 1000: (minute_stop * 60 + second_stop) * 1000]
    trimmed_sound.export(output_file_path, format="mp3")


data = [
    [5, 20, 7, 27, "01"],
    [5, 13, 7, 30, "02"],
    [4, 20, 5, 55, "03"],
    [4, 29, 6, 25, "04"],
    [3, 43, 5, 41, "05"],
    [5, 1, 6, 55, "06"],
    [3, 43, 6, 26, "07"],
    [2, 50, 4, 4, "08"],
    [3, 28, 4, 53, "09"],
    [3, 35, 4, 51, "10"],
    [3, 49 , 5, 13, "11"],
    [3, 51, 5, 32, "12"],
    [2, 59, 4, 14, "13"],
    [3, 41, 5, 4, "14"],
    [5, 18, 7, 15, "15"],
    [5, 42, 7, 27, "16"],
    [7, 26, 9, 52, "16"],
]

for d in data:
    print(data[4])
    trim(d[0],
         d[1],
         d[2],
         d[3],
         'input_files/' + d[4] + '.mp3',
         'results/' + d[4] + '.mp3'
         )
