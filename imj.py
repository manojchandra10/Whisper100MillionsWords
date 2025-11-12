import os
import random
import string

# def generate_random_words(num_words, min_length=4, max_length=None):
#     words = []
#     for _ in range(num_words):
#         if max_length:
#             word_length = random.randint(min_length, max_length)
#         else:
#             # Random length:
#             word_length = random.randint(min_length, 100)
#         word = ''.join(random.choices(string.ascii_lowercase, k=word_length))
#         words.append(word)
#     return words

# # Number of words
# num_words = 100000000
# # Generate words
# words = generate_random_words(num_words)
# # Save to a file
# with open("random_words.txt", "w") as f:
#     for word in words:
#         f.write(word + "\n")
# print(f"{num_words} random words saved to 'random_words.txt'.")

# #now pick a random word

# # with open("random_words.txt", "r") as f:
#     # words = f.read().splitlines()
# # words_to_pick_from = words[10000:]
# # random_word = random.choice(words_to_pick_from)
# # print(random_word)
# # Output: MemoryError!
# file_path = "random_words.txt"
# skip_lines = 10000
# offsets = []
# with open(file_path, "r") as f:
#     offset = 0
#     for i, line in enumerate(f):
#         if i >= skip_lines:
#             offsets.append(offset)
#         offset += len(line)

# rand_offset = random.choice(offsets)
# with open(file_path, "r") as f:
#     f.seek(rand_offset)
#     random_word = f.readline().strip()
# print(random_word)

# Further improved code
file_path = "random_words.txt"
num1_words = 100_000_000
# Only generate file if it doesn't exist
if not os.path.exists(file_path):
    num_words = 100_000_000
    with open(file_path, "w") as f:
        for _ in range(num_words):
            word_length = random.randint(4, 100)
            word = ''.join(random.choices(string.ascii_lowercase, k=word_length))
            # Save to a file
            f.write(word + "\n")
    print(f"{num_words} random words saved to '{file_path}'")
else:
    # print("Picking a random word now.")
    print(f"{num1_words} random words saved to '{file_path}'\nPicking a random word now.")

# Pick a random word
skip_lines = 10000
offsets = []

with open(file_path, "r") as f:
    offset = 0
    for i, line in enumerate(f):
        if i >= skip_lines:
            offsets.append(offset)
        offset += len(line)

rand_offset = random.choice(offsets)
with open(file_path, "rb") as f:
    f.seek(rand_offset)
    random_word = f.readline().decode("utf-8").strip()

print(random_word)

# Create new word from random letters if it's too long
if len(random_word) > 10:
    new_length = random.randint(4, 10)
    new_random_word = ''.join(random.choices(random_word, k=new_length))
    print(new_random_word)
else:
    print(random_word)