email_adr = input('이메일 주소를 입력하세요: ')

user_name, domain = email_adr.split('@')
print(f'사용자명: {user_name}')
print(f'도메인: {domain}')