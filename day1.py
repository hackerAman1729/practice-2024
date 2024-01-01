import re

def text_analyzer(text):
    words = re.findall(r'\w+', text)  
    num_words = len(words)

    sentences = re.findall(r'[^.!?]+', text)
    num_sentences = len(sentences)

    avg_word_length = sum(len(word) for word in words) / num_words if num_words else 0

    avg_words_per_sentence = num_words / num_sentences if num_sentences else 0

    return {
        "Number of words": num_words,
        "Number of sentences": num_sentences,
        "Average word length": avg_word_length,
        "Average words per sentence": avg_words_per_sentence
    }

text = "Hello world! This is a test. This test is fun."
print(text_analyzer(text))
