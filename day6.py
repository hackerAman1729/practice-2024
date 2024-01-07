import string

def count_word(file_path):
    word_count = {}
    with open(file_path, 'r') as file:
        for line in file:
            line_clean = line.translate(str.maketrans('', '', string.punctuation)).lower()
            words = line_clean.split()

            for word in words:
                if word in word_count:
                    word_count[word] += 1
                else:
                    word_count[word] = 1

    return word_count
print(count_word("day6.txt"))

# day6 ques 2

def list_to_dict(input2):
  dict = {}
  for item in input2:
      if '=' in item:
          key, value = item.split('=',1)
          dict[key] = value
  return dict
  
print("\n")
print(list_to_dict(["name==Dunki", "age=30", "city=Laltu"]))

# day6 ques 3

def find_right_max(input3):
  output3 = []
  for i in range(len(input3)):
      found = False
      for k in range(i+1, len(input3)):
          if input3[k] > input3[i]:
              output3.append(input3[k])
              found = True
              break
      if not found:
          output3.append(-1)

  return output3

print("\n")
print(find_right_max([3, 2, 2, 4, 5]))  

# alt approach

def find_right_max_stack(input3):
  output3 = [-1] * len(input3)
  stack = []

  for i, num in enumerate(input3):
      while stack and input3[stack[-1]] < num:
          output3[stack.pop()] = num
      stack.append(i)

  return output3

print(find_right_max_stack([3, 2, 2, 4, 5]))  
  
