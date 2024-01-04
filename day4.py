import math 
import string

# day4 ques 1

def is_prime(n):
  if n<=1:
    return False
  elif n>1:
    for i in range(2, int(math.sqrt(n)) +1):
      if n%i==0:
        return False
    return True

print(is_prime(9))

# day4 ques 2
def roman_to_integers(roman):
  roman_dict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
  integers = 0
  for i in range(len(roman)):
    if i+1<len(roman) and roman_dict[roman[i]]<roman_dict[roman[i+1]]:
      integers -= roman_dict[roman[i]]
    else:
      integers += roman_dict[roman[i]]
  return integers

print(roman_to_integers("IX"))

# day4 ques 3
def func(string):
  