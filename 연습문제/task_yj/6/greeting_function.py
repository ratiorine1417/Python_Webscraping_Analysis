def greeting_f(name, greeting='안녕하세요', greeting2=None):
    if greeting2 != None:
        print(f"{greeting}, {name}! {greeting2}")
    else:
        print(f"{greeting}, {name}!")

greeting_f('김철수님')
greeting_f('John', 'Hello')
greeting_f('이영희님', greeting2='좋은 하루 되세요!')