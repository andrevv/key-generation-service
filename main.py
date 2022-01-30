import os

import constants
from key_generator import KeyGenerator
from dotenv import load_dotenv

load_dotenv()

ALPHABET = os.getenv(constants.ALPHABET)
KEY_LENGTH = int(os.getenv(constants.KEY_LENGTH))

if __name__ == '__main__':
    key_generator = KeyGenerator(alphabet=ALPHABET, key_length=KEY_LENGTH)
    key_generator.generate()
    print(key_generator.keys[0])
