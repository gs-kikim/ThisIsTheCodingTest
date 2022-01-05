import unittest

import src.Array.Q23 as Q23
from src.Array import Q24


class TestGreedy(unittest.TestCase):
    def test_Q23(self):
        self.assertEqual(Q23.array_Q23(12, ["Junkyu 50 60 100",
                                            "Sangkeun 80 60 50",
                                            "Sunyoung 80 70 100",
                                            "Soong 50 60 90",
                                            "Haebin 50 60 100",
                                            "Kangsoo 60 80 100",
                                            "Donghyuk 80 60 100",
                                            "Sei 70 70 70",
                                            "Wonseob 70 70 90",
                                            "Sanghyun 70 70 80",
                                            "nsj 80 80 80",
                                            "Taewhan 50 60 90"]),
                         ["Donghyuk", "Sangkeun", "Sunyoung", "nsj", "Wonseob", "Sanghyun", "Sei", "Kangsoo", "Haebin",
                          "Junkyu", "Soong", "Taewhan"])

    def test_Q24(self):
        self.assertEqual(Q24.array_Q24(4,[5,1,7,9]),5)

if __name__ == '__main__':
    unittest.main()
