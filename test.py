import unittest

from yo_world import yo

from string_compare import diff_count

class yoworldtesting (unittest.TestCase):
   def test_say_yo(self):
      expected = 'Yo World!'
      self.assertEqual(yo(), expected)


class string_compare_testing (unittest.TestCase):
   def test_identical_string(self):
     self.assertEqual(diff_count('CATCGTAATGACGGCCT','CATCGTAATGACGGCCT'),0)

   def test_different_long_string(self):
     self.assertEqual(diff_count('GAGCCTACTAACGGGAT','CATCGTAATGACGGCCT'),7)

   def test_single_identical_string(self):
     self.assertEqual(diff_count('C','C'),0)

   def test_single_different_string(self):
     self.assertEqual(diff_count('C','A'),1)

   def test_empty_strings(self):
        self.assertEqual(diff_count('', ''), 0)

   def test_different_length_strings(self):
        with self.assertRaises(ValueError):    # with - runs within protective cover
            diff_count('ertg', 'pytedy')

   def test_one_empty_string(self):
        with self.assertRaises(ValueError):
            diff_count('', 'GAGCC')

if __name__ == "__main__":
    unittest.main()
