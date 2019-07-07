from pydub import AudioSegment


def trim(input_file_path, output_file_path, minute_start, second_start, minute_stop, second_stop):
    sound = AudioSegment.from_file(input_file_path, format="mp3")
    trimmed_sound = sound[(minute_start * 60 + second_start) * 1000: (minute_stop * 60 + second_stop) * 1000]
    trimmed_sound.export(output_file_path, format="mp3")


def trim_last_n_seconds(input_file_path, output_file_path, N):
    sound = AudioSegment.from_file(input_file_path, format="mp3")
    trimmed_sound = sound[:-N * 1000]
    trimmed_sound.export(output_file_path, format="mp3")


def trim_first_n_seconds(input_file_path, output_file_path, N):
    sound = AudioSegment.from_file(input_file_path, format="mp3")
    trimmed_sound = sound[N * 1000:]
    trimmed_sound.export(output_file_path, format="mp3")


data = [
    [2, 12, 100, 27, "hsk4_1"],
    [2, 9, 100, 27, "hsk4_2"],
    [2, 15, 100, 27, "hsk4_3"],
]

for d in data:
    print(d[4] + '.mp3')
    trim_first_n_seconds('input_files/' + d[4] + '.mp3', 'results/' + d[4] + '.mp3', d[0] * 60 + d[1])

