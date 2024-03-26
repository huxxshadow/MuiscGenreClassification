from dataclasses import dataclass
from pathlib import Path
import numpy as np
import pandas as pd
import thinkdsp
from typing import Dict, List, Tuple, Union
from matplotlib import pyplot as plt



TRAINPATH="SimpleData/train"
@dataclass
class Features:
    sample_rate: int = 22050
    hop_length: int = 220
    n_fft: int = 2048
    n_frames_per_example: int = 1


def extract_features(file_path: Union[str, Path], params: Features) -> List[np.ndarray]:
    wave=thinkdsp.read_wave(str(file_path))

    # spectrogram = librosa.feature.melspectrogram(
    #     y=waveform, n_fft=params.n_fft, hop_length=params.hop_length
    # )
    spectrogram= wave.make_spectrogram(4096)

    spectrogram = np.log(1e-20 + np.abs(spectrogram**2))

    n_examples = spectrogram.shape[1] // params.n_frames_per_example

    return [
        spectrogram[
            :, i * params.n_frames_per_example : (i + 1) * params.n_frames_per_example
        ].reshape(1, -1)
        for i in range(n_examples)
    ]


PATH = TRAINPATH + "/classical/1429195257218202828.wav"
PARAMS = Features(n_frames_per_example=15)

# ipd.display(ipd.Audio(PATH))

sample_features = [
    feature.reshape(-1, PARAMS.n_frames_per_example)
    for feature in extract_features(file_path=PATH, params=PARAMS)
]

plt.figure(figsize=(20, 5))
plt.title("Spectrogram")
plt.imshow(np.hstack(sample_features), cmap="plasma")
plt.axis("off")
plt.savefig("spectrogram.png", dpi=200)
plt.show()

plt.figure(figsize=(20, 5))
for i, feature in enumerate(sample_features):
    plt.subplot(1, len(sample_features) + 1, i + 1)
    plt.imshow(feature, cmap="plasma")
    plt.axis("off")
plt.show()