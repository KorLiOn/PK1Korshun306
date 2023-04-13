import string
from collections import Counter


def read_file(filename):
    with open(filename, encoding="utf8") as file:
        return file.read()


def preprocess_text(text, remove_spaces):
    text = text.lower()
    if remove_spaces:
        text = text.replace(" ", "")
    allowed_chars = set(string.ascii_lowercase + "абвгдеёжзийклмнопрстуфхцчшщъыьэюя")
    text = "".join(filter(lambda char: char in allowed_chars, text))
    return text


def get_char_frequencies(text):
    char_count = Counter(text)
    total_count = sum(char_count.values())
    return {char: count / total_count for char, count in char_count.items()}


def get_bigram_frequencies(text, skip):
    bigram_count = Counter(text[i:i + 2] for i in range(0, len(text) - 1, skip))
    total_count = sum(bigram_count.values())
    return {bigram: count / total_count for bigram, count in bigram_count.items()}


def coincidence_index(text):
    N = len(text)
    freq = {}
    for char in text:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    coincidence_sum = 0
    for letter, count in freq.items():
        coincidence_sum += count * (count - 1)
    coincidence_index = coincidence_sum / (N * (N - 1))
    return coincidence_index


text = preprocess_text(read_file("/Users/roman/PycharmProjects/PK1Korshun/venv/TextTest"), remove_spaces=False)
text_no_spaces = preprocess_text(read_file("/Users/roman/PycharmProjects/PK1Korshun/venv/TextTest"), remove_spaces=True)

char_frequencies = get_char_frequencies(text)
char_frequencies_no_spaces = get_char_frequencies(text_no_spaces)

bigram_frequencies_intersect = get_bigram_frequencies(text, skip=1)
bigram_frequencies_no_intersect = get_bigram_frequencies(text, skip=2)

bigram_frequencies_no_spaces_intersect = get_bigram_frequencies(text_no_spaces, skip=1)
bigram_frequencies_no_spaces_no_intersect = get_bigram_frequencies(text_no_spaces, skip=2)

print("Частоти символів з пробілами:")
print(char_frequencies)

print("Частоти символів без пробілів:")
print(char_frequencies_no_spaces)

print("Частоти біграми з пробілами та перетином:")
print(bigram_frequencies_intersect)

print("Частоти біграми з пробілами і без перетину:")
print(bigram_frequencies_no_intersect)

print("Частоти біграми без пробілів і перетинів:")
print(bigram_frequencies_no_spaces_intersect)

print("Частоти біграми без пробілів і без перетинів:")
print(bigram_frequencies_no_spaces_no_intersect)

print("Індекс відповідності:", coincidence_index("/Users/roman/PycharmProjects/PK1Korshun/venv/TextTest"))
print("Індекс відповідності без пробілів:", coincidence_index(text_no_spaces))
