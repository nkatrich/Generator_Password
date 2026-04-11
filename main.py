import random

symbs = '+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'

def generate_password(len_p):
    created_pwrd = []
    for i in range(len_p):
        created_pwrd.append(random.choice(symbs))

    return ''.join(created_pwrd)

while True:
    try:
        len_pwrd = int(input("Enter the length of the password not less than 4 and not more than 8: "))
        if len_pwrd <= 8 and len_pwrd >= 4:
            pwrd = generate_password(len_pwrd)
            print(f'Your password is: {pwrd}')
            break
        else:
            print('The length of number is more than 8' if len_pwrd >= 8 else 'The length of number is less than 4')
            continue
    except ValueError:
        print("Please enter the numbers.")