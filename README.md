# Whisper100MillionWords

Whisper100MillionWords is a Python-based fun program to generate extremely large datasets of random words and efficiently pick random words from them.
  - Generates up to **100 million random words**.
  - Each word has a random length between configurable limits (default 4 to 100 characters).
  - Saves the generated words efficiently to a text file.
  - **Efficient Random Word Selection:**: Picks a random word from the generated file without loading the entire file into memory.
  - Handles very large files (5GB+ and more) efficiently.
  - **New Word Generation from Existing Words:** If a randomly picked word is longer than 10 letters, you can generate a new random word using letters only from the picked word.

## The Output
```
PS C:\Users\username\Desktop\manojchandra.co.uk> python rwp.py
100000000 random words saved to 'random_words.txt'.
Picking a random word now.
jsailpolveeyaosuelbyenmainndydosuoruszoanlym
snlyjmay
```
