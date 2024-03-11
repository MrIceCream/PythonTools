from pydub import AudioSegment
from pydub.silence import detect_silence
import os

def delete_files_in_directory(directory):
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            os.remove(file_path)
            print(f"Deleted file: {file_path}")


def split_by_silence(input_file, output_dir, min_silence_len, silence_thresh):
    # 加载 MP3 文件
    audio = AudioSegment.from_mp3(input_file)

    # 使用 detect_silence 函数检测停顿
    silent_ranges = detect_silence(audio, min_silence_len=min_silence_len, silence_thresh=silence_thresh)

    # 切割并保存切割后的音频文件
    preview_start = 0
    os.makedirs(output_dir, exist_ok=True)
    for i, (start, end) in enumerate(silent_ranges):
        real_end = start+(end-start)/2
        print('分割区间:{0}-{1}'.format(preview_start, real_end))
        segment = audio[preview_start:real_end]
        output_file = f"{output_dir}/{i + 1}.mp3"
        segment.export(output_file, format="mp3")
        preview_start = real_end


def get_mp3_files(directory):
    mp3_files = []
    for filename in os.listdir(directory):
        if filename.endswith(".mp3"):
            file_path = os.path.join(directory, filename)
            mp3_files.append(file_path)
    return mp3_files


def main():
    directory = "input"  # 目录路径
    mp3_files = get_mp3_files(directory)

    min_silence_len = 2000               # 停顿的最小持续时间（单位：毫秒）
    silence_thresh = -30                 # 停顿的音量阈值（单位：dBFS）

    for mp3_file in mp3_files:
        print('{0} 分割中...'.format(mp3_file))
        output_dir = "output/{0}".format(os.path.basename(mp3_file))             # 输出切割后 MP3 文件的前缀
        split_by_silence(mp3_file, output_dir, min_silence_len, silence_thresh)

main()