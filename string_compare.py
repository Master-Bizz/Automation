'''
string_compare.py

Given two sets of string data of equal length, calculate the positional difference between them
eg:

GAGCCTACTAACGGGAT
CATCGTAATGACGGCCT
^ ^ ^  ^ ^    ^^

differences = 7
'''
# CATCGTAATGACGGCCT
# CATCGTAATGACGGCCT   .. 'zip' function groups everything together as displayed in Shell - print(list(zip(string_a, string_b)))
def diff_count(string_a,string_b):
  if len(string_a) != len(string_b):
     raise ValueError ('Review. Both string_a and string_b must be equal')

  result = []
  for x, y in zip(string_a, string_b):
       if x != y:
         result.append((x,y))
  return len(result)   

