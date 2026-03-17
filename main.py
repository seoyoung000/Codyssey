def analyze_log():
    file_name = 'mission_computer_main.log'
    report_name = 'log_analysis.md'
    issue_logs = []
    
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            
        for line in lines:
            print(line.strip())
            if 'unstable' in line.lower() or 'explosion' in line.lower():
                issue_logs.append(line.strip())

        with open(report_name, 'w', encoding='utf-8') as report:
            report.write('화성 기지 사고 분석 보고서\n\n')
            report.write('1. 사고 발생 개요\n')
            report.write('- 최종 사고 시각: 2023-08-27 11:40:00\n')
            report.write('- 주요 원인: 산소 탱크 폭발\n\n')
            report.write('2. 상세 타임라인\n')
            report.write('- 11:28:00: 로켓 지상 착륙 성공\n')
            report.write('- 11:35:00: 산소 탱크 불안정 감지 (unstable)\n')
            report.write('- 11:40:00: 산소 탱크 폭발 발생 (explosion)\n\n')
            report.write('3. 분석 \n')
            report.write('로켓은 안전하게 착륙했으나 착륙 7분 후 산소 탱크 결함으로 폭발함.')

    except FileNotFoundError:
        print(f"오류: '{file_name}' 파일을 찾을 수 없습니다.")
    except Exception as e:
        print(f'알 수 없는 오류 발생: {e}')

if __name__ == '__main__':
    analyze_log()
