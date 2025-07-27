score = float(input('점수를 입력하세요: '))

if (score  < 60)&(score >= 0):
    grade = 'F'
elif (score < 70)&(score >= 60):
    grade = 'D'
elif (score  < 80)&(score >= 70):
    grade = 'C'
elif (score  < 90)&(score >= 80):
    grade = 'B'
elif (score  <= 100)&(score >= 90):
    grade = 'A'
else:
    print('점수를 잘못 입력했습니다. 다시 입력해 주세요.')
    exit()
print(f'점수 {score}점의 학점은 {grade}입니다.')