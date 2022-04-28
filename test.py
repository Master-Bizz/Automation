import unittest

from yo_world import yo

from string_compare import diff_count

from test_list import listing
from test_list import lenlist

class yoworldtesting (unittest.TestCase):
   def test_say_yo(self):
      expected = 'Yo World!'
      self.assertEqual(yo(), expected)
     
class lenlist(unittest.TestCase):
   def len_count_list(self):
     self.assertEqual(lenlist([12,21,2,2,2,45,12,8]),True)
     self.assertEqual(lenlist([12,21,2,2,2,45,12]),False)
     
class listing_testing(unittest.TestCase):
   def test_list_True(self):
     self.assertEqual(listing([19,19,8,8,8,641]),True)

   def test_list_True2(self):
     self.assertEqual(listing([19,19,7,5,21,76,8,8,8,641]),True)
     
   def test_list_False(self):
     self.assertEqual(listing([19,1,8,8,8,6]),False)

   def test_list_False2(self):
     self.assertEqual(listing([]),0)    # 0 is == False remember (own exercise)

   def listing_validate_length(self):
      with self.assertRaises(ValueError):
         listing([19,19,7,5,21,76,8,8,8,64,31])
    
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
