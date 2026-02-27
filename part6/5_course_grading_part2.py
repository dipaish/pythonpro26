"""
Quick Start: Click Terminal > New Terminal | pwd (check location) | cd part6 (if needed)

Course grading, part 2

Let's expand the program created in the previous exercise. Now also the exam points 
awarded to each student are contained in a CSV file. The contents of the file follow 
this format:

id;e1;e2;e3
12345678;4;1;4
12345687;3;5;3
12345699;10;2;2

In the above example the student whose student number is 12345678 was awarded 4+1+4 
points in the exam, which equals a total of 9 points.

The program should again ask the user for the names of the files. Then the program 
should process the files and print out a grade for each student.

Sample output:
Student information: students1.csv
Exercises completed: exercises1.csv
Exam points: exam_points1.csv
pekka peloton 0
jaana javanainen 1
liisa virtanen 3

Note: The implementation should calculate and display the final grade (0-5) for each student 
based on the grading table below. With the provided test files (students.csv, exercises.csv, 
exam.csv), the actual output format is:

Peter Python 21 34 55
Jean Java 27 50 77

Each completed exercise is counted towards exercise points, so that completing at least 
10% of the total exercises awards 1 point, completing at least 20% awards 2 points, etc. 
Completing all 40 exercises awards 10 points. The number of points awarded is always an 
integer number.

The final grade for the course is determined based on the sum of exam and exercise points 
according to the following table:

exam + exercise points -> grade
0-14 -> 0 (fail)
15-17 -> 1
18-20 -> 2
21-23 -> 3
24-27 -> 4
28- -> 5

NB: this exercise doesn't ask you to write any functions, so you should not place any 
code within an if __name__ == "__main__" block.
"""

# TODO: Implement your solution below
if False:
    student_info = input("Student information: ")
    exercise_data = input("Exercises completed: ")
    exam_data = input("Exam points: ")
else:
    student_info = "students.csv"
    exercise_data = "exercises.csv"
    exam_data = "exam.csv"

# Read student information, exercise data, and exam points
# Print each student's name, exercise points, exam points, and total



# Save your file and run it using: python 5_course_grading_part2.py
# Check: python grade_part6.py

# Commit and push changes to GitHub:
# 1. git add .                                    (stage all changes)
# 2. git commit -m "Completed task 5"         (commit with message)
# 3. git push                                      (push to GitHub)
