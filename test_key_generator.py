from unittest import TestCase

from key_generator import KeyGenerator


class TestKeyGenerator(TestCase):
    def test_generate(self):
        alphabet = ['a', 'b', 'c']
        key_generator = KeyGenerator(alphabet=alphabet, key_length=3)
        key_generator.generate()

        self.assertTrue(list(sorted(key_generator.keys)) == [
            'aaa', 'aab', 'aac',
            'aba', 'abb', 'abc',
            'aca', 'acb', 'acc',
            'baa', 'bab', 'bac',
            'bba', 'bbb', 'bbc',
            'bca', 'bcb', 'bcc',
            'caa', 'cab', 'cac',
            'cba', 'cbb', 'cbc',
            'cca', 'ccb', 'ccc',
        ])

    def test_generate_alpha_26_key_3(self):
        alphabet = [chr(char) for char in range(ord('a'), ord('z') + 1)]
        key_generator = KeyGenerator(alphabet=alphabet, key_length=3)
        key_generator.generate()
        self.assertTrue(len(key_generator.keys) == 17576)
