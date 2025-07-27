str1 = input('문장을 입력하세요: ')
look_for = input('찾을 문자를 입력하세요: ')

print(f"문자 '{look_for}'이 {str1.lower().count(look_for.lower())}번 나타납니다.")
