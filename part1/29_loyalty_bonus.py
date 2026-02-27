"""
Quick Start: Click Terminal > New Terminal | pwd (check location) | cd part1 (if needed)
Run: python 29_loyalty_bonus.py | Check: python grade_part1.py

Programming exercise: Loyalty Bonus

This program calculates the end of year bonus a customer receives on their loyalty card. The bonus is calculated with the following formula:

If there are less than a hundred points on the card, the bonus is 10 %
In any other case the bonus is 15 %
The program should work like this:

Sample output:

How many points are on your card? 55
Your bonus is 10 %
You now have 60.5 points

But there is a problem with the program, so with some inputs it doesn't work quite right:

How many points are on your card? 95
Your bonus is 10 %
Your bonus is 15 %
You now have 120.175 points

Please fix the program so that there is always either a 10 % or a 15 % bonus, but never both.

"""

# TODO: Fix the code below

points = int(input("How many points are on your card? "))
if points < 100:
    points *= 1.1
    print("Your bonus is 10 %")

if points >= 100:
    points *= 1.15
    print("Your bonus is 15 %")

print("You now have", points, "points")





# Save your file and run it using: python 29_loyalty_bonus.py
# Check: python grade_part1.py

# Commit and push changes to GitHub:
# 1. git add .                                    (stage all changes)
# 2. git commit -m "Completed task 29"             (commit with message)
# 3. git push                                      (push to GitHub)
