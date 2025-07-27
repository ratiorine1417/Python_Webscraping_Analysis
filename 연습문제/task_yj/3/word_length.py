word = ['cat', 'elephant', 'dog', 'butterfly', 'ant']
word_length = []

for i in word:
    word_length.append(len(i))

max_index = word_length.index(max(word_length))
min_index = word_length.index(min(word_length))

print(f'단어 목록: {word}')
print(f'가장 긴 단어: {word[max_index]} ({max(word_length)}글자)')
print(f'가장 짧은 단어: {word[min_index]} ({min(word_length)}글자)')