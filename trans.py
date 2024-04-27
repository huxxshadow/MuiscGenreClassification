import os
from pydub import AudioSegment
def trans_all_file(files_path, target="wav"):
    output_dir = os.path.join(files_path, "../input/wavInput")
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for filepath in os.listdir(files_path):
        full_path = os.path.join(files_path, filepath)
        base_name, ext = os.path.splitext(filepath)
        if ext:
            song = AudioSegment.from_file(full_path, format=ext.replace(".", ""))
            target_path = os.path.join(output_dir, f"{base_name}.{target}")
            song.export(target_path, format=target)

# trans_all_file("input")

def make_chunks(audio_segment, chunk_length_ms):
    chunks = []
    for start in range(0, len(audio_segment), chunk_length_ms):
        end = start + chunk_length_ms
        chunk = audio_segment[start:end]
        chunks.append(chunk)
    return chunks


input_dir = "input/wavInput"
output_dir = "SimpleData/test"


def start():
    size = 6000
    trans_all_file("input")
    for each in os.listdir(input_dir):
        if each.endswith(".wav"):
            wave_path = os.path.join(input_dir, each)
            wave = AudioSegment.from_file(wave_path, "wav")
            chunks = make_chunks(wave, size)
            for i, chunk in enumerate(chunks):
                t=each.split('.')
                chunk_name = f"{str().join(t[0:len(t)-1])}-{i}.wav"
                chunk.export(os.path.join(output_dir, chunk_name), format="wav")

def removeAll(filepath):
    del_list = os.listdir(filepath)
    for f in del_list:
        file_path = os.path.join(filepath, f)
        if os.path.isfile(file_path):
            os.remove(file_path)

def endall():
    removeAll("SimpleData/test")
    removeAll("input/wavInput")
    print("End")

endall()