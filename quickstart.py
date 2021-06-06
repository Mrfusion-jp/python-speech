import io
import os
from google.cloud import speech

# クライアントの生成
client = speech.SpeechClient()

# 音声ファイル名の生成
file_name = os.path.join(os.path.dirname(__file__), "resources", "audio.raw")

# 音声ファイルの読み込み
with io.open(file_name, "rb") as audio_file:
    content = audio_file.read()
    audio = speech.RecognitionAudio(content=content)

# 音声ファイルをテキストに変換
config = speech.RecognitionConfig(
    encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
    sample_rate_hertz=16000,
    language_code="en-US",
)
response = client.recognize(config=config, audio=audio)

# 出力
for result in response.results:
    print("Transcript: {}".format(result.alternatives[0].transcript))
