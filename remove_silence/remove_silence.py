from pydub import AudioSegment


def remove_leading_silence_from_file_and_save(input_directory_path, input_file_name, input_file_extension, result_directory_path, result_file_name, result_file_extension):
    sound = AudioSegment.from_mp3(input_directory_path + input_file_name + input_file_extension)
    result = remove_silence_from_sound(sound)
    result.export(result_directory_path + result_file_name + result_file_extension, format='mp3')


def from_to_are_silent(chunks, from_index, to_index):
    for i in range(from_index, to_index):
        if -30 < chunks[i].dBFS:
            return False
    return True


CHUNK_SIZE = 500 # in ms
CHUNK_BUFFER = 6


def remove_silence_from_sound(sound):
    result = AudioSegment.empty()
    chunks_raw = sound[::CHUNK_SIZE]
    chunks = []
    for chunk_raw in chunks_raw:
        chunks.append(chunk_raw)
    for i in range(0, CHUNK_BUFFER):
        result = result + chunks[i]
    for i in range(CHUNK_BUFFER, len(chunks) - CHUNK_BUFFER):
        if not from_to_are_silent(chunks, i - CHUNK_BUFFER, i + CHUNK_BUFFER):
            result = result + chunks[i]
    for i in range(len(chunks) - CHUNK_BUFFER, len(chunks)):
        result = result + chunks[i]
    return result

data = [
    # 'hsk4_1',
    # 'hsk4_2',
    # 'hsk4_3',
    'hsk4_4',
    'hsk4_5',
]

for d in data:
    print(d + '.mp3')
    remove_leading_silence_from_file_and_save('./input_files/', d, '.mp3', './results/', d, '.mp3')