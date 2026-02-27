"""
Quick Start: Click Terminal > New Terminal | pwd (check location) | cd part2 (if needed)
Run: python 17_fix_the_code_countdown.py | Check: python grade_part2.py

This program should print out a countdown. The code has errors - please fix the program so it works correctly.

The program should print:

Countdown!
5
4
3
2
1
Now!

"""

# TODO: Fix the solution below this line

number = 5
print("Countdown!")
while True:
  print(number)
  number = number - 1
  if number > 0:
    break

print("Now!")


# Save your file and run it using: python 17_fix_the_code_countdown.py
# Check: python grade_part2.py

# Commit and push changes to GitHub:
# 1. git add .                                    (stage all changes)
# 2. git commit -m "Completed task 17"            (commit with message)
# 3. git push                                      (push to GitHub)
