from yo_world import yo
print(yo())
from string_compare import diff_count


print(diff_count('CATCGTAATGACGGCCT','GAGCCTACTAACGGGAT')) # gives written error when strings/parameters are not the same/equal
print(diff_count('CATCGTAATGACGGCCT','GAGCCTACTAACGGGAT'))
print (diff_count('GAGCC', 'GAGCC'))


print('TDD, Test Driven Development')

print('Yo World!' not in yo())

print('Bla Bla Black Sheep,\n\thave you any Wool,\bBla Bla,\fno sir\vbut i have all the toolz')
print('a'== 'b')
print(not('a '== 'b'))
print(not('a '!= 'b'))

#===========================

print(2**5)
print(pow(2,5))


quads = []
for i in range(10):
   quads.append(pow(i,2.325))
print(quads)

ease = ([pow(s,5) for s in range(15)])
print(ease)

for A in "Liam Bizzl3":
   print(A)


#
import math

print(int(1905/100))
print(5%100)

string = "timeflies"
print(string[1:-3:2])
print(string[1:3:1])
# Reades the same in reverse! = Palindrome
print(string[::-1])
print(string[::-2])
print(string)
print(string[1:-3:3])

jee = 'print(231/3,34*34)'
exec(jee)
eval(jee)

print(abs(-23.34))
print(abs(-23))
print(abs(23))

print(bool(4.5))
print(bool(0))
print(bool(-30))
print(bool(30))

now = [12,12,12,23,45,45,12,45]
print(now.count(12))
print(now.count(23))
print(now.count(45))
now.append('9')
print(now)
now.insert(0,7)
print(now)
now.insert(4,['nice', 'day'])
print(now)
now.remove(23)
print(now)
now[9]=10
print(now)
print(len(now))

print(all(now))

from test_list import listing

print(listing(lista=[19,19,1,7,8,8]))
print(listing(lista=[19,19,1,8,8,8]))
print(listing(lista=[19,19,7,5,21,76,8,8,8,6,4,3,1]))
print(listing(lista=[19,19,7,5,21,76,8,8,8,64,31]))

print(not(5==6))

class moose:
  z=5
qw=moose()
print(qw.z)

class Person:
  def __init__(self, fname, lname):
    self.fname = fname
    self.lname = lname
  def print_name(self):
    print(self.fname)
    print(self.lname)
  def into_self(self):
    print (f'The names.. {self.lname}, {self.fname} {self.lname}.')
class Student(Person):
   pass
  

v = Student(fname='zee', lname='jones')
v.print_name()
p = Person(fname='Dwain', lname='kase')
print(p.lname)
print(v.into_self())
p.into_self()
print(dir(Person))

from test_list import lenlist

print(lenlist(newl=[12,12,3,4,5,5,5,8]))
print(lenlist(newl=[12,12,3,4,5,5,8]))
print(lenlist(newl=[12,12,3,4,5,5,5]))
print('-------- numberic types --------')
print(5%2) # gives remainder after dividing; remainder is final output
print(123%32)
print(139/4)
print(139//4) # answer rounded down regardless
print(5//2) #  ''  answer rounded down
print(math.floor(5//2)) # same thing
print(divmod(139,4)) # gives; floored division '//',THEN remaindered division '%' answers
y = 6 + 3j
print(y.conjugate())
y = 6 - 3j
print(y.conjugate())
print(6*3j)
y = 6 * 3j
print(y.conjugate())
y = 3j
print(y.conjugate())
y = 6 ** 3j
p= 80
i=3
print(y.conjugate())
print(complex(p, i))

print('------- break------')
# Binary <..64 32 16 8 4 2 1 - pow(b,2) ...|...: 1 = On/Yes, 0 = Off/No
print(bin(83))
print(int(0b1010011))
print(0b1010011 == 83)
print(83 == 0b1010011)
print(21 == 0b10101)
print(p&i) # If Both corresponding bits are 1 then output is 1, else 0 for any other combination
print(p|i) # If Both corresponding bits are 0 then output is 0, else 1 for any other combination
print(p^i)# If Both corresponding bits are 0 then output is 0 + If Both corresponding bits are 1 then output is 0, else 1 for any other combination
print(~83) # Binary numbers inverted representing a different number
print(83>>3) # Binary numbers shifted right x times (3 in this case)
print(83<<3) # vise vesa for the left
def test(n):
  return n > 4**4 and n % 34 == 4 # mod = %, 
print(test(950))
print(test(922))
def test(a):
  return [a+(2*i) for i in range(a)]  # order of evaluation: Parenthesis - power - multiplication/division - add/subtract.. Left to Right
print(test(7))
print(test(4))

def solution(inputArray): # finding the product of two highest numbers adjacent
   return max([inputArray[x] * inputArray[x+1] for x in range(len(inputArray)-1)])
print(solution([12,23,4,5]))

def solution(n):  # shape area - finding the area
    return (n-1)**2 + pow(n,2)

  
total4 = 0
for i in range(1,100):  # adding multliples of 3 and 5
   if i % 3 == 0 or i % 5 == 0:
     total4+=i
print(total4)

def solution(n):  # add digits in an integer
     total = 0
     while n != 0:
         x = n % 10
         total = total + x
         n = math.floor(n/10)
     return total
print(solution(354))

tot = 0
for i in [5, 4, 3, 2, 1] :
    tot = tot + 1
print(tot)

def computepay(h, r):
   if h > 40:
         print('Overtime Included !!!')
         reg = h * r 
         overtime = (h - 40.0) * (r * 0.50)
         return reg + overtime
         
   else:
     print('Regular Pay !!!')
     reg = h * r 
     return reg 
     
h = input("Enter Hours: ")
fh = float(h)
p = computepay(fh, 10.50)
print("Pay", p)

#  -----------SIGH
largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done":
       break # skips to end
    print(num) 
    try:
       inum = int(num)
    except:
       print ('Invalid input')
       continue # Loops back to top
    if smallest == None and largest == None:
        smallest = inum
        largest = inum
    elif inum > largest: 
        largest = inum
    elif inum < smallest: 
        smallest = inum

print("Maximum", largest)
print("Minimum", smallest)
