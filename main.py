import os

def analyze_log():
    file_name = 'mission_computer_main.log'
    
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            
        for line in lines:
            print(line.strip())
            
    except FileNotFoundError:
        print(f"오류: '{file_name}' 파일을 찾을 수 없습니다. 경로를 확인하세요.")

if __name__ == '__main__':
    analyze_log()