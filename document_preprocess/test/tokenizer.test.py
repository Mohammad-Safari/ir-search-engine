import unittest

from document_preprocess.tokenizer import normalize_tokens, tokenize_text


class TokenizerTests(unittest.TestCase):
    def test_tokenizer(self):
        text = """
            سلام،
            خوبی حالت چطوره؟ بچه‌ها msafari@gmail.com @hey_hi خوبن
            یه عدد خاص 123 دارم
        """
        tokens = tokenize_text(text)
        print(tokens)
        self.assertEqual(len(tokens), 13)

    def test_normalizer(self):
        tokens = ["مي", "توانم", "رئیس", "را", "ملاقات", "کنم"]
        normalized_tokens = normalize_tokens(tokens)
        print(normalized_tokens)
        self.assertEqual(len(normalized_tokens), 5)


if __name__ == "__main__":
    unittest.main()
