import random

made = 0
name = input('Привет, как тебя зовут?')
print(name.title(), ', я загадал число от 1 до 100, попробуй угадать его за 8 попыток')
number = random.randint(1,100)
while made <8:
    print('Попыток осталось:', (8-made) )
    guess = int(input('Твое число: '))
    made += 1
    if guess>number:
        print(name.title(), ', твое число больше')
    elif guess<number:    
        print(name.title(), ', твое число меньше')
    else:
        break
if guess == number:
    print(name.title(), ', ты угадал!')
else:
    print(name.title(), ', ты не угадал, попытки закочились. \nЯ загадал число: ', number)
