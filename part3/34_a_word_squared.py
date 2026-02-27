"""
Quick Start: Click Terminal > New Terminal | pwd (check location) | cd part3 (if needed)
Run: python 34_a_word_squared.py | Check: python grade_part3.py

A Word Squared

Task: Please write a function named squared, which takes a string argument and an integer argument, and prints out a square of characters as specified by the examples below.

squared("ab", 3)
print()
squared("aybabtu", 5)

Sample output

aba
bab
aba

aybab
tuayb
abtua
ybabt
uayba

Instructions:
- Write a function named squared
- It takes two parameters: a string (word) and an integer (size)
- It prints a square pattern where each line contains 'size' characters
- Each line starts at a different offset, cycling through the word
- Line i starts at position (i * size) in the word, wrapping around
- The function doesn't return anything
"""

# TODO: Write your solution below this line





# Testing the function
if __name__ == "__main__":
    squared("ab", 3)
    print()
    squared("aybabtu", 5)

# Save your file and run it using: python 34_a_word_squared.py
# Check: python grade_part3.py

# Commit and push changes to GitHub:
# 1. git add .                                    (stage all changes)
# 2. git commit -m "Completed task 34"         (commit with message)
# 3. git push                                      (push to GitHub)
