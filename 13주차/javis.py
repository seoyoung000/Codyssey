import os
import wave
import csv
from datetime import datetime
import pyaudio
import speech_recognition as sr

class MarsVoiceRecorder:
    def __init__(self, record_seconds=10):
        self.chunk = 1024
        self.format = pyaudio.paInt16
        self.channels = 1
        self.rate = 44100
        self.record_seconds = record_seconds
        self.output_dir = 'records'

    def create_directory(self):
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

    def generate_file_name(self):
        current_time = datetime.now()
        time_string = current_time.strftime('%Y%m%d-%H%M%S')
        file_name = f'{time_string}.wav'
        return os.path.join(self.output_dir, file_name)

    def record_audio(self):
        self.create_directory()
        file_path = self.generate_file_name()

        audio = pyaudio.PyAudio()
        stream = audio.open(
            format=self.format,
            channels=self.channels,
            rate=self.rate,
            input=True,
            frames_per_buffer=self.chunk
        )

        print('음성 기록을 시작합니다...')
        frames = []

        loop_count = int(self.rate / self.chunk * self.record_seconds)
        for _ in range(0, loop_count):
            data = stream.read(self.chunk)
            frames.append(data)

        print('음성 기록이 완료되었습니다.')

        stream.stop_stream()
        stream.close()
        audio.terminate()

        with wave.open(file_path, 'wb') as wave_file:
            wave_file.setnchannels(self.channels)
            wave_file.setsampwidth(audio.get_sample_size(self.format))
            wave_file.setframerate(self.rate)
            wave_file.writeframes(b''.join(frames))

        print(f'기록이 정상적으로 저장되었습니다: {file_path}')
        return file_path

class SpeechToTextConverter:
    def __init__(self):
        self.input_dir = 'records'
        self.recognizer = sr.Recognizer()

    def get_audio_files(self):
        file_list = []
        if os.path.exists(self.input_dir):
            for file_name in os.listdir(self.input_dir):
                if file_name.endswith('.wav'):
                    file_list.append(os.path.join(self.input_dir, file_name))
        return file_list

    def convert_and_save(self):
        audio_files = self.get_audio_files()
        if not audio_files:
            print('변환할 음성 파일이 없습니다.')
            return

        for audio_file in audio_files:
            base_name = os.path.splitext(audio_file)[0]
            csv_file = f'{base_name}.csv'

            # 이미 변환된 CSV 파일이 존재하면 건너뜀
            if os.path.exists(csv_file):
                continue

            print(f'{audio_file} 파일의 텍스트 변환을 시작합니다...')
            text_result = self.extract_text(audio_file)

            # 파일 전체를 한 번에 인식하므로 시작 시간을 '00:00'으로 기록
            self.save_to_csv(csv_file, '00:00', text_result)

    def extract_text(self, file_path):
        try:
            with sr.AudioFile(file_path) as source:
                audio_data = self.recognizer.record(source)
                # Google Web Speech API를 활용하여 한국어로 텍스트 추출
                text = self.recognizer.recognize_google(audio_data, language='ko-KR')
                return text
        except sr.UnknownValueError:
            return '음성을 인식할 수 없습니다.'
        except sr.RequestError:
            return '음성 인식 서비스에 접근할 수 없습니다.'
        except Exception as error_msg:
            return f'오류 발생: {error_msg}'

    def save_to_csv(self, file_path, time_stamp, text):
        # 한글 깨짐 방지를 위해 'utf-8-sig' 인코딩 사용
        with open(file_path, 'w', encoding='utf-8-sig', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(['시간', '인식된 텍스트'])
            writer.writerow([time_stamp, text])
        print(f'텍스트가 정상적으로 CSV로 저장되었습니다: {file_path}')

if __name__ == '__main__':
    # 1. 음성 녹음 실행
    recorder = MarsVoiceRecorder(record_seconds=10)
    recorder.record_audio()

    # 2. records 폴더 내의 음성 파일을 읽어 STT 변환 및 CSV 저장
    converter = SpeechToTextConverter()
    converter.convert_and_save()