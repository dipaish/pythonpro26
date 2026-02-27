"""
Quick Start: Click Terminal > New Terminal | pwd (check location) | cd part1 (if needed)
Run: python 13_fix_single_line.py | Check: python grade_part1.py

Programming exercise: Fix the code - Print a single line

Each print command usually prints out a line of its own, complete with a change of line at the end. 
However, if the print command is given an additional argument end = "", it will not print a line change.

For example:
print("Hi ", end="")
print("there!")

Sample output:
Hi there!

Please fix this program so that the entire calculation, complete with result, is printed out on a single line. 
Do not change the number of print commands used.
"""

# Fix the code below - do not change the number of print commands
print(5)
print(" + ")
print(8)
print(" - ")
print(4)
print(" = ")
print(5 + 8 - 4)

# Save your file and run it using: python 13_fix_single_line.py

# Commit and push changes to GitHub:
# 1. git add .                                    (stage all changes)
# 2. git commit -m "Completed task 13"            (commit with message)
# 3. git push                                      (push to GitHub)
