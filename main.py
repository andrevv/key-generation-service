from key_generator import KeyGenerator

if __name__ == '__main__':
    alphabet = [chr(char) for char in range(ord('a'), ord('z') + 1)]
    key_generator = KeyGenerator(alphabet=alphabet, key_length=5)
    key_generator.generate()
    print(key_generator.keys[0])
