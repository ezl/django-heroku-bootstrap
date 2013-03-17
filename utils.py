import string
import random

def random_slug():
    return "".join(random.sample(string.letters+string.digits, 10))


