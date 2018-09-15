import unittest
import main

class TestMain(unittest.TestCase):
    def test_hello(self):
        self.assertEqual(main.hello(), "Hello World!")

    def test_puzzle_creation(self):
        total = 0
        puzzle = main.puzzle(2,2)
        puzzle[0][0] = 1
        for row in range(len(puzzle)):
            total += sum(puzzle[row])
        self.assertEqual(total, 1)

if __name__ == '__main__':
    unittest.main()
