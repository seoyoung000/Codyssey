import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# password.txt 파일 읽기
with open(os.path.join(BASE_DIR, "password.txt"), "r", encoding="utf-8") as file:
    encrypted_text = file.read().strip()


# 카이사르 암호 해독 함수
def caesar_cipher_decode(target_text):

    # 알파벳 개수만큼 반복
    for shift in range(26):

        decoded_text = ""

        # 문자열 한 글자씩 검사
        for char in target_text:

            # 대문자 처리
            if char.isupper():
                decoded_char = chr(
                    (ord(char) - ord('A') - shift) % 26 + ord('A')
                )
                decoded_text += decoded_char

            # 소문자 처리
            elif char.islower():
                decoded_char = chr(
                    (ord(char) - ord('a') - shift) % 26 + ord('a')
                )
                decoded_text += decoded_char

            # 알파벳이 아니면 그대로
            else:
                decoded_text += char

        # 자리수별 결과 출력
        print(f"[{shift}칸 이동 결과]")
        print(decoded_text)
        print("-" * 30)


# 함수 실행
caesar_cipher_decode(encrypted_text)


# 정답 자리수 입력
answer_shift = int(input("정답 자리수를 입력하세요: "))

result_text = ""

for char in encrypted_text:

    if char.isupper():
        decoded_char = chr(
            (ord(char) - ord('A') - answer_shift) % 26 + ord('A')
        )
        result_text += decoded_char

    elif char.islower():
        decoded_char = chr(
            (ord(char) - ord('a') - answer_shift) % 26 + ord('a')
        )
        result_text += decoded_char

    else:
        result_text += char


# result.txt 저장
with open(os.path.join(BASE_DIR, "result.txt"), "w", encoding="utf-8") as file:
    file.write(result_text)

print("해독 결과가 result.txt로 저장되었습니다.")