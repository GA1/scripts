from pydub import AudioSegment


def remove_leading_silence_from_file_and_save(input_directory_path, input_file_name, input_file_extension, result_directory_path, result_file_name, result_file_extension):
    sound = AudioSegment.from_mp3(input_directory_path + input_file_name + input_file_extension)
    result = remove_silence_from_sound(sound)
    result.export(result_directory_path + result_file_name + result_file_extension, format='mp3')


def remove_silence_from_sound(sound):
    chunk_size = 1000
    result = AudioSegment.empty()
    print(len(sound))
    for i in range(0, len(sound), chunk_size):
        chunk = sound[i * chunk_size: (i + 1) * chunk_size]
        # print(chunk.dBFS)
        # if -30.0 < chunk.dBFS:
        print(len(result))
        print(len(chunk))
        print(len(result + chunk))
        result = result + chunk
        print(len(result))
        # print(chunk.dBFS)
    return result


remove_leading_silence_from_file_and_save('./input_files/', '90-120s', '.mp3', './results/', 'result', '.mp3')
