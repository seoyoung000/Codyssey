'''시스템 마이크를 통해 음성을 녹음하고 records 폴더에 저장하는 모듈.'''

import os
import wave
import datetime

import pyaudio


CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
RECORD_SECONDS = 5
RECORDS_DIR = 'records'


def ensure_records_dir(directory):
    '''녹음 파일을 저장할 폴더가 없으면 생성한다.'''
    if not os.path.exists(directory):
        os.makedirs(directory)


def make_file_name():
    '''현재 날짜와 시간을 이용해 파일 이름을 생성한다.'''
    now = datetime.datetime.now()
    return now.strftime('%Y%m%d-%H%M%S') + '.wav'


def record_audio(duration=RECORD_SECONDS):
    '''마이크로부터 지정한 시간 동안 음성을 녹음하여 파일로 저장한다.'''
    ensure_records_dir(RECORDS_DIR)

    audio = pyaudio.PyAudio()
    stream = audio.open(
        format=FORMAT,
        channels=CHANNELS,
        rate=RATE,
        input=True,
        frames_per_buffer=CHUNK,
    )

    print('녹음을 시작합니다.')
    frames = []
    total_chunks = int(RATE / CHUNK * duration)
    for _ in range(total_chunks):
        data = stream.read(CHUNK)
        frames.append(data)
    print('녹음을 종료합니다.')

    sample_width = audio.get_sample_size(FORMAT)
    stream.stop_stream()
    stream.close()
    audio.terminate()

    file_path = os.path.join(RECORDS_DIR, make_file_name())
    with wave.open(file_path, 'wb') as wave_file:
        wave_file.setnchannels(CHANNELS)
        wave_file.setsampwidth(sample_width)
        wave_file.setframerate(RATE)
        wave_file.writeframes(b''.join(frames))

    print('저장된 파일: ' + file_path)
    return file_path


def main():
    '''스크립트가 직접 실행될 때 녹음을 수행한다.'''
    record_audio()


if __name__ == '__main__':
    main()
