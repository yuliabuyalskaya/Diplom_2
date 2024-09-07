import random
import string


def generating_cred():
    def generating(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    creds = {}
    creds['email'] = generating(10) + '@yandex.ru'
    creds['password'] = generating(10)
    creds['name'] = generating(10)
    return creds
