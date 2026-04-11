import random

symbs = '+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'

def generate_password(len_p):
    created_pwrd = ''
    for i in range(len_p):
        num = random.choice(symbs)
        created_pwrd += symbs[num]

    return created_pwrd

len_pwrd = int(input("Enter the length of the password not less than 4 and not more than 8: "))

while len_pwrd > 8 or len_pwrd < 4:
    len_pwrd = int(input("Please, Enter the correct length of the password: "))

pwrd = generate_password(len_pwrd)
print(f'Your password is: {pwrd}')