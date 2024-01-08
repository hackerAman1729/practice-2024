import string

def func1(input1):
      input1 = input1.lower()
      input1 = input1.translate(str.maketrans('', '', string.punctuation))
      if not input1:  
          return ""

      output = ""
      count = 1
      for i in range(1, len(input1)):
          if input1[i] == input1[i - 1]:
              count += 1
          else:
              output += input1[i - 1] + str(count)
              count = 1

      output += input1[-1] + str(count)

      return output if len(output) < len(input1) else input1

print(func1("aabcccccaaa"))  
