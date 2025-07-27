with open('test.txt', 'w', encoding='utf-8') as file:
    file.write('안녕하세요\n')
    file.write('파이썬 파일 처리를 연습하고 있습니다\n')
    file.write('오늘은 좋은 날씨입니다\n')

with open('test.txt', 'r', encoding='utf-8') as file:
    for line in file.readlines():
        print(line, end='')