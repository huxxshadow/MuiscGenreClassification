import os
from pydub import AudioSegment

import os
from pydub import AudioSegment

def trans_all_file(files_path, target="wav"):
    output_dir = os.path.join(files_path, "../out")
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for filepath in os.listdir(files_path):
        full_path = os.path.join(files_path, filepath)
        base_name, ext = os.path.splitext(filepath)
        if ext:
            song = AudioSegment.from_file(full_path, format=ext.replace(".", ""))
            # 修改target_path来包含output_dir
            target_path = os.path.join(output_dir, f"{base_name}.{target}")
            song.export(target_path, format=target)

trans_all_file("/MuiscGenreClassification/input")

def make_chunks(audio_segment, chunk_length_ms):
    chunks = []
    for start in range(0, len(audio_segment), chunk_length_ms):
        end = start + chunk_length_ms
        chunk = audio_segment[start:end]
        chunks.append(chunk)
    return chunks


input_dir = "/MuiscGenreClassification/out"
output_dir = "/MuiscGenreClassification/SimpleData/test"


size = 6000
for each in os.listdir(input_dir):
    if each.endswith(".wav"):
        wave_path = os.path.join(input_dir, each)
        wave = AudioSegment.from_file(wave_path, "wav")
        chunks = make_chunks(wave, size)
        for i, chunk in enumerate(chunks):
            chunk_name = f"{each.split('.')[0]}-{i}.wav"
            chunk.export(os.path.join(output_dir, chunk_name), format="wav")
