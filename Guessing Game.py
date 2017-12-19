import random
max_number = int(input('I will choose a number between one and whatever maximum you set. Please choose the maximum number now: ' ))
c = 10
while c == 10:
    n = random.randint(1, max_number)
    z = 10
    while z == 10:
        ans = int(input('Enter your guess - or enter "0" to quit: '))
        if ans == 0:
            print('Thank you for playing!')
            c = 11
            break
    
        else:
            if ans == n:
                print('Success you win! I will now choose another number.')
                z = 11
            elif ans > n:
                print('That is too high. Guess again!')
            else:
                print('That is too low. Keep guessing!')
    
