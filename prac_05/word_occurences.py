"""
Word Occurrences
Estimated: 40 mins
Actual: 21 mins
CP1404 - William Hunter
"""

word_to_count = {}
sentence = input("Enter sentence: ").lower()
words = sentence.split()

if sentence != "":
    for word in words:
        word_to_count[word] = word_to_count.get(word, 0) + 1

    words = list(word_to_count.keys())
    words.sort()

    max_length = max((len(word) for word in words))
    for word in words:
        print(f"{word:{max_length}} : {word_to_count[word]}")
