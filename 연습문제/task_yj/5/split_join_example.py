str_base = 'Python is awesome programming language'
split_str = str_base.split(' ')
join_hyphen = '-'.join(split_str)
join_upper = ' '.join(split_str).upper()

print(f'원본 문자열: {str_base}')
print(f'분리된 단어들: {split_str}')
print(f'하이픈으로 연결: {join_hyphen}')
print(f'대문자로 변환 후 공백으로 연결: {join_upper}')
