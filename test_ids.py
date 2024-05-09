
import random
import string


for t in range(50):

    letters = string.ascii_uppercase
    digits = string.digits
    key = ''.join(random.choices(digits, k=9))

    with open("/home/smart200481xx/spvk/n_env/test_ids.txt", "a") as myfile:
        myfile.write(f'{key} \n')

    t += 1

myfile.close()
