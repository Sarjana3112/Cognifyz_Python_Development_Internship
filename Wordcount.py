from collections import Counter

filename = input("Enter file name (with .txt): ")

with open(filename, 'r') as file:
    text = file.read().lower()
    words = text.split()

word_count = Counter(words)

for word in sorted(word_count):
    print(f"{word}: {word_count[word]}")