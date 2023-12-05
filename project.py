import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
import numpy as np
from denoise import AudioDeNoise
import speech_recognition as sr
from gtts import gTTS

audioDenoiser = AudioDeNoise(inputFile="inputAudiofile.wav")

audioDenoiser.deNoise(outputFile="input_denoised.wav")


audio_file = "input_denoised.wav"  
recognizer = sr.Recognizer()  # 인식기 객체를 올바르게 생성합니다.

harvard_audio = sr.AudioFile(audio_file)
with harvard_audio as source:
    audio = recognizer.record(source)

try:
    text = recognizer.recognize_google(audio, language='ko-KR')  # 'recognizer' 변수명을 사용하여 메서드 호출을 수정합니다.
    print(text)
except sr.UnknownValueError:
    print("Google 웹 API가 오디오를 이해하지 못했습니다.")
except sr.RequestError as e:
    print(f"Google 웹 API에서 결과를 요청할 수 없었습니다; {e}")
except Exception as e:
    print(f"오류가 발생했습니다: {e}")


# Specify the file path where you want to save the text
file_path = "output.txt"

# Open the file in write mode ('w')
with open(file_path, 'w', encoding='utf-8') as file:
    # Write the text to the file
    file.write(text)

print(f'Text has been written to {file_path}')

s = None

with open("output.txt", "r", encoding="utf-8") as f:
    s = f.read()

file = "read_my_file.mp3"
tts = gTTS(s, lang='ko')  # 'ko'는 한국어로 설정됩니다.
tts.save(file)


