#day 5 ques 1

def find_longest_palindrome_in_string(string):
  longest_palindromes = []
  max_length = 0
  for i in range(len(string)):
      for j in range(i, len(string)):
          substring = string[i:j + 1]
          if substring == substring[::-1]:
              if len(substring) > max_length:
                  max_length = len(substring)
                  longest_palindromes = [substring]  
              elif len(substring) == max_length:
                  longest_palindromes.append(substring) 

  return longest_palindromes

print(find_longest_palindrome_in_string("akkadbakkadbambeeb"))
