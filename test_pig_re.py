import pig_latin_re
import unittest

class TestPig(unittest.TestCase):
    def setUp(self):
        self.pig=pig_latin_re.pig_latin
        return super().setUp()
    def test_word_start_vowel(self):
        word='anguandia'
        self.assertEqual(self.pig(word), 'anguandiaway')
    def test_word_start_consonant(self):
        word='mike'
        self.assertEqual(self.pig(word), 'ikemay')
    def test_word_not_in_english(self):
        word='mo$es'
        self.assertEqual(self.pig(word), 'word not english')
    def test_word_has_no_vowel(self):
        word='mxqrt'
        self.assertEqual(self.pig(word), 'no vowel in word')
    def test_word_cannot_start_non_alphabet(self):
        word='-mal'
        self.assertEqual(self.pig(word), 'word must start with alphabet')

if __name__=="__main__":
    unittest.main()