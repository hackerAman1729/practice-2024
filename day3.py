import string

def stddev(list):
    n = len(list)
    mean = sum(list) / n
    variance = sum((x - mean) ** 2 for x in list) / n
    return variance ** 0.5

print(stddev([2,4,5,6,7,8,9]))

# day 3 ques 2

def merge_intervals(intervals):
  sorted_intervals = sorted(intervals, key=lambda x: x[0])
  merged = []
  for interval in sorted_intervals:
      if not merged or merged[-1][1] < interval[0]:
          merged.append(interval)
      else:
          merged[-1] = (merged[-1][0], max(merged[-1][1], interval[1]))
  return merged

print(merge_intervals([(1, 3), (2, 6), (8, 10), (15, 18)]))


# ques 3

def find_anagram_in_string(string, tofind):
  sen_len = len(string)
  tofind_len = len(tofind)
  index = []
  sorted_tofind = sorted(tofind)
  for i in range(sen_len - tofind_len + 1):
    if sorted(string[i:i+tofind_len]) == sorted_tofind:
      index.append(i)
    
  return index

print(find_anagram_in_string("this is si test string", "is"))


# ques 4

def word_count_in_sen(sentence):
  sentence_no_punct = sentence.translate(str.maketrans('', '', string.punctuation))
  words = sentence_no_punct.split()
  word_count = {}
  for word in words:
    if word in word_count:
      word_count[word] += 1
    else:
      word_count[word] = 1

  return word_count

print(word_count_in_sen("I think I am getting along with python. LoL. These questions are easy though."))
      