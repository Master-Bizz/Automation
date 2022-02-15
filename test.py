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

class single_string_testing (unittest.TestCase):
   def test_single_identical_string(self):
     self.assertEqual(diff_count('C','C'),0)

class single_different_string_testing (unittest.TestCase):
   def test_single_different_string(self):
     self.assertEqual(diff_count('C','A'),1)

class empty_strings (unittest.TestCase):
  def test_two_empty_strings(self):
      self.assertEqual(diff_count('', ''), 0)   

class different_length_testing (unittest.TestCase):
   def test_single_different_string(self):    # with - runs within protective cover
     with self.assertRaises(ValueError):
       diff_count('Awsd', 'Gqawse')

class one_empty_string (unittest.TestCase):
   def test_empty_strings(self):
        self.assertRaise(diff_count('', 'Zer')




if __name__ == "__main__":
    unittest.main()
