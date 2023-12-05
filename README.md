//보고서

//요구사항
import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from denoise import AudioDeNoise
import speech_recognition as sr
from gtts import gTTS
import numpy as np
import pywt
import soundfile
from tqdm import tqdm
from lib.noiseProfiler import NoiseProfiler


// 우분투 20.04 기준 설치방법
pip install tqdm
pip install gTTS
pip install numpy
pip install matplotlib
pip install SpeechRecognition
pip install PyWavelets
pip install scipy


// [오픈소스 URL]
#DeNoise
https://github.com/AP-Atul/Audio-Denoising

#Speech_Recognition
[참조 문헌]
https://prlabhotelshoe.tistory.com/8

// 발표 슬라이드 내용과 구체적인 설명
