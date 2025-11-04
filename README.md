# Python Programming Course - Complete Task List

[![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-sa/4.0/)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)

***A comprehensive auto-graded Python programming tasks repo with **168 exercises** across 6 parts.***

This repository contains the aligned, auto-graded exercises for the course [Fundamentals of Programming - Python](https://dipaish.github.io/programming-24/) which is adapted from the University of Helsinki’s [Introduction to Programming (Programming MOOC)](https://programming-24.mooc.fi/) course.

> 🚀 **No installation required!** Use GitHub Codespaces to start coding in your browser instantly.

## 📊 Tasks Overview

| Part | Topics | Tasks | Learning Materials |
|------|--------|-------|-------|
| [Part 1](#part-1-fundamentals-31-tasks) | Fundamentals | 31 | [Part 1](https://dipaish.github.io/programming-24/part-1) |
| [Part 2](#part-2-conditionals--loops-22-tasks) | Conditionals & Loops | 22 | [Part 2](https://dipaish.github.io/programming-24/part-2)  |
| [Part 3](#part-3-loops--functions-34-tasks) | Loops & Functions | 34 | [Part 3](https://dipaish.github.io/programming-24/part-3)  |
| [Part 4](#part-4-functions--lists-37-tasks) | Functions & Lists | 37 | [Part 4](https://dipaish.github.io/programming-24/part-4)  |
| [Part 5](#part-5-advanced-topics-25-tasks) | Advanced Topics (Optional*) | 25 | [Part 5](https://dipaish.github.io/programming-24/part-5)  |
| [Part 6](#part-6-file-handling--errors-19-tasks) | File Handling & Errors | 19 | [Part 6](https://dipaish.github.io/programming-24/part-6) |

**Total: 168 exercises** (**Part 5** is optional and not counted toward the total score)

## 🚀 Quick Start Options

### Option 1: GitHub Codespaces (Recommended - No Setup!)
**Perfect for students without Python installed**

**Steps to get started:**

1. **Fork this repository** to your GitHub account
   - Click the **"Fork"** button at the top-right of this page
   - This creates your own copy of the repository

2. **Create a Codespace**
   - Go to your forked repository
   - Click the **"<> Code"** button (green button)
   - Select the **"Codespaces"** tab
   - Click **"Create codespace on main"**

3. **Start coding!**
   - Wait 30-60 seconds for your environment to load
   - Your browser-based VS Code will open automatically
   - All Python tools and extensions are pre-installed

**Features:**
- ✅ Pre-configured Python 3.11
- ✅ All VS Code extensions installed
- ✅ Auto-save enabled
- ✅ Integrated terminal and debugger
- ✅ Works on any device (desktop, tablet, mobile)
- ✅ Free 60 hours/month

📖 **[Complete Codespaces Guide →](.devcontainer/README.md)**

### Option 2: Local Development
**For those who prefer working on their own computer**

**Requirements:**
- Python 3.11 or higher
- Git (for version control)
- Visual Studio Code (recommended editor)
- VS Code Python extensions

**📖 Complete Setup Guide:** **[→ LOCAL_SETUP_GUIDE.md](LOCAL_SETUP_GUIDE.md)**

This comprehensive guide covers:
- ✅ Installing Python on Windows, macOS, and Linux
- ✅ Installing Git and GitHub Desktop
- ✅ Installing Visual Studio Code
- ✅ Setting up VS Code extensions for Python
- ✅ Signing in with your GitHub account
- ✅ Cloning this repository
- ✅ Verifying your setup works
- ✅ Troubleshooting common issues

---

## 🎯 How to Use This Course

1. Navigate to each part's folder (e.g., `part1/part1Exercises/tasks/`)
2. Complete the exercises in the task files
3. Run the grader: `python grade_partX.py`
4. Check your progress in `.progress/marksheet.md`

Each task is worth **1 point**. Your live progress is tracked automatically in `.progress/marksheet.md`.

## 📚 For Students

### ✅ What You Should Edit:
- **All task files**: `1_emoticon.py`, `2_seven_brothers.py`, `1.1.1_extra_space.py`, etc.
- Work on the exercises and implement your solutions

### ❌ What You Should NOT Edit:
- **Grader files**: `grade_part1.py`, `grade_part2.py`, etc.
- **README files**: All documentation files
- **Task specification files**: `p*Alltasks.md`, `part*alltasks.md`
- **Progress tracking**: `.progress/` folder contents

> **⚠️ Important:** Solutions are auto-graded. Modifying them compromises learning and accurate self-assessment.

---

## Part 1: Fundamentals (31 tasks)

### Getting Started (10 tasks)
1. `1_emoticon.py` - Print an emoticon
2. `2_seven_brothers.py` - Print Seven Brothers poem
3. `3_row_your_boat.py` - Print Row Your Boat song
4. `4_minutes_in_year.py` - Calculate minutes in a year
5. `5_print_some_code.py` - Print example code
6. `6_name_twice.py` - Input and print name twice
7. `7_name_excalaimation_mark.py` - Name with exclamation marks
8. `8_name_Address.py` - Name and address input
9. `9_fix_the_code.py` - Fix syntax error in code
10. `10_story.py` - Create a story with user input

### Section 1.1: More about variables (3 tasks)
1. `1.1.1_extra_space.py` - Print text with proper spacing
2. `1.1.2_arithmetics.py` - Print arithmetic expression (5 + 8 - 4 = 9)
3. `1.1.3_fix_the_code_print_single_line.py` - Fix print to output on single line

### Section 1.2: Arithmetic operations (8 tasks)
1. `1.2.1_times_five.py` - Multiply input by 5
2. `1.2.2_name_and_age.py` - Calculate age in year 2021
3. `1.2.3_seconds_in_a_day.py` - Calculate seconds in given days
4. `1.2.4_fix_the_code_product.py` - Fix bug (+ should be *)
5. `1.2.5_sum_and_product.py` - Calculate sum and product of two numbers
6. `1.2.6_sum_and_mean.py` - Calculate sum and mean of four numbers
7. `1.2.7_food_expenditure.py` - Calculate daily/weekly food costs
8. `1.2.8_students_in_groups.py` - Divide students into groups (integer division)

### Section 1.3: Conditional statements (10 tasks)
1. `1.3.1_orwell.py` - Check if year is 1984
2. `1.3.2_absolute_value.py` - Calculate absolute value
3. `1.3.3_soup_or_no_soup.py` - No soup for Jerry! (Seinfeld reference)
4. `1.3.4_order_of_magnitude.py` - Compare to 1000, 100, 10
5. `1.3.5_calculator.py` - Simple calculator (add, multiply, subtract)
6. `1.3.6_temperatures.py` - Convert Fahrenheit to Celsius
7. `1.3.7_daily_wages.py` - Calculate wages (double pay on Sunday)
8. `1.3.8_loyalty_bonus.py` - Fix bonus calculation bug (if/elif)
9. `1.3.9_what_to_wear_tomorrow.py` - Weather-based clothing advice
10. `1.3.10_solving_a_quadratic_equation.py` - Solve quadratic equations using formula

---

## Part 2: Conditionals & Loops (22 tasks)

### Section 2.1: Programming terminology (3)
1. `2.1.1_fix_syntax.py` - Fix syntax errors
2. `2.1.2_number_of_characters.py` - Count characters in string
3. `2.1.3_typecasting.py` - Type conversion exercises

### Section 2.2: More conditionals (4)
1. `2.2.1_age_of_maturity.py` - Check if age >= 18
2. `2.2.2_greater_than_or_equal_to.py` - Compare two numbers
3. `2.2.3_the_elder.py` - Find older person
4. `2.2.4_alphabetically_last.py` - Find alphabetically last word

### Section 2.3: Combining conditions (7)
1. `2.3.1_age_check.py` - Check age range
2. `2.3.2_nephews.py` - Donald Duck's nephews
3. `2.3.3_grades_and_points.py` - Convert points to grades
4. `2.3.4_fizzbuzz.py` - Classic FizzBuzz
5. `2.3.5_leap_year.py` - Check if leap year
6. `2.3.6_alphabetically_in_the_middle.py` - Find middle word
7. `2.3.7_gift_tax_calculator.py` - Calculate gift tax

### Section 2.4: Simple loops (8)
1. `2.4.1_shall_we_continue.py` - Continue prompt loop
2. `2.4.2_input_validation.py` - Validate numeric input
3. `2.4.3_fix_the_code_countdown.py` - Fix countdown loop
4. `2.4.4_repeat_password.py` - Password confirmation
5. `2.4.5_pin_and_number_of_attempts.py` - PIN with attempts
6. `2.4.6_the_next_leap_year.py` - Find next leap year
7. `2.4.7_story.py` - Build story with loop
8. `2.4.8_working_with_numbers.py` - Number operations loop

---

## Part 3: Loops & Functions (34 tasks)

### Section 3.1: Loops with conditions (7)
1. `3.1.1_print_numbers.py` - Print even numbers 2-30
2. `3.1.2_fix_the_code_countdown.py` - Fix countdown syntax errors
3. `3.1.3_numbers.py` - Print 1 to n
4. `3.1.4_powers_of_two.py` - Powers of 2 up to limit
5. `3.1.5_powers_of_base_n.py` - Powers of base n up to limit
6. `3.1.6_sum_of_consecutive_numbers_v1.py` - Sum until limit (result only)
7. `3.1.7_sum_of_consecutive_numbers_v2.py` - Sum with calculation shown

### Section 3.2: Working with strings (15)
1. `3.2.1_string_multiplied.py` - Repeat string n times
2. `3.2.2_the_longer_string.py` - Compare string lengths
3. `3.2.3_end_to_beginning.py` - Print reversed character by character
4. `3.2.4_second_and_second_to_last.py` - Compare 2nd and 2nd-to-last chars
5. `3.2.5_a_line_of_hashes.py` - Print line of # characters
6. `3.2.6_a_rectangle_of_hashes.py` - Print hash rectangle
7. `3.2.7_underlining.py` - Underline strings with dashes
8. `3.2.8_right_aligned.py` - Right-align with * padding
9. `3.2.9_a_framed_word.py` - Center word in asterisk frame
10. `3.2.10_substrings_part1.py` - Substrings from beginning
11. `3.2.11_substrings_part2.py` - Substrings from end
12. `3.2.12_does_it_contain_vowels.py` - Check for vowels a, e, o
13. `3.2.13_find_the_first_substring.py` - First 3-char substring match
14. `3.2.14_find_all_substrings.py` - All 3-char substring matches
15. `3.2.15_the_second_occurrence.py` - Second non-overlapping occurrence

### Section 3.3: More loops (5)
1. `3.3.1_multiplication.py` - Multiplication table
2. `3.3.2_first_letters_of_words.py` - Extract first letter of each word
3. `3.3.3_factorial.py` - Calculate n!
4. `3.3.4_flip_the_pairs.py` - Swap adjacent characters
5. `3.3.5_taking_turns.py` - Alternate characters from two strings

### Section 3.4: Defining functions (7)
1. `3.4.1_seven_brothers.py` - Return list of Seven Brothers names
2. `3.4.2_the_first_character.py` - Return first character
3. `3.4.3_mean.py` - Calculate mean of three numbers
4. `3.4.4_print_many_times.py` - Print string n times
5. `3.4.5_a_square_of_hashes.py` - Print hash square
6. `3.4.6_chessboard.py` - Print 1/0 chessboard pattern
7. `3.4.7_a_word_squared.py` - Print word in special square pattern

---

## Part 4: Functions & Lists (37 tasks)

### Section 4.1: More functions (10)
1. `4.1.1_line.py` - Draw line with character
2. `4.1.2_a_box_of_hashes.py` - Draw hash box
3. `4.1.3_a_square_of_hashes.py` - Draw hash square
4. `4.1.4_a_square.py` - Draw square with character
5. `4.1.5_a_triangle.py` - Draw triangle
6. `4.1.6_a_shape.py` - Draw combined shape
7. `4.1.7_a_spruce.py` - Draw spruce tree
8. `4.1.8_the_greatest_number.py` - Find greatest of three
9. `4.1.9_same_characters.py` - Check character equality
10. `4.1.10_first_second_last_words.py` - Extract words from string

### Section 4.2: Lists (8)
1. `4.2.1_change_value.py` - Modify list element
2. `4.2.2_add_items.py` - Add items to list
3. `4.2.3_addition_and_removal.py` - List operations
4. `4.2.4_same_word_twice.py` - Check for duplicates
5. `4.2.5_list_twice.py` - Check if list appears twice
6. `4.2.6_length_of_list.py` - Get list length
7. `4.2.7_arithmetic_mean.py` - Calculate mean of list
8. `4.2.8_range_of_list.py` - Calculate range (max-min)

### Section 4.3: Definite iteration (12)
1. `4.3.1_star_studded.py` - Add stars around items
2. `4.3.2_negative_to_positive.py` - Convert negatives
3. `4.3.3_list_of_stars.py` - Create star patterns
4. `4.3.4_anagrams.py` - Check if anagrams
5. `4.3.5_palindromes.py` - Check if palindrome
6. `4.3.6_sum_of_positives.py` - Sum positive numbers
7. `4.3.7_even_numbers.py` - Filter even numbers
8. `4.3.8_sum_of_lists.py` - Sum two lists element-wise
9. `4.3.9_distinct_numbers.py` - Remove duplicates
10. `4.3.10_length_of_longest.py` - Find longest string
11. `4.3.11_shortest.py` - Find shortest string
12. `4.3.12_all_the_longest.py` - Find all longest strings

### Section 4.4: Print statement formatting (1)
1. `4.4.1_integers_to_strings.py` - Format integers as strings

### Section 4.5: More strings and lists (6)
1. `4.5.1_everything_reversed.py` - Reverse list and strings
2. `4.5.2_most_common_character.py` - Find most common character
3. `4.5.3_no_vowels_allowed.py` - Remove vowels
4. `4.5.4_no_shouting_allowed.py` - Remove uppercase
5. `4.5.5_neighbours_in_list.py` - Find longest consecutive sequence
6. `4.5.6_grade_statistics.py` - Grade statistics calculator

---

## Part 5: Advanced Topics (25 tasks)

### Section 5.1: More lists (7)
1. `5.1.1_the_longest_string.py` - Find longest string in list
2. `5.1.2_number_of_matching_elements.py` - Count matching elements
3. `5.1.3_go.py` - Determine Go game winner
4. `5.1.4_sudoku_check_row.py` - Validate sudoku row
5. `5.1.5_sudoku_check_column.py` - Validate sudoku column
6. `5.1.6_sudoku_check_block.py` - Validate sudoku block
7. `5.1.7_sudoku_check_grid.py` - Validate entire sudoku grid

### Section 5.2: References (6)
1. `5.2.1_items_multiplied_by_two.py` - Double list items in-place
2. `5.2.2_remove_the_smallest.py` - Remove smallest from list
3. `5.2.3_sudoku_print_grid.py` - Print sudoku grid
4. `5.2.4_sudoku_copy_and_add.py` - Copy and add number
5. `5.2.5_tic_tac_toe.py` - Place piece on board
6. `5.2.6_transpose_matrix.py` - Transpose matrix

### Section 5.3: Dictionary (9)
1. `5.3.1_times_ten.py` - Create dictionary with values × 10
2. `5.3.2_factorials.py` - Factorial dictionary
3. `5.3.3_histogram.py` - Character histogram
4. `5.3.4_phone_book_v1.py` - Phone book (one number)
5. `5.3.5_phone_book_v2.py` - Phone book (multiple numbers)
6. `5.3.6_invert_dictionary.py` - Swap keys and values
7. `5.3.7_numbers_spelled_out.py` - Number to word dictionary
8. `5.3.8_movie_database.py` - Add movies to database
9. `5.3.9_find_movies.py` - Search movie database

### Section 5.4: Tuple (5)
1. `5.4.1_create_tuple.py` - Create tuple from numbers
2. `5.4.2_the_oldest_person.py` - Find oldest person
3. `5.4.3_older_people.py` - Filter people by age
4. `5.4.4_student_database.py` - Student course tracker
5. `5.4.5_square_of_letters.py` - Letter square pattern

---

## Part 6: File Handling & Errors (19 tasks)

### Section 6.1: Reading files (9)
1. `6.1.1_largest_number.py` - Find largest number in file
2. `6.1.2_fruit_market.py` - Read fruit prices from file
3. `6.1.3_matrix.py` - Matrix sum and max from file
4. `6.1.4_course_grading_part1.py` - Student exercises from files
5. `6.1.5_course_grading_part2.py` - Add exam points
6. `6.1.6_course_grading_part3.py` - Calculate grades
7. `6.1.7_spell_checker.py` - Check spelling with wordlist
8. `6.1.8_recipe_search.py` - Search recipes by criteria
9. `6.1.9_city_bikes.py` - Parse city bike data

### Section 6.2: Writing files (7)
1. `6.2.1_inscription.py` - Write personalized inscription
2. `6.2.2_diary.py` - Diary application with file storage
3. `6.2.3_filtering_contents.py` - Filter file lines
4. `6.2.4_store_personal_data.py` - Store tuple data to file
5. `6.2.5_course_grading_part4.py` - Write results to files
6. `6.2.6_word_search.py` - Word search with wildcards
7. `6.2.7_dictionary_file.py` - Dictionary with file persistence

### Section 6.3: Handling errors (3)
1. `6.3.1_reading_input.py` - Input validation with error handling
2. `6.3.2_parameter_validation.py` - Validate function parameters
3. `6.3.3_incorrect_lottery.py` - Validate lottery numbers

---

## 🚀 Getting Started

```bash
# Clone/Fork the repository
cd pythonpro26

# Start with Part 1
cd part1/part1Exercises/tasks

# Work on exercises...

# Run the grader
python grade_part1.py

# Check your progress
cat ../../.progress/marksheet.md
```

## 📈 Progress Tracking

- Each task is worth **1 point**
- Progress persists across grading sessions
- Cumulative scores tracked across all parts
- Auto-generated progress report with visual progress bars
- Personalized with your username

## 🎓 Learning Path

1. **Part 1-2**: Master basics (variables, conditionals, loops)
2. **Part 3**: Learn functions and string manipulation
3. **Part 4**: Work with lists and iteration
4. **Part 5**: Advanced data structures (dictionaries, tuples)
5. **Part 6**: File I/O and error handling

---

## 📄 License & Attribution

This project is licensed under the **Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License** - see the [LICENSE](LICENSE) file for details.

### Adaptations in This Repository

- ✅ Auto-grading system with persistent progress tracking
- ✅ Academic integrity checks (no implementation detection)
- ✅ 4-scale grading system (Fail/1/2/3)
- ✅ GitHub Codespaces configuration for zero-installation setup
- ✅ Comprehensive setup guides for Windows, macOS, and Ubuntu
- ✅ Repository restructuring and enhanced documentation

### What This License Means:

- ✅ **Free to use** for personal and educational purposes
- ✅ **Free to modify and distribute** with proper attribution
- ❌ **Not for commercial use** without permission
- 🔄 **Share-alike** - derivatives must use the same license
- 📝 **Attribution required** - credit University of Helsinki and this adaptation

For the full legal text, visit: [https://creativecommons.org/licenses/by-nc-sa/4.0/](https://creativecommons.org/licenses/by-nc-sa/4.0/)

---

**Happy Coding! 🐍**

---

## 📘 Documentation site (GitHub Pages)

This project’s website is built with MkDocs (Dracula theme) and deployed via GitHub Actions.

- Branch used for deploy: `mkdocsTesting`
- Trigger: any push to `mkdocsTesting`
- GitHub Pages setting: Source = “GitHub Actions” (Repository → Settings → Pages)

How it works:

1. A GitHub Actions workflow installs MkDocs and the Dracula theme.
2. It builds the site from `docs/` using `mkdocs.yml`.
3. The built site is uploaded as a Pages artifact and deployed by GitHub Pages.

How to publish updates:

1. Commit your documentation changes (files in `docs/` or `mkdocs.yml`) to `mkdocsTesting`.
2. Push to GitHub. The workflow “Deploy MkDocs (Dracula)” will build and deploy.
3. Visit https://dipaish.github.io/pythonpro26/ (hard refresh with Ctrl+F5 if needed).

Notes:

- Ensure Settings → Pages → Source is set to “GitHub Actions.”
- `site/` is ignored by Git (see `.gitignore`) because the site is built in CI.
