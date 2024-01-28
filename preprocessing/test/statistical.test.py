import unittest
from preprocessing.statistical import eliminate_most_frequent_terms, get_most_frequent_terms_with_freq


class StatisticalTests(unittest.TestCase):
    def test_removal(self):
        doc = ["سلام", "خوش", "سلام", "عالی", "سلام", "خوش"]
        most_frequent = get_most_frequent_terms_with_freq({"#": doc}, 2)
        filtered_docs = eliminate_most_frequent_terms({"#": doc}, list(map(lambda tf: tf[0], most_frequent)))
        print(filtered_docs)
        self.assertEqual(len(filtered_docs["#"]), 1)


if __name__ == "__main__":
    unittest.main()
