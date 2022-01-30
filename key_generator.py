from random import shuffle


class KeyGenerator:
    def __init__(self, alphabet, key_length):
        self.alphabet = alphabet
        self.key_length = key_length
        self.keys = []

    def generate(self):
        self.generate_keys([])
        shuffle(self.keys)

    def generate_keys(self, key):
        if len(key) == self.key_length:
            self.keys.append(''.join(key))
            return

        for i in range(len(self.alphabet)):
            self.generate_keys(key + [self.alphabet[i]])
