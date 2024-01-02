def maxfrequency(lst):
  frequency = {}
  for item in lst:
      if item in frequency:
          frequency[item] += 1
      else:
          frequency[item] = 1

  max_freq = max(frequency.values(), default=0)

  most_frequent = [item for item, freq in frequency.items() if freq == max_freq]

  return most_frequent

print(maxfrequency([1, 3, 2, 2, 1, 3, 3, 2, 3, 1, 4]))  
print(maxfrequency([1, 2, 2, 3, 3]))  

  
    