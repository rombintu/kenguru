import unittest
from core.translator import Translator

trs = Translator()

simple_words_en = ["hello", "world", "love", "dark", "sun"]
simple_words_ru = ["привет", "мир", "любовь", "темный", "солнце"]

class TestDataEqual(unittest.TestCase):
    def test_check_equal_words(self):
        words_check = simple_words_en
        for i, word in enumerate(simple_words_en):
            assert trs.check_equal_words(word, words_check[i])