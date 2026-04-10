import random

symbs = '+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
created_pwrd = ''

def generate_password(len_p):
    global created_pwrd
    for i in range(len_p):
        num = random.randint(0, len(symbs))
        created_pwrd += symbs[num]

    print(created_pwrd)

len_pwrd = int(input("Enter the length of the password: "))

while len_pwrd > 8 or len_pwrd < 1:
    len_pwrd = int(input("Please, Enter one more time the length of the password: "))

generate_password(len_pwrd)