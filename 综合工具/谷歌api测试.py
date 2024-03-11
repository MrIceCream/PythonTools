from google.cloud import speech

def transcribe_speech(audio_file):
    # 创建一个 Client 实例
    client = speech.SpeechClient()

    # 读取音频文件的数据
    with open(audio_file, "rb") as audio_data:
        audio = speech.RecognitionAudio(content=audio_data.read())

    # 配置语音识别请求
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        language_code="zh-CN",
        audio_channel_count=2
    )

    # 发送语音识别请求
    response = client.recognize(config=config, audio=audio)

    # 解析并打印识别结果
    for result in response.results:
        print("Transcript: {}".format(result.alternatives[0].transcript))

# 测试用法
audio_file = "test.wav"  # 音频文件的路径

transcribe_speech(audio_file)