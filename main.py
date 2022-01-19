import string
import random

a = list(string.ascii_letters + string.digits + "!@#$%^&*()")


def generate_random_password():
    ## length of password from the user
    length = int(input("Enter password length: "))

    ## shuffling the a
    random.shuffle(a)

    ## picking random characters from the list a
    password = []
    for i in range(length):
        password.append(random.choice(a))

    ## shuffling the resultant password
    random.shuffle(password)

    ## converting the list to string
    ## printing the list
    print("".join(password))


## invoking the function
generate_random_password()