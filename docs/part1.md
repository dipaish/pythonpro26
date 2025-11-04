# Part 1: Python Programming Fundamentals

**31 exercises** covering the basics of Python programming: print statements, variables, arithmetic operations, and conditional statements.

---

## 📚 Learning Resources

- **Official Course Material:** [Part 1 - Introduction to Programming](https://dipaish.github.io/programming-24/part-1)
  - [Getting Started](https://dipaish.github.io/programming-24/part-1/1-getting-started) - Print statements and basic syntax
  - [Information from the User](https://dipaish.github.io/programming-24/part-1/2-information-from-the-user) - Input and variables
  - [More About Variables](https://dipaish.github.io/programming-24/part-1/3-more-about-variables) - String operations
  - [Arithmetic Operations](https://dipaish.github.io/programming-24/part-1/4-arithmetic-operations) - Math and calculations
  - [Conditional Statements](https://dipaish.github.io/programming-24/part-1/5-conditional-statements) - if/elif/else logic
- **Tasks Repository:** [GitHub - part1/part1Exercises/tasks/](https://github.com/dipaish/pythonpro26/tree/main/part1/part1Exercises/tasks/)

---

## 🎯 Learning Objectives

By completing Part 1, you will learn to:

- ✅ Write and execute Python programs
- ✅ Use `print()` to display output
- ✅ Get user input with `input()`
- ✅ Store and manipulate data with variables
- ✅ Perform arithmetic operations (`+`, `-`, `*`, `/`, `//`, `%`, `**`)
- ✅ Make decisions using `if`, `elif`, and `else` statements
- ✅ Compare values with comparison operators (`==`, `!=`, `<`, `>`, `<=`, `>=`)
- ✅ Combine conditions with logical operators (`and`, `or`, `not`)

---

## 📋 Course Structure

| Section | Tasks | Topics Covered |
|---------|-------|----------------|
| **Getting Started** | 10 | Basic print statements, user input, string operations |
| **1.1 More About Variables** | 3 | Variable usage, string formatting, fixing errors |
| **1.2 Arithmetic Operations** | 8 | Math operators, calculations, type conversion, integer division |
| **1.3 Conditional Statements** | 10 | if/elif/else, comparisons, boolean logic, decision making |

**Total:** 31 tasks × 1 point each = **31 points**

---

## 🚀 Getting Started

### Option 1: GitHub Codespaces (Recommended)

1. Open your forked repository on GitHub
2. Click **Code** → **Codespaces** → **Create codespace on main**
3. Wait for the environment to load (30-60 seconds)
4. Navigate to Part 1 tasks:
   ```bash
   cd part1/part1Exercises/tasks
   ```

### Option 2: Local Development

1. Clone the repository:
   ```bash
   git clone https://github.com/YOUR_USERNAME/pythonpro26.git
   cd pythonpro26/part1/part1Exercises/tasks
   ```

2. Ensure Python 3.11+ is installed:
   ```bash
   python --version
   ```

---

## 📝 How to Complete Tasks

### Step 1: Open a Task File

All tasks are in: `part1/part1Exercises/tasks/`

Example: `1_emoticon.py`, `1.2.1_times_five.py`, `1.3.1_orwell.py`

### Step 2: Read the Instructions

Each file contains:
- Task description
- Sample input/output
- Hints (if applicable)

### Step 3: Write Your Solution

Replace the TODO comment with your code:

```python
"""
Task: Print a smiley emoticon :-)
"""

# TODO: Write your solution below this line
print(":-)")  # Your solution here
```

### Step 4: Test Your Code

Run the file to see if it works:

```bash
# Windows PowerShell
python 1_emoticon.py

# macOS/Linux
python3 1_emoticon.py
```

### Step 5: Grade Your Work

Run the auto-grader to check all solutions:

```bash
# From the tasks directory
python grade_part1.py
```

The grader will:
- ✓ Test each task's output
- ✓ Award 1 point per correct solution
- ✓ Save progress to `.progress/points.json`
- ✓ Generate a report in `.progress/marksheet.md`

---

## 📖 Section Guides

### Getting Started (10 tasks)

Learn the basics of Python output and input.

**📖 Read:** [Getting Started - University of Helsinki](https://dipaish.github.io/programming-24/part-1/1-getting-started)

#### Key Concepts:
- `print()` function for output
- `input()` function for user input
- String concatenation with `+`
- Escape sequences (`\n` for newline)

#### Example Tasks:

**Task 1: Emoticon**
```python
# Print: :-)
print(":-)")
```

**Task 6: Name Twice**
```python
# Ask for name and print it twice on one line
name = input("Please type in your name: ")
print(name + " " + name)
```

**Task 10: Story**
```python
# Create a story using multiple inputs
name = input("Please tell me your name: ")
year = input("Which year were you born: ")
print("Hi " + name + "! You were born in " + year + ".")
```

---

### Section 1.1: More About Variables (3 tasks)

Master variable usage and output formatting.

**📖 Read:** [More About Variables - University of Helsinki](https://dipaish.github.io/programming-24/part-1/3-more-about-variables)

#### Key Concepts:
- Variables store values
- String formatting techniques
- Multiple print statements vs. single-line output

#### Example Tasks:

**1.1.1 Extra Space**
```python
# Print specific text with proper spacing
print("Peter Python")
print("Paula Pythonson")
print()  # Empty line
print("Peter and Paula are quite a pair!")
```

**1.1.2 Arithmetics**
```python
# Print an arithmetic expression that equals 9
print("5 + 8 - 4 = 9")
```

**1.1.3 Fix the Code - Print Single Line**
```python
# Fix the code to print on one line
print("Hi ", end="")
print("there!")
# Output: Hi there!
```

---

### Section 1.2: Arithmetic Operations (8 tasks)

Learn to perform calculations and work with numbers.

**📖 Read:** [Arithmetic Operations - University of Helsinki](https://dipaish.github.io/programming-24/part-1/4-arithmetic-operations)

#### Key Concepts:
- Basic operators: `+`, `-`, `*`, `/`
- Integer division: `//`
- Modulo (remainder): `%`
- Exponentiation: `**`
- Type conversion: `int()`, `float()`, `str()`

#### Example Tasks:

**1.2.1 Times Five**
```python
# Multiply user input by 5
number = int(input("Please type in a number: "))
print(f"{number} times 5 is {number * 5}")
```

**1.2.3 Seconds in a Day**
```python
# Calculate seconds in given days
days = int(input("How many days? "))
seconds = days * 24 * 60 * 60
print(f"Seconds in {days} days: {seconds}")
```

**1.2.8 Students in Groups**
```python
# Divide students into groups using integer division
students = int(input("How many students on the course? "))
group_size = int(input("Desired group size? "))
groups = students // group_size
print(f"Number of groups formed: {groups}")
```

---

### Section 1.3: Conditional Statements (10 tasks)

Make your programs intelligent with decision-making logic.

**📖 Read:** [Conditional Statements - University of Helsinki](https://dipaish.github.io/programming-24/part-1/5-conditional-statements)

#### Key Concepts:
- `if` statement for single condition
- `elif` for multiple alternative conditions
- `else` for default case
- Comparison operators: `==`, `!=`, `<`, `>`, `<=`, `>=`
- Logical operators: `and`, `or`, `not`

#### Example Tasks:

**1.3.1 Orwell**
```python
# Check if year is 1984
year = int(input("Please type in a number: "))
if year == 1984:
    print("Orwell")
```

**1.3.2 Absolute Value**
```python
# Calculate absolute value without using abs()
number = int(input("Please type in a number: "))
if number < 0:
    print(f"The absolute value is {-number}")
else:
    print(f"The absolute value is {number}")
```

**1.3.5 Calculator**
```python
# Simple calculator with operation choice
num1 = int(input("Number 1: "))
num2 = int(input("Number 2: "))
operation = input("Operation: ")

if operation == "add":
    print(f"{num1} + {num2} = {num1 + num2}")
elif operation == "multiply":
    print(f"{num1} * {num2} = {num1 * num2}")
elif operation == "subtract":
    print(f"{num1} - {num2} = {num1 - num2}")
```

**1.3.7 Daily Wages**
```python
# Calculate wages with double pay on Sunday
hours = int(input("Hours: "))
day = input("Day of the week: ")
hourly_wage = 15

if day == "Sunday":
    wage = hours * hourly_wage * 2
else:
    wage = hours * hourly_wage

print(f"Daily wages: {wage} euros")
```

**1.3.10 Solving a Quadratic Equation**
```python
# Solve ax² + bx + c = 0 using quadratic formula
from math import sqrt

a = float(input("Value of a: "))
b = float(input("Value of b: "))
c = float(input("Value of c: "))

root1 = (-b + sqrt(b**2 - 4*a*c)) / (2*a)
root2 = (-b - sqrt(b**2 - 4*a*c)) / (2*a)

print(f"The roots are {root1} and {root2}")
```

---

## 🎓 Grading & Progress Tracking

### Running the Grader

From the tasks directory:

```bash
cd part1/part1Exercises/tasks
python grade_part1.py
```

### Grading Criteria

Each task is evaluated based on:
- ✓ Correct output format
- ✓ Handling of user input (for interactive tasks)
- ✓ Implementation presence (no empty TODO stubs)

**Scoring:**
- ✅ **Pass (1 point):** Output matches expected result
- ❌ **Fail (0 points):** Incorrect output or no implementation

### Progress Files

- **Points:** `.progress/points.json` (raw scores)
- **Report:** `.progress/marksheet.md` (formatted progress)

Example marksheet output:
```
Part 1: 31/31 ████████████████████ 100%
```

---

## 💡 Tips for Success

### Debugging Tips

1. **Test incrementally:** Run your code after each change
2. **Check output format:** Match sample output exactly (spaces, punctuation, newlines)
3. **Read error messages:** Python tells you what went wrong and where
4. **Use print() for debugging:** Print variable values to see what's happening

### Common Mistakes to Avoid

❌ **Forgetting to convert input:**
```python
age = input("Age: ")  # This is a string!
print(age + 1)  # Error: can't add string and int
```

✅ **Correct approach:**
```python
age = int(input("Age: "))  # Convert to integer
print(age + 1)  # Works!
```

❌ **Using `=` instead of `==` in conditions:**
```python
if year = 1984:  # Error: assignment, not comparison
```

✅ **Correct approach:**
```python
if year == 1984:  # Comparison operator
```

❌ **Incorrect indentation:**
```python
if age >= 18:
print("Adult")  # Error: not indented
```

✅ **Correct approach:**
```python
if age >= 18:
    print("Adult")  # Indented with 4 spaces
```

### Best Practices

- ✅ Use descriptive variable names (`age` instead of `a`)
- ✅ Add spaces around operators for readability (`x + y` not `x+y`)
- ✅ Test with different inputs to ensure your code works generally
- ✅ Commit your work regularly with git

---

## 💾 Saving Your Work

### Git Workflow

After completing tasks:

```bash
# Check what changed
git status

# Add completed tasks
git add part1/part1Exercises/tasks/1_emoticon.py
git add part1/part1Exercises/tasks/1.2.1_times_five.py

# Or add all at once
git add .

# Commit with descriptive message
git commit -m "Complete Part 1 Getting Started tasks (1-10)"

# Push to GitHub
git push
```

### Commit Message Examples

- ✅ `"Complete Part 1 Getting Started (tasks 1-10)"`
- ✅ `"Add Part 1.2 arithmetic operations solutions"`
- ✅ `"Fix Part 1.3.5 calculator logic"`

---

## 📊 Task Checklist

### Getting Started (10/10)

- [ ] 1_emoticon.py - Print a smiley face
- [ ] 2_seven_brothers.py - Print Seven Brothers names
- [ ] 3_row_your_boat.py - Print song lyrics
- [ ] 4_minutes_in_year.py - Calculate minutes in a year
- [ ] 5_print_some_code.py - Print code as text
- [ ] 6_name_twice.py - Input name, print twice
- [ ] 7_name_excalaimation_mark.py - Name with exclamations
- [ ] 8_name_Address.py - Input and display name/address
- [ ] 9_fix_the_code.py - Fix syntax error
- [ ] 10_story.py - Create story with multiple inputs

### Section 1.1: More About Variables (3/3)

- [ ] 1.1.1_extra_space.py - Print with proper spacing
- [ ] 1.1.2_arithmetics.py - Print arithmetic expression
- [ ] 1.1.3_fix_the_code_print_single_line.py - Fix print to single line

### Section 1.2: Arithmetic Operations (8/8)

- [ ] 1.2.1_times_five.py - Multiply by 5
- [ ] 1.2.2_name_and_age.py - Calculate age in 2021
- [ ] 1.2.3_seconds_in_a_day.py - Calculate seconds
- [ ] 1.2.4_fix_the_code_product.py - Fix multiplication bug
- [ ] 1.2.5_sum_and_product.py - Calculate sum and product
- [ ] 1.2.6_sum_and_mean.py - Calculate average
- [ ] 1.2.7_food_expenditure.py - Calculate daily/weekly costs
- [ ] 1.2.8_students_in_groups.py - Integer division practice

### Section 1.3: Conditional Statements (10/10)

- [ ] 1.3.1_orwell.py - Check if year is 1984
- [ ] 1.3.2_absolute_value.py - Calculate absolute value
- [ ] 1.3.3_soup_or_no_soup.py - Seinfeld reference check
- [ ] 1.3.4_order_of_magnitude.py - Compare to 1000/100/10
- [ ] 1.3.5_calculator.py - Simple calculator
- [ ] 1.3.6_temperatures.py - Fahrenheit to Celsius
- [ ] 1.3.7_daily_wages.py - Calculate wages (double on Sunday)
- [ ] 1.3.8_loyalty_bonus.py - Fix bonus calculation
- [ ] 1.3.9_what_to_wear_tomorrow.py - Weather-based advice
- [ ] 1.3.10_solving_a_quadratic_equation.py - Quadratic formula

---

## 🔗 Quick Links

- **Next:** [Part 2 - Conditionals & Loops](part2.md)
- **Main README:** [Course Overview](index.md)
- **Setup Guide:** [Local Development Setup](setup.md)
- **Progress:** Check `.progress/marksheet.md` in your workspace

---

## 🆘 Getting Help

### Resources

- **Course Material:** [programming-24.mooc.fi/part-1](https://dipaish.github.io/programming-24/part-1)
  - [Getting Started](https://dipaish.github.io/programming-24/part-1/1-getting-started)
  - [Information from the User](https://dipaish.github.io/programming-24/part-1/2-information-from-the-user)
  - [More About Variables](https://dipaish.github.io/programming-24/part-1/3-more-about-variables)
  - [Arithmetic Operations](https://dipaish.github.io/programming-24/part-1/4-arithmetic-operations)
  - [Conditional Statements](https://dipaish.github.io/programming-24/part-1/5-conditional-statements)
- **Python Documentation:** [docs.python.org](https://docs.python.org/3/)
- **GitHub Issues:** Report problems or ask questions

### Troubleshooting

**Grader not working?**
- Make sure you're in the correct directory: `part1/part1Exercises/tasks/`
- Check Python version: `python --version` (need 3.11+)

**Task failing but looks correct?**
- Compare your output character-by-character with sample output
- Check for extra spaces, missing newlines, or wrong punctuation
- Ensure variable names match (case-sensitive)

**Import errors?**
- For `from math import sqrt`, make sure it's at the top of the file
- Don't modify the import statements

---

**Good luck! Start with task 1_emoticon.py and work your way through. 🐍✨**
