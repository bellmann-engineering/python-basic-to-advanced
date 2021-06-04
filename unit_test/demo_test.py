from demo import Person
import unittest

class TestPerson(unittest.TestCase):

    def test_fullname(self):
        p = Person("Max", "Meier")
        self.assertEqual(p.full_name, "Max Meier")


if __name__ == '__main__':
    unittest.main()
