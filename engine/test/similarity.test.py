import unittest

from engine.similarity import (
    _calculate_cosine_similarity,
    _calculate_dot_product,
    vectorize_query,
)


class SimilarityTests(unittest.TestCase):
    def test_query_vectorize(self):
        query = """
            سلام،
            دانشجوها
            دولت
        """
        query_vector = vectorize_query(query)
        print(query_vector)
        self.assertEqual(len(query_vector), 3)

    def test_dot_product(self):
        query_vector = {"سلام": 1, "دولت": 1, "دانشجو": 1}
        idf = {"سلام": 0.7, "تست": 0.1, "استاد": 0.2, "دانشجو": 0.3}
        dot_product = _calculate_dot_product(query_vector, idf)
        print(dot_product)
        self.assertEqual(dot_product, 1.0)

    def test_cosine_similarity(self):
        query_vector = {"سلام": 1, "دولت": 1, "دانشجو": 1}
        idf = {"سلام": 0.7, "تست": 0.1, "استاد": 0.2, "دانشجو": 0.3, "پروژه": 0.1}
        similarity = _calculate_cosine_similarity(query_vector, idf)
        print(similarity)
        self.assertEqual(similarity, 10 / 8)


if __name__ == "__main__":
    unittest.main()
