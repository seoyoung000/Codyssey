def manage_mars_inventory():
    source_file = 'Mars_Base_Inventory_List.csv'
    danger_csv = 'Mars_Base_Inventory_danger.csv'
    
    inventory_list = []

    # 1. 파일 읽기 및 내용 출력
    try:
        print('--- Mars_Base_Inventory_List.csv 내용 출력 ---')
        with open(source_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            # 전체 내용을 화면에 먼저 출력
            for line in lines:
                print(line.strip())
            
            # 2. 리스트 객체로 변환 (데이터 파싱)
            for line in lines[1:]:  # 첫 줄(헤더)은 제외하고 반복
                row = line.strip().split(',')
                if len(row) >= 5:
                    name = row[0]       # 물질 이름
                    index = float(row[4]) # 인화성 지수
                    inventory_list.append([name, index])
    except FileNotFoundError:
        print(f"오류: '{source_file}' 파일이 없습니다.")
        return
    except Exception as e:
        print(f'파일을 읽는 중 오류가 발생했습니다: {e}')
        return

    # 3. 인화성 지수 기준 내림차순 정렬
    # 정렬 기준(key)을 두 번째 요소(x[1])인 숫자로 설정
    inventory_list.sort(key=lambda x: x[1], reverse=True)

    print('\n---정렬된 리스트 ---')
    for item in inventory_list:
        print(item)

    # 4. 인화성 지수 0.7 이상만 따로 모으기
    danger_list = []
    for item in inventory_list:
        if item[1] >= 0.7:
            danger_list.append(item)

    print('\n---위험 물질(0.7 이상) 목록 ---')
    for item in danger_list:
        print(f"'{item[0]}': {item[1]}")

    # 5. 위험 물질 목록을 CSV 파일로 저장
    try:
        with open(danger_csv, 'w', encoding='utf-8') as f:
            f.write('Substance,Flammability\n')
            for item in danger_list:
                f.write(f"'{item[0]}',{item[1]}\n")
        print(f"\n---'{danger_csv}' 저장 완료 ---")
    except Exception as e:
        print(f'저장 중 오류가 발생했습니다: {e}')

if __name__ == '__main__':
    manage_mars_inventory()