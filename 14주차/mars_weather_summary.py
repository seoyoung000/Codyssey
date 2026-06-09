# CREATE TABLE mars_weather (
#     weather_id INT AUTO_INCREMENT PRIMARY KEY,
#     mars_date DATETIME NOT NULL,
#     temp INT,
#     storm INT
# );

import csv
import mysql.connector

def main():
    # 1. MySQL DB 연결 설정
    # 본인의 로컬 환경에 맞게 비밀번호와 데이터베이스 이름을 수정해 주세요.
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="YOUR_PASSWORD",  # MySQL 비밀번호
            database="YOUR_DATABASE"   # 생성한 테이블이 있는 데이터베이스 이름
        )
        cursor = connection.cursor()
        print("✅ MySQL 데이터베이스 연결 성공")

    except mysql.connector.Error as err:
        print(f"❌ DB 연결 에러: {err}")
        return

    # 2. CSV 파일 읽기 및 데이터 확인
    # 업로드해주신 파일명에 맞게 확장자를 대문자(CSV)로 맞추거나 실제 파일명과 동일하게 지정합니다.
    file_path = 'mars_weathers_data.CSV' 
    
    try:
        with open(file_path, mode='r', encoding='utf-8') as file:
            csv_data = csv.reader(file)
            header = next(csv_data)  # 첫 줄(헤더) 건너뛰기
            print(f"📊 CSV 컬럼 정보: {header}")
            
            # 3. INSERT 쿼리 준비
            # weather_id는 AUTO_INCREMENT이므로 생략하고 나머지 3개만 입력합니다.
            insert_query = """
            INSERT INTO mars_weather (mars_date, temp, storm)
            VALUES (%s, %s, %s)
            """
            
            # 4. 반복 실행을 통한 데이터 삽입
            count = 0
            for row in csv_data:
                # row[0]: weather_id (DB 자동 증가이므로 사용 안 함)
                # row[1]: mars_date
                # row[2]: temp (소수점 문자열이므로 float 변환 후 int로 캐스팅)
                # row[3]: stom (storm)
                
                mars_date = row[1]
                temp = int(float(row[2]))
                storm = int(row[3])
                
                cursor.execute(insert_query, (mars_date, temp, storm))
                count += 1
                
                # 처음 3줄만 샘플로 콘솔에 출력하여 데이터 확인
                if count <= 3:
                    print(f"데이터 삽입 확인 중... -> 날짜: {mars_date}, 온도: {temp}, 폭풍: {storm}")

            # 5. DB에 최종 반영 (Commit)
            connection.commit()
            print(f"\n🚀 총 {count}건의 화성 날씨 데이터가 성공적으로 백업되었습니다!")

    except FileNotFoundError:
        print(f"❌ 에러: '{file_path}' 파일을 찾을 수 없습니다. 파이썬 스크립트와 같은 경로에 있는지 확인해 주세요.")
    except Exception as e:
        print(f"❌ 데이터 처리 중 에러 발생: {e}")
        connection.rollback()
    
    finally:
        # 6. 안전한 연결 종료
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
            print("🔒 MySQL 연결이 종료되었습니다.")

if __name__ == "__main__":
    main()