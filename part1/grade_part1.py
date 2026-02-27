#!/usr/bin/env python3
"""
Part 1 Grader — awards 1 point per correct task and persists progress.
Usage:
    python part1Exercises/grade_part1.py
    (Windows) python part1Exercises\\grade_part1.py
"""
from __future__ import annotations
import json, os, sys, subprocess, time, re, shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent       # part1 folder
WORKSPACE_ROOT = ROOT.parent                 # repository/workspace root
# Use shared workspace-level progress file for all parts
PROGRESS = WORKSPACE_ROOT / ".progress" / "points.json"
PROGRESS_DIR = PROGRESS.parent
MARKSHEET_DIR = WORKSPACE_ROOT / ".progress"

# For non-interactive tasks: key is filename, value is expected output string
EXPECTED = {
    "1_emoticon.py": ":-)\n",
    "2_seven_brothers.py": "Aapo\nEero\nJuhani\nLauri\nSimeoni\nTimo\nTuomas\n",
    "3_row_your_boat.py": "Row, row, row your boat,\nGently down the stream.\nMerrily, merrily, merrily, merrily,\nLife is but a dream.\n",
    "4_minutes_in_year.py": "Minutes in a year:\n525600\n",
    "5_print_some_code.py": "print(\"Hello there!\")\n",
    "11_extraspace.py": "my name is Tim Tester, I am 20 years old\n\nmy skills are\n - python (beginner)\n - java (veteran)\n - programming (semiprofessional)\n\nI am looking for a job with a salary of 2000-3000 euros per month\n",
    # "12_arithmetics.py" moved to DYNAMIC_CHECKS
    "13_fix_single_line.py": "5 + 8 - 4 = 9\n",
}

# For tasks that need dynamic validation (values can change)
DYNAMIC_CHECKS = {
    "12_arithmetics.py": "arithmetics_check",
    "27_temperatures.py": "temperature_check",
    "29_loyalty_bonus.py": "loyalty_bonus_check",
    "30_what_to_wear_tomorrow.py": "weather_check",
    "31_solving_a_quadratic_equation.py": "quadratic_check"
}

# For interactive tasks: key is filename, value is dict with "inputs" (list) and "expected_output" (string)
INTERACTIVE = {
    "6_name_twice.py": {
        "inputs": ["Paul"],
        "expected_output": "What is your name? Paul\nPaul\n"
    },
    "7_name_excalaimation_mark.py": {
        "inputs": ["Paul"],
        "expected_output": "What is your name? !Paul!Paul!\n"
    },
    "8_name_Address.py": {
        "inputs": ["Steve", "Sanders", "91 Station Road", "London EC05 6AW"],
        "expected_output": "Given name: Family name: Street address: City and postal code: Steve Sanders\n91 Station Road\nLondon EC05 6AW\n"
    },
    "9_fix_the_code.py": {
        "inputs": ["hickory", "dickory", "dock"],
        "expected_output": "The 1st part: The 2nd part: The 3rd part: hickory-dickory-dock!\n"
    },
    "10_story.py": {
        "inputs": ["Mary", "1572"],
        "expected_output": "Please type in a name: Please type in a year: Mary is a valiant knight, born in the year 1572. One morning Mary woke up to an awful racket: a dragon was approaching the village. Only Mary could save the village's residents.\n"
    },
    # Section 1.2 - Arithmetic operations
    "14_times_five.py": {
        "inputs": ["3"],
        "expected_output": "Please type in a number: 3 times 5 is 15\n"
    },
    "15_name_and_age.py": {
        "inputs": ["Frances Fictitious", "1990"],
        "expected_output": "What is your name? Which year were you born? Hi Frances Fictitious, you will be 36 years old at the end of the year 2026\n"
    },
    "16_seconds_in_a_day.py": {
        "inputs": ["1"],
        "expected_output": "How many days? Seconds in that many days: 86400\n"
    },
    "17_fix_the_code_product.py": {
        "inputs": ["2", "4", "5"],
        "expected_output": "Please type in the first number: Please type in the second number: Please type in the third number: The product is 40\n"
    },
    "18_sum_and_product.py": {
        "inputs": ["3", "7"],
        "expected_output": "Number 1: Number 2: The sum of the numbers: 10\nThe product of the numbers: 21\n"
    },
    "19_sum_and_mean.py": {
        "inputs": ["2", "1", "6", "7"],
        "expected_output": "Number 1: Number 2: Number 3: Number 4: The sum of the numbers is 16 and the mean is 4.0\n"
    },
    "20_food_expenditure.py": {
        "inputs": ["4", "2.50", "28.5"],
        "expected_output": "How many times a week do you eat at the student cafeteria? The price of a typical student lunch? How much money do you spend on groceries in a week? \nAverage food expenditure:\nDaily: 5.5 euros\nWeekly: 38.5 euros\n"
    },
    "21_students_in_groups.py": {
        "inputs": ["8", "4"],
        "expected_output": "How many students on the course? Desired group size? Number of groups formed: 2\n"
    },
    # Section 1.3 - Conditional statements
    "22_orwell.py": {
        "inputs": ["1984"],
        "expected_output": "Please type in a number: Orwell\n"
    },
    "23_absolute_value.py": {
        "inputs": ["-7"],
        "expected_output": "Please type in a number: The absolute value of this number is 7\n"
    },
    "24_soup_or_no_soup.py": {
        "inputs": ["Kramer", "2"],
        "expected_output": "Please tell me your name: How many portions of soup? The total cost is 11.8\nNext please!\n"
    },
    "25_order_of_magnitude.py": {
        "inputs": ["2"],
        "expected_output": "Please type in a number: This number is smaller than 1000\nThis number is smaller than 100\nThis number is smaller than 10\nThank you!\n"
    },
    "26_calculator.py": {
        "inputs": ["10", "17", "add"],
        "expected_output": "Number 1: Number 2: Operation: 10 + 17 = 27\n"
    },
    # "27_temperatures.py" moved to DYNAMIC_CHECKS
    "28_daily_wages.py": {
        "inputs": ["8.5", "3", "Monday"],
        "expected_output": "Hourly wage: Hours worked: Day of the week: Daily wages: 25.5 euros\n"
    },
    # "29_loyalty_bonus.py" moved to DYNAMIC_CHECKS
    # "30_what_to_wear_tomorrow.py" moved to DYNAMIC_CHECKS
    # "31_solving_a_quadratic_equation.py" moved to DYNAMIC_CHECKS
}

def load_state():
    if PROGRESS.exists():
        try:
            return json.loads(PROGRESS.read_text(encoding="utf-8"))
        except Exception:
            pass
    return {"parts": {}, "total_points": 0, "updated_at": None}

def save_state(state):
    PROGRESS_DIR.mkdir(parents=True, exist_ok=True)
    state["updated_at"] = time.strftime("%Y-%m-%d %H:%M:%S")
    PROGRESS.write_text(json.dumps(state, indent=2), encoding="utf-8")

def task_sort_key(filename: str) -> tuple:
    """Sort tasks numerically by the number prefix before the underscore."""
    import re
    match = re.match(r'^(\d+)', filename)
    if match:
        return (int(match.group(1)), filename)
    return (999999, filename)

def write_marksheet(state: dict, user: str | None) -> None:
    """Render a marksheet markdown file in workspace-level .progress with per-part details."""
    MARKSHEET_DIR.mkdir(parents=True, exist_ok=True)
    lines = []
    title_name = user if user else "Student"
    lines.append("# Basics of Programming")
    lines.append("")
    lines.append(f"## Hi {title_name}, check your scores below!")
    lines.append("")
    lines.append(f"Last updated: {state.get('updated_at','')}")
    lines.append("")
    # Table header
    lines.append("| Part | Score | Max | Percent | Progress |")
    lines.append("|------|-------|-----|---------|----------|")
    parts = state.get("parts", {})
    # Sort parts numerically when possible
    def part_sort_key(k: str):
        try:
            return (0, int(k))
        except Exception:
            return (1, str(k))
    for part_key in sorted(parts.keys(), key=part_sort_key):
        p = parts[part_key]
        score = int(p.get("score", 0))
        total = int(p.get("total", 0))
        percent = int(round((score / total) * 100)) if total else 0
        # simple 10-char bar
        filled = int(round((score / total) * 10)) if total else 0
        bar = "█" * filled + "░" * (10 - filled)
        lines.append(f"| Part {part_key} | {score} | {total} | {percent}% | {bar} |")
    lines.append("")
    # Calculate max points excluding Part 5 (Parts 1-4, 6: 31+22+34+37+19 = 143)
    max_points = sum(p.get("total", 0) for k, p in parts.items() if k != "5")
    current_points = int(state.get('total_points', 0))
    lines.append(f"**Total points:** {current_points}/{max_points}")
    
    # Calculate grade on 4-point scale
    percentage = (current_points / max_points * 100) if max_points > 0 else 0
    if percentage < 50:
        grade = "Fail"
    elif percentage < 65:
        grade = "1"
    elif percentage < 85:
        grade = "2"
    else:
        grade = "3"
    lines.append(f"**Grade:** {grade} ({percentage:.1f}%)")
    lines.append("")
    lines.append("_Note: Part 5 is optional and not counted toward the total._")
    lines.append("")
    # Detailed per-part task summary
    if parts:
        lines.append("## Details by Part")
        for part_key in sorted(parts.keys(), key=part_sort_key):
            p = parts[part_key]
            tasks = p.get("tasks", {}) or {}
            passed = [t for t, ok in tasks.items() if ok]
            failed = [t for t, ok in tasks.items() if not ok]
            lines.append("")
            lines.append(f"### Part {part_key}")
            lines.append(f"- Tasks passed: {len(passed)}")
            lines.append(f"- Tasks failed: {len(failed)}")
            if failed:
                lines.append("- Failed task files:")
                for f in sorted(failed, key=task_sort_key):
                    lines.append(f"  - `{f}`")
    lines.append("")
    lines.append("> This file is auto-generated by the grader whenever it runs.")

    (MARKSHEET_DIR / "marksheet.md").write_text("\n".join(lines), encoding="utf-8")

def _run_capture(args: list[str], cwd: Path | None = None, timeout: int = 5) -> tuple[int, str]:
    """Run a command and return (returncode, stdout). Never raises; returns (1, "") on failure."""
    try:
        proc = subprocess.run(args, cwd=str(cwd) if cwd else None, text=True, capture_output=True, timeout=timeout)
        return proc.returncode, proc.stdout.strip()
    except Exception:
        return 1, ""

def get_display_user() -> str | None:
    """Best-effort GitHub/VS Code identity for display.

    Priority:
    1) Env vars: GITHUB_USER/GITHUB_USERNAME/GH_USER
    2) GitHub CLI (gh): gh api user --jq .login
    3) Git user.name
    4) Owner parsed from git remote origin URL
    5) OS username (USERNAME/USER)
    """
    # 1) Environment variables
    for key in ("GITHUB_USER", "GITHUB_USERNAME", "GH_USER"):
        v = os.environ.get(key)
        if v:
            return v.strip()

    # 2) GitHub CLI
    if shutil.which("gh"):
        rc, out = _run_capture(["gh", "api", "user", "--jq", ".login"])  # requires gh auth login
        if rc == 0 and out:
            return out

    # 3) git user.name
    rc, out = _run_capture(["git", "-C", str(WORKSPACE_ROOT), "config", "--get", "user.name"])
    if rc == 0 and out:
        return out

    # 4) parse owner from origin URL
    rc, url = _run_capture(["git", "-C", str(WORKSPACE_ROOT), "config", "--get", "remote.origin.url"])
    if rc == 0 and url:
        # Examples: https://github.com/owner/repo.git or git@github.com:owner/repo.git
        m = re.search(r"github\.com[/:]([^/\s]+)/", url, re.IGNORECASE)
        if m:
            return m.group(1)

    # 5) OS username
    for key in ("USERNAME", "USER"):
        v = os.environ.get(key)
        if v:
            return v
    return None

def has_implementation(pyfile: Path) -> bool:
    """
    Check if a task file contains actual implementation code.
    Returns False if the file only contains TODO comments, docstrings, or is empty.
    This prevents students from getting credit for deleted/empty solutions.
    """
    if not pyfile.exists():
        return False
    
    try:
        content = pyfile.read_text(encoding="utf-8")
        # Remove docstrings and comments
        lines = content.split('\n')
        code_lines = []
        in_docstring = False
        docstring_char = None
        
        for line in lines:
            stripped = line.strip()
            
            # Track docstring boundaries
            if '"""' in stripped or "'''" in stripped:
                if not in_docstring:
                    # Starting docstring
                    docstring_char = '"""' if '"""' in stripped else "'''"
                    in_docstring = True
                    # Check if docstring closes on same line
                    if stripped.count(docstring_char) >= 2:
                        in_docstring = False
                    continue
                else:
                    # Ending docstring
                    in_docstring = False
                    continue
            
            # Skip lines inside docstrings
            if in_docstring:
                continue
            
            # Skip comments and empty lines
            if not stripped or stripped.startswith('#'):
                continue
            
            # Skip TODO comments
            if 'TODO' in stripped.upper() and '#' in stripped:
                continue
            
            # This is actual code
            code_lines.append(stripped)
        
        # File must have at least one line of actual code (not just imports/pass)
        substantive_code = [line for line in code_lines 
                          if line and line != 'pass' and not line.startswith('import ') and not line.startswith('from ')]
        
        return len(substantive_code) > 0
    except Exception:
        return False

def run_task(pyfile: Path, input_data: str = ""):
    """Run a Python task file, optionally providing input via stdin."""
    try:
        proc = subprocess.run(
            [sys.executable, str(pyfile)],
            cwd=str(pyfile.parent),
            text=True,
            input=input_data,
            capture_output=True,
            timeout=5
        )
        return proc.returncode, proc.stdout, proc.stderr
    except subprocess.TimeoutExpired:
        return 124, "", "Timed out (5s)"
    except Exception as e:
        return 1, "", str(e)

def arithmetics_check(path: Path, output: str) -> bool:
    """
    Validate 12_arithmetics.py - checks that the output correctly performs
    arithmetic operations with whatever x and y values are in the code.
    """
    try:
        # Read the code to extract x and y values
        content = path.read_text(encoding="utf-8")
        
        # Remove docstring to avoid matching values in the examples
        # Find the end of the docstring (first """ or ''' that appears after the opening one)
        lines = content.split('\n')
        code_lines = []
        in_docstring = False
        docstring_marker = None
        
        for line in lines:
            # Check for docstring start/end
            if '"""' in line or "'''" in line:
                marker = '"""' if '"""' in line else "'''"
                if not in_docstring:
                    in_docstring = True
                    docstring_marker = marker
                    # Check if docstring closes on same line
                    if line.count(marker) >= 2:
                        in_docstring = False
                elif marker == docstring_marker:
                    in_docstring = False
                    continue
            
            # Only keep lines outside docstrings
            if not in_docstring and not ('"""' in line or "'''" in line):
                code_lines.append(line)
        
        # Join code lines and extract x and y from actual code (not docstring)
        code_only = '\n'.join(code_lines)
        
        # Extract x and y values using regex from code only
        x_match = re.search(r'^\s*x\s*=\s*(-?\d+)', code_only, re.MULTILINE)
        y_match = re.search(r'^\s*y\s*=\s*(-?\d+)', code_only, re.MULTILINE)
        
        if not x_match or not y_match:
            return False
            
        x = int(x_match.group(1))
        y = int(y_match.group(1))
        
        # Calculate expected results
        add_result = x + y
        sub_result = x - y
        mul_result = x * y
        div_result = x / y
        
        # Build expected output
        expected = f"{x} + {y} = {add_result}\n"
        expected += f"{x} - {y} = {sub_result}\n"
        expected += f"{x} * {y} = {mul_result}\n"
        expected += f"{x} / {y} = {div_result}\n"
        
        return output == expected
    except Exception:
        return False

def temperature_check(path: Path, output: str) -> bool:
    """
    Validate 27_temperatures.py - checks that temperature conversion works
    correctly regardless of whether the input is displayed as int or float.
    Test input: 21
    Expected: converts to -6.111111111111111 Celsius and shows "cold" message
    """
    try:
        # Expected Celsius calculation for input 21
        fahrenheit = 21
        celsius = (fahrenheit - 32) * 5 / 9  # = -6.111111111111111
        
        # Check for required elements in output (flexible about 21 vs 21.0)
        lines = output.strip().split('\n')
        
        if len(lines) != 2:
            return False
        
        # First line should have prompt + conversion output
        # Accept both "21 degrees" or "21.0 degrees"
        line1_patterns = [
            f"Please type in a temperature (F): 21 degrees Fahrenheit equals {celsius} degrees Celsius",
            f"Please type in a temperature (F): 21.0 degrees Fahrenheit equals {celsius} degrees Celsius"
        ]
        
        line1_match = any(pattern in lines[0] for pattern in line1_patterns)
        
        # Second line should be the cold message
        line2_match = lines[1] == "Brr! It's cold in here!"
        
        return line1_match and line2_match
    except Exception:
        return False

def loyalty_bonus_check(path: Path, output: str) -> bool:
    """
    Validate 29_loyalty_bonus.py - checks loyalty bonus calculation.
    Test input: 95
    Expected: Should show ONLY ONE bonus (not both 10% and 15%)
    This test catches the common bug of using two separate if statements.
    """
    try:
        import re
        lines = output.strip().split('\n')
        
        # Check that only ONE bonus message appears (not both)
        bonus_10_count = output.count("Your bonus is 10 %")
        bonus_15_count = output.count("Your bonus is 15 %")
        
        # Must have exactly one bonus message total
        if (bonus_10_count + bonus_15_count) != 1:
            return False
        
        # For input 95, should have 10% bonus (95 < 100)
        if bonus_10_count != 1:
            return False
        
        # Should be 2 lines: prompt+bonus message, then points result
        if len(lines) != 2:
            return False
        
        # Line 1: Check prompt and bonus message
        if "How many points are on your card?" not in lines[0]:
            return False
        if "Your bonus is 10 %" not in lines[0]:
            return False
        
        # Line 2: Check final points (handle floating point precision)
        # 95 * 1.1 = 104.5
        match = re.search(r'You now have ([\d.]+) points', lines[1])
        if not match:
            return False
        
        actual_points = float(match.group(1))
        expected_points = 104.5
        
        # Allow small floating point error (within 0.01)
        return abs(actual_points - expected_points) < 0.01
    except Exception:
        return False

def weather_check(path: Path, output: str) -> bool:
    """
    Validate 30_what_to_wear_tomorrow.py - tests all temperature ranges and rain condition.
    Tests multiple scenarios to ensure proper conditional logic.
    """
    try:
        # Test 1: Temperature > 20, no rain - should only show basic message
        code1, out1, err1 = run_task(path, "21\nno\n")
        if code1 != 0:
            return False
        expected1 = "What is the weather forecast for tomorrow?\nTemperature: Will it rain (yes/no): Wear jeans and a T-shirt\n"
        if out1 != expected1:
            return False
        
        # Test 2: Temperature 11 (10 < temp <= 20), no rain - basic + jumper
        code2, out2, err2 = run_task(path, "11\nno\n")
        if code2 != 0:
            return False
        expected2 = "What is the weather forecast for tomorrow?\nTemperature: Will it rain (yes/no): Wear jeans and a T-shirt\nI recommend a jumper as well\n"
        if out2 != expected2:
            return False
        
        # Test 3: Temperature 7 (5 < temp <= 10), no rain - basic + jumper + jacket
        code3, out3, err3 = run_task(path, "7\nno\n")
        if code3 != 0:
            return False
        expected3 = "What is the weather forecast for tomorrow?\nTemperature: Will it rain (yes/no): Wear jeans and a T-shirt\nI recommend a jumper as well\nTake a jacket with you\n"
        if out3 != expected3:
            return False
        
        # Test 4: Temperature 3 (temp <= 5), with rain - all messages
        code4, out4, err4 = run_task(path, "3\nyes\n")
        if code4 != 0:
            return False
        expected4 = "What is the weather forecast for tomorrow?\nTemperature: Will it rain (yes/no): Wear jeans and a T-shirt\nI recommend a jumper as well\nTake a jacket with you\nMake it a warm coat, actually\nI think gloves are in order\nDon't forget your umbrella!\n"
        if out4 != expected4:
            return False
        
        return True
    except Exception:
        return False

def quadratic_check(path: Path, output: str) -> bool:
    """
    Validate 31_solving_a_quadratic_equation.py - tests multiple scenarios.
    Tests: two distinct roots, equal roots, and verifies formula correctness.
    """
    try:
        import math
        
        # Test 1: Two distinct real roots (a=1, b=2, c=-8)
        # Expected roots: 2.0 and -4.0
        code1, out1, err1 = run_task(path, "1\n2\n-8\n")
        if code1 != 0:
            return False
        
        # Check prompts and either root order
        if "Value of a:" not in out1 or "Value of b:" not in out1 or "Value of c:" not in out1:
            return False
        if "The roots are" not in out1:
            return False
        
        # Extract roots from output (handle either order)
        import re
        match = re.search(r'The roots are ([\-\d.]+) and ([\-\d.]+)', out1)
        if not match:
            return False
        
        root1_out = float(match.group(1))
        root2_out = float(match.group(2))
        expected_roots = {2.0, -4.0}
        actual_roots = {root1_out, root2_out}
        
        # Check if roots match (with small tolerance)
        if not all(any(abs(actual - expected) < 0.01 for expected in expected_roots) for actual in actual_roots):
            return False
        
        # Test 2: Equal roots (a=1, b=-4, c=4)
        # Expected: discriminant = 16 - 16 = 0, roots = 2.0 and 2.0
        code2, out2, err2 = run_task(path, "1\n-4\n4\n")
        if code2 != 0:
            return False
        
        match2 = re.search(r'The roots are ([\-\d.]+) and ([\-\d.]+)', out2)
        if not match2:
            return False
        
        root1_out2 = float(match2.group(1))
        root2_out2 = float(match2.group(2))
        
        # Both roots should be 2.0
        if not (abs(root1_out2 - 2.0) < 0.01 and abs(root2_out2 - 2.0) < 0.01):
            return False
        
        # Test 3: Different coefficients (a=2, b=5, c=-3)
        # Expected roots: 0.5 and -3.0
        code3, out3, err3 = run_task(path, "2\n5\n-3\n")
        if code3 != 0:
            return False
        
        match3 = re.search(r'The roots are ([\-\d.]+) and ([\-\d.]+)', out3)
        if not match3:
            return False
        
        root1_out3 = float(match3.group(1))
        root2_out3 = float(match3.group(2))
        expected_roots3 = {0.5, -3.0}
        actual_roots3 = {root1_out3, root2_out3}
        
        if not all(any(abs(actual - expected) < 0.01 for expected in expected_roots3) for actual in actual_roots3):
            return False
        
        return True
    except Exception:
        return False


def extract_task_number(filename: str) -> int:
    """Extract the task number from a filename like '12_arithmetics.py' -> 12"""
    try:
        return int(filename.split('_')[0])
    except (ValueError, IndexError):
        return 999  # Put files without numbers at the end

def grade_part1():
    state = load_state()
    prev = state.get("parts", {}).get("1", {}).get("tasks", {})
    results = {}
    part_score = 0
    
    # Combine all tasks
    all_tasks = list(EXPECTED.keys()) + list(DYNAMIC_CHECKS.keys()) + list(INTERACTIVE.keys())
    total_tasks = len(all_tasks)
    
    # Store detailed results for sorted output
    task_details = {}

    print("Grading Part 1 — Getting Started")
    print("-" * 40)

    # Grade non-interactive tasks
    for fname, expected in EXPECTED.items():
        path = ROOT / fname
        
        # Check if file has actual implementation
        if not has_implementation(path):
            results[fname] = False
            task_details[fname] = {
                "status": "FAIL",
                "message": "(no implementation)",
                "passed": False
            }
            continue
        
        code, out, err = run_task(path)
        passed_now = (out == expected)
        passed = (code == 0 and passed_now)

        results[fname] = bool(passed)
        status = "PASS" if passed else "FAIL"
        if passed:
            part_score += 1
            task_details[fname] = {"status": status, "passed": True}
        else:
            exp = expected.replace("\n", "\\n")
            got = (out or "").replace("\n", "\\n")
            message = f"  expected: {exp}\n  got     : {got}"
            if err:
                message += f"\n  stderr  : {err.strip()}"
            task_details[fname] = {
                "status": status,
                "message": message,
                "passed": False
            }

    # Grade dynamic check tasks (e.g., tasks where values can change)
    for fname, check_func_name in DYNAMIC_CHECKS.items():
        path = ROOT / fname
        
        # Check if file has actual implementation
        if not has_implementation(path):
            results[fname] = False
            task_details[fname] = {
                "status": "FAIL",
                "message": "(no implementation)",
                "passed": False
            }
            continue
        
        # Call the appropriate check function
        if check_func_name == "arithmetics_check":
            code, out, err = run_task(path)
            passed_now = arithmetics_check(path, out)
        elif check_func_name == "temperature_check":
            # Pass input "21" to the temperature task
            code, out, err = run_task(path, "21\n")
            passed_now = temperature_check(path, out)
        elif check_func_name == "loyalty_bonus_check":
            # Pass input "95" to the loyalty bonus task
            # This catches the bug where both bonuses are applied
            code, out, err = run_task(path, "95\n")
            passed_now = loyalty_bonus_check(path, out)
        elif check_func_name == "weather_check":
            # Weather check runs multiple test cases internally
            code = 0  # Will be set by the check function
            passed_now = weather_check(path, "")
        elif check_func_name == "quadratic_check":
            # Quadratic check runs multiple test cases internally
            code = 0  # Will be set by the check function
            passed_now = quadratic_check(path, "")
        else:
            code, out, err = run_task(path)
            passed_now = False
        
        passed = (code == 0 and passed_now)

        results[fname] = bool(passed)
        status = "PASS" if passed else "FAIL"
        if passed:
            part_score += 1
            task_details[fname] = {"status": status, "passed": True}
        else:
            message = ""
            if err:
                message = f"  stderr  : {err.strip()}"
            else:
                message = "  Output format or calculations incorrect"
            task_details[fname] = {
                "status": status,
                "message": message,
                "passed": False
            }

    # Grade interactive tasks
    for fname, test_spec in INTERACTIVE.items():
        path = ROOT / fname
        
        # Check if file has actual implementation
        if not has_implementation(path):
            results[fname] = False
            task_details[fname] = {
                "status": "FAIL",
                "message": "(no implementation)",
                "passed": False
            }
            continue
        
        # Prepare input: join with newlines
        input_str = "\n".join(test_spec["inputs"]) + "\n"
        expected = test_spec["expected_output"]

        code, out, err = run_task(path, input_str)
        passed_now = (out == expected)
        passed = (code == 0 and passed_now)

        results[fname] = bool(passed)
        status = "PASS" if passed else "FAIL"
        if passed:
            part_score += 1
            task_details[fname] = {"status": status, "passed": True}
        else:
            exp = expected.replace("\n", "\\n")
            got = (out or "").replace("\n", "\\n")
            message = f"  expected: {exp}\n  got     : {got}"
            if err:
                message += f"\n  stderr  : {err.strip()}"
            task_details[fname] = {
                "status": status,
                "message": message,
                "passed": False
            }
    
    # Print results sorted by task number in table format
    sorted_tasks = sorted(task_details.keys(), key=extract_task_number)
    
    # Count pass/fail
    passed_count = sum(1 for t in task_details.values() if t['passed'])
    failed_count = total_tasks - passed_count
    
    # Print summary
    print(f"Summary: {passed_count} passed, {failed_count} failed out of {total_tasks} tasks")
    print()
    
    # Print table header
    print("+" + "-" * 6 + "+" + "-" * 46 + "+" + "-" * 12 + "+")
    print(f"| {'Task':<4} | {'Description':<44} | {'Status':<10} |")
    print("+" + "=" * 6 + "+" + "=" * 46 + "+" + "=" * 12 + "+")
    
    # Print each task
    for fname in sorted_tasks:
        detail = task_details[fname]
        task_num = extract_task_number(fname)
        task_name = fname.replace('.py', '').replace('_', ' ')[fname.index('_')+1:] if '_' in fname else fname
        # Truncate long names
        if len(task_name) > 43:
            task_name = task_name[:40] + "..."
        
        # Status with symbol
        status_symbol = "[PASS]" if detail['passed'] else "[FAIL]"
        
        print(f"| {task_num:>4} | {task_name:<44} | {status_symbol:<10} |")
        print("+" + "-" * 6 + "+" + "-" * 46 + "+" + "-" * 12 + "+")
        
        # Print error details if failed (brief version)
        if not detail['passed'] and 'message' in detail:
            message = detail['message'].strip()
            # For long error messages, just show they failed and need to check
            if len(message) > 200:
                print(f"|      See output mismatch - check expected vs actual output   |")
                print("+" + "-" * 6 + "+" + "-" * 46 + "+" + "-" * 12 + "+")
            else:
                # Show short error messages
                message_lines = message.split('\n')
                for line in message_lines:
                    if len(line) <= 57:
                        print(f"|      {line:<57} |")
                    else:
                        # Simple truncation for long lines
                        print(f"|      {line[:54]:<54}... |")
                print("+" + "-" * 6 + "+" + "-" * 46 + "+" + "-" * 12 + "+")

    state.setdefault("parts", {})
    state["parts"]["1"] = {"tasks": results, "score": part_score, "total": total_tasks}
    # Exclude Part 5 from total points aggregation
    state["total_points"] = sum(p.get("score", 0) for k, p in state["parts"].items() if k != "5")
    save_state(state)
    # Write marksheet markdown
    write_marksheet(state, get_display_user())

    print("-" * 40)
    user = get_display_user()
    if user:
        print(f"{user}: your Part 1 score is {part_score}/{total_tasks}")
        print(f"{user}: your total score is {state['total_points']}")
    else:
        print(f"Part 1 score: {part_score}/{total_tasks}")
        print(f"Cumulative score: {state['total_points']}")
    print(f"(Saved to {PROGRESS})")

if __name__ == "__main__":
    grade_part1()
