"""
Quick Start: Click Terminal > New Terminal | pwd (check location) | cd part6 (if needed)

Reading input 

Please write a function named read_input, which asks the user for input until the user types in an integer which falls within the bounds given as arguments to the function. The function should return the final valid integer value typed in by the user.

An example of the function in action:

number = read_input("Please type in a number: ", 5, 10)
print("You typed in:", number)
Sample output
Please type in a number: seven
You must type in an integer between 5 and 10
Please type in a number: -3
You must type in an integer between 5 and 10
Please type in a number: 8
You typed in: 8

"""

def read_input(prompt: str, min_val: int, max_val: int) -> int:
    # TODO: Loop until valid input received
    # TODO: Try to convert input to int
    # TODO: Check if value is within range [min_value, max_value]
    # TODO: Print error message if invalid
    # TODO: Return valid integer
    pass

if __name__ == "__main__":
    number = read_input("Please type in a number: ", 5, 10)
    print(f"You typed in: {number}")



# Save your file and run it using: python 17_reading_input.py
# Check: python grade_part6.py

# Commit and push changes to GitHub:
# 1. git add .                                    (stage all changes)
# 2. git commit -m "Completed task 17"         (commit with message)
# 3. git push                                      (push to GitHub)
