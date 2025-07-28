with open('test.txt', 'w', encoding='utf-8') as file:
    file.write('쉬운 파이썬 프로그래밍 언어 배우기\n')
    file.write('파이썬 프로그래밍 언어\n')
    file.write('강력한 파이썬\n')

def count_word():
    with open('test.txt', 'r', encoding='utf-8') as file:
        text = file.read()

    words = text.split()
    frequency = {}

    for word in words:
        frequency[word] = frequency.get(word, 0) + 1
    print('단어 빈도 분석 결과:')
    for word, freq in frequency.items():
        print(f"{word}: {freq}번")

count_word()
# 다른 방법: pandas value_counts 사용