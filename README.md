##보고서  
##요구사항  
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

변환하고자 하는 .wav 파일을 inputAudiofile.wav 형태로 프로젝트 폴더 내에 저장합니다.  
project.py 를 실행하면 음성파일을 텍스트 대본으로 출력하고, gtts 음성으로 변환된 파일이 폴더 내에 read_my_file.mp3 로 저장됩니다.
Visualize.py 를 실행하면 원본 음성파일과 denoise 된 파일의 spectogram을 plot 하여 출력합니다.


##우분투 20.04 기준 설치방법  
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

// [참조 문헌]  
https://prlabhotelshoe.tistory.com/8  

// 발표 슬라이드 내용과 구체적인 설명
-block diagram : 입력으로 받은 wav 파일을 denoising 과정을 거쳐 text 파일로 변환하고, 이것을 다시 gtts를 이용하여 목소리를 교체 후 .wav 로 저장합니다.-
gtts : google 의 text-to-speech 를 사용하여 텍스트를 음성으로 변환하는 파이썬 라이브러리.
denoise process는 오픈소스를 활용하였습니다.
노이즈 제거 전후의 차이를 눈으로 파악하기 위해 matplotlib를 활용하여 원본 wav와 denoise된 wav를 그래프로 표시합니다
recognition_speech로 wav 파일을 읽어 그 대본을 txt 형식으로 작업 폴더 안에 저장합니다.
저장된 txt를 다시 gtts로 읽습니다.
