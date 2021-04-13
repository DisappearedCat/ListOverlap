import unittest
import main


class Test(unittest.TestCase):
    def test_overlap(self):
        self.assertEqual(main.list_overlap([1, 2, 3], [1, 3]), [1, 3])
        self.assertEqual(main.list_overlap([1, 2, 3], [1]), [1])
        self.assertEqual(main.list_overlap([1, 2, 3, 4, 5, 6], [1, 3]), [1, 3])
        self.assertEqual(main.list_overlap([1, 2, 3], [1, 3, 5, 6, 7, 11]), [1, 3])


if __name__ == '__main__':
    unittest.main()
