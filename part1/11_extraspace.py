"""
Quick Start: Click Terminal > New Terminal | pwd (check location) | cd part1 (if needed)
Run: python 11_extraspace.py | Check: python grade_part1.py

Programming exercise: Extra Space

Your friend is working on an app for jobseekers. She sends you this bit of code that works almost correctly, but not quite. This exercise has very strict tests which check the output for every single bit of whitespace.

The program should print out exactly the following:

Sample output:

my name is Tim Tester, I am 20 years old

my skills are
 - python (beginner)
 - java (veteran)
 - programming (semiprofessional)

I am looking for a job with a salary of 2000-3000 euros per month

Please fix the code so that the printout looks right. The easiest way is to use f-strings.
Hint: you can print an empty line by adding an empty print command, or by adding the newline character \n.
"""

# Fix the code below Hint: Use f-strings with print

name = "Tim Tester"
age = 20
skill1 = "python"
level1 = "beginner"
skill2 = "java"
level2 = "veteran"
skill3 = "programming"
level3 = "semiprofessional"
lower = 2000
upper = 3000

print("my name is ", name, " , I am ", age, "years old")
print("my skills are")
print("- ", skill1, " (", level1, ")")
print("- ", skill2, " (", level2, ")")
print("- ", skill3, " (", level3, " )")
print("I am looking for a job with a salary of", lower, "-", upper, "euros per month")





# Save your file and run it using: python 11_extraspace.py
# Check: python grade_part1.py

# Commit and push changes to GitHub:
# 1. git add .                                    (stage all changes)
# 2. git commit -m "Completed task 11"            (commit with message)
# 3. git push                                      (push to GitHub)
