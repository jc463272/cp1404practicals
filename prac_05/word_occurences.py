"""
Word Occurrences
Estimated: 40 mins
Actual: 21 mins
CP1404 - William Hunter
"""

word_to_number = {}
sentence = input("Enter sentence: ")
words = sentence.split()

for word in words:
    number_of_letters = word_to_number.get(word, 0)
    word_to_number[word] = number_of_letters + 1

words = list(word_to_number.keys())
words.sort()

max_length = max((len(word) for word in words))
for word in words:
    print(f"{word:{max_length}} : {word_to_number[word]}")
