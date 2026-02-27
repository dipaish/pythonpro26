"""
Quick Start: Click Terminal > New Terminal | pwd (check location) | cd part1 (if needed)
Run: python 17_fix_the_code_product.py | Check: python grade_part1.py

Programming exercise: Fix the Code - Product

This program is supposed to ask for three numbers and then print out their product. 
Please fix the program so that it works correctly.

Sample output:
Please type in the first number: 2
Please type in the second number: 4
Please type in the third number: 5
The product is 40
"""

# Fix the code below

number = int(input("Please type in the first number: "))
number = int(input("Please type in the second number: "))
number = int(input("Please type in the third number: "))

product = number * number * number

print("The product is", product)




# Save your file and run it using: python 17_fix_the_code_product.py
# Check: python grade_part1.py

# Commit and push changes to GitHub:
# 1. git add .                                    (stage all changes)
# 2. git commit -m "Completed task 17"             (commit with message)
# 3. git push                                      (push to GitHub)
