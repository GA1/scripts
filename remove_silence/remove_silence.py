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


def remove_silence_from_sound(sound):
    chunk_size = 5
    chunk_buffer = 6
    result = AudioSegment.empty()
    chunks_raw = sound[::chunk_size]
    chunks = []
    for chunk_raw in chunks_raw:
        chunks.append(chunk_raw)
    print(len(chunks))
    for i in range(0, chunk_buffer):
        result = result + chunks[i]
    for i in range(chunk_buffer, len(chunks) - chunk_buffer):
        if not from_to_are_silent(chunks, i - chunk_buffer, i + chunk_buffer):
            result = result + chunks[i]
    for i in range(len(chunks) - chunk_buffer, len(chunks)):
        result = result + chunks[i]
    return result


remove_leading_silence_from_file_and_save('./input_files/', 'H41001', '.mp3', './results/', 'result', '.mp3')
