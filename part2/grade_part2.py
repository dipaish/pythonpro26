#!/usr/bin/env python3
"""
Part 2 Grader — awards 1 point per correct task and persists progress.
Usage:
    python part2Exercises/grade_part2.py
    (Windows) python part2Exercises\\grade_part2.py
"""
from __future__ import annotations
import json, os, sys, subprocess, time, re, shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent       # part2 folder
WORKSPACE_ROOT = ROOT.parent                 # repository/workspace root
# Use shared workspace-level progress file for all parts
PROGRESS = WORKSPACE_ROOT / ".progress" / "points.json"
PROGRESS_DIR = PROGRESS.parent
MARKSHEET_DIR = WORKSPACE_ROOT / ".progress"

# For non-interactive tasks: key is filename, value is expected output string
EXPECTED = {
    # Section 2.4.7 - Story (non-interactive once inputs provided)
}

# For tasks that need dynamic validation (values can change or multiple test cases needed)
DYNAMIC_CHECKS = {
    "2_number_of_characters.py": "number_of_characters_check",
    "3_typecasting.py": "typecasting_check",
    "4_age_of_maturity.py": "age_of_maturity_check",
    "5_greater_than_or_equal_to.py": "greater_than_or_equal_check",
    "6_the_elder.py": "elder_check",
    "7_alphabetically_last.py": "alphabetically_last_check",
    "8_age_check.py": "age_check_check",
    "9_nephews.py": "nephews_check",
    "10_grades_and_points.py": "grades_and_points_check",
    "11_fizzbuzz.py": "fizzbuzz_check",
    "12_leap_year.py": "leap_year_check",
    "13_alphabetically_in_the_middle.py": "alphabetically_in_middle_check",
    "14_gift_tax_calculator.py": "gift_tax_calculator_check",
    "19_pin_and_number_of_attempts.py": "pin_attempts_check",
    "20_the_next_leap_year.py": "next_leap_year_check",
    "21_story.py": "story_check"
}

# For interactive tasks: key is filename, value is dict with "inputs" (list) and "expected_output" (string)
INTERACTIVE = {
    # Section 2.1 - Programming terminology
    "1_fix_syntax.py": {
        "inputs": ["150"],
        "expected_output": "Please type in a number: The number was greater than one hundred\nNow its value has decreased by one hundred\nIts value is now 50\n50 must be my lucky number!\nHave a nice day!\n"
    },
    # "2_number_of_characters.py" moved to DYNAMIC_CHECKS
    # "3_typecasting.py" moved to DYNAMIC_CHECKS
    
    # Section 2.2 - More conditionals
    # "4_age_of_maturity.py" moved to DYNAMIC_CHECKS
    # "5_greater_than_or_equal_to.py" moved to DYNAMIC_CHECKS
    # "6_the_elder.py" moved to DYNAMIC_CHECKS
    # "7_alphabetically_last.py" moved to DYNAMIC_CHECKS,
    
    # Section 2.3 - Combining conditions
    # "8_age_check.py" moved to DYNAMIC_CHECKS
    # "9_nephews.py" moved to DYNAMIC_CHECKS
    # "10_grades_and_points.py" moved to DYNAMIC_CHECKS
    # "11_fizzbuzz.py" moved to DYNAMIC_CHECKS
    # "12_leap_year.py" moved to DYNAMIC_CHECKS
    # "13_alphabetically_in_the_middle.py" moved to DYNAMIC_CHECKS
    # "14_gift_tax_calculator.py" moved to DYNAMIC_CHECKS
    
    # Section 2.4 - Simple loops
    "15_shall_we_continue.py": {
        "inputs": ["yes", "oui", "no"],
        "expected_output": "hi\nShall we continue? hi\nShall we continue? hi\nShall we continue? okay then\n"
    },
    "16_input_validation.py": {
        "inputs": ["16", "4", "-3", "1", "0"],
        "expected_output": "Please type in a number: 4.0\nPlease type in a number: 2.0\nPlease type in a number: Invalid number\nPlease type in a number: 1.0\nPlease type in a number: Exiting...\n"
    },
    "17_fix_the_code_countdown.py": {
        "inputs": [],
        "expected_output": "Countdown!\n5\n4\n3\n2\n1\nNow!\n"
    },
    "18_repeat_password.py": {
        "inputs": ["sekred", "secret", "cantremember", "sekred"],
        "expected_output": "Password: Repeat password: They do not match!\nRepeat password: They do not match!\nRepeat password: User account created!\n"
    },
    # "19_pin_and_number_of_attempts.py" moved to DYNAMIC_CHECKS
    # "20_the_next_leap_year.py" moved to DYNAMIC_CHECKS
    # "21_story.py" moved to DYNAMIC_CHECKS
    "22_working_with_numbers.py": {
        "inputs": ["5", "22", "9", "-2", "0"],
        "expected_output": "Please type in integer numbers. Type in 0 to finish.\nNumber: Number: Number: Number: Number: Numbers typed in 4\nThe sum of the numbers is 34\nThe mean of the numbers is 8.5\nPositive numbers 3\nNegative numbers 1\n"
    },
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

def number_of_characters_check(path: Path, output: str) -> bool:
    """
    Validate 2_number_of_characters.py - tests both scenarios:
    1. Single character input (should only print "Thank you!")
    2. Multiple character input (should print count + "Thank you!")
    """
    try:
        # Test case 1: Single character
        code1, out1, err1 = run_task(path, "b\n")
        expected1 = "Please type in a word: Thank you!\n"
        test1_pass = (code1 == 0 and out1 == expected1)
        
        # Test case 2: Multiple characters
        code2, out2, err2 = run_task(path, "python\n")
        expected2 = "Please type in a word: There are 6 letters in the word python\nThank you!\n"
        test2_pass = (code2 == 0 and out2 == expected2)
        
        # Test case 3: Another multi-character word
        code3, out3, err3 = run_task(path, "banana\n")
        expected3 = "Please type in a word: There are 6 letters in the word banana\nThank you!\n"
        test3_pass = (code3 == 0 and out3 == expected3)
        
        return test1_pass and test2_pass and test3_pass
    except Exception:
        return False

def typecasting_check(path: Path, output: str) -> bool:
    """
    Validate 3_typecasting.py - tests typecasting with floating-point tolerance.
    The decimal part calculation can have floating-point precision issues,
    so we check the logic is correct rather than exact string matching.
    """
    try:
        import re
        
        # Test case 1: 1.34
        code1, out1, err1 = run_task(path, "1.34\n")
        if code1 != 0:
            return False
        
        # Parse output for integer and decimal parts
        int_match = re.search(r'Integer part:\s*(\d+)', out1)
        dec_match = re.search(r'Decimal part:\s*([\d.]+)', out1)
        
        if not int_match or not dec_match:
            return False
        
        int_part = int(int_match.group(1))
        dec_part = float(dec_match.group(1))
        
        # Check integer part is correct (should be 1)
        # Check decimal part is close to 0.34 (within 0.001 tolerance for floating-point)
        test1_pass = (int_part == 1 and abs(dec_part - 0.34) < 0.001)
        
        # Test case 2: 2.99
        code2, out2, err2 = run_task(path, "2.99\n")
        if code2 != 0:
            return False
        
        int_match2 = re.search(r'Integer part:\s*(\d+)', out2)
        dec_match2 = re.search(r'Decimal part:\s*([\d.]+)', out2)
        
        if not int_match2 or not dec_match2:
            return False
        
        int_part2 = int(int_match2.group(1))
        dec_part2 = float(dec_match2.group(1))
        
        test2_pass = (int_part2 == 2 and abs(dec_part2 - 0.99) < 0.001)
        
        # Test case 3: 5.5
        code3, out3, err3 = run_task(path, "5.5\n")
        if code3 != 0:
            return False
        
        int_match3 = re.search(r'Integer part:\s*(\d+)', out3)
        dec_match3 = re.search(r'Decimal part:\s*([\d.]+)', out3)
        
        if not int_match3 or not dec_match3:
            return False
        
        int_part3 = int(int_match3.group(1))
        dec_part3 = float(dec_match3.group(1))
        
        test3_pass = (int_part3 == 5 and abs(dec_part3 - 0.5) < 0.001)
        
        return test1_pass and test2_pass and test3_pass
    except Exception:
        return False

def age_of_maturity_check(path: Path, output: str) -> bool:
    """
    Validate 4_age_of_maturity.py - tests both scenarios:
    1. Age >= 18 (of age)
    2. Age < 18 (not of age)
    """
    try:
        # Test case 1: Age 32 (of age)
        code1, out1, err1 = run_task(path, "32\n")
        expected1 = "How old are you? You are of age!\n"
        test1_pass = (code1 == 0 and out1 == expected1)
        
        # Test case 2: Age 12 (not of age)
        code2, out2, err2 = run_task(path, "12\n")
        expected2 = "How old are you? You are not of age!\n"
        test2_pass = (code2 == 0 and out2 == expected2)
        
        # Test case 3: Edge case - exactly 18 (should be of age)
        code3, out3, err3 = run_task(path, "18\n")
        expected3 = "How old are you? You are of age!\n"
        test3_pass = (code3 == 0 and out3 == expected3)
        
        return test1_pass and test2_pass and test3_pass
    except Exception:
        return False

def greater_than_or_equal_check(path: Path, output: str) -> bool:
    """
    Validate 5_greater_than_or_equal_to.py - tests all 3 scenarios:
    1. First number greater
    2. Second number greater
    3. Numbers equal
    """
    try:
        # Test case 1: First greater (5 > 3)
        code1, out1, err1 = run_task(path, "5\n3\n")
        expected1 = "Please type in the first number: Please type in another number: The greater number was: 5\n"
        test1_pass = (code1 == 0 and out1 == expected1)
        
        # Test case 2: Second greater (5 < 8)
        code2, out2, err2 = run_task(path, "5\n8\n")
        expected2 = "Please type in the first number: Please type in another number: The greater number was: 8\n"
        test2_pass = (code2 == 0 and out2 == expected2)
        
        # Test case 3: Equal (5 == 5)
        code3, out3, err3 = run_task(path, "5\n5\n")
        expected3 = "Please type in the first number: Please type in another number: The numbers are equal!\n"
        test3_pass = (code3 == 0 and out3 == expected3)
        
        return test1_pass and test2_pass and test3_pass
    except Exception:
        return False

def elder_check(path: Path, output: str) -> bool:
    """
    Validate 6_the_elder.py - tests both scenarios:
    1. Different ages - prints elder's name
    2. Same age - prints both names
    """
    try:
        # Test case 1: Different ages (Ada elder)
        code1, out1, err1 = run_task(path, "Alan\n26\nAda\n27\n")
        expected1 = "Person 1:\nName: Age: Person 2:\nName: Age: The elder is Ada\n"
        test1_pass = (code1 == 0 and out1 == expected1)
        
        # Test case 2: Same age
        code2, out2, err2 = run_task(path, "Bill\n1\nJean\n1\n")
        expected2 = "Person 1:\nName: Age: Person 2:\nName: Age: Bill and Jean are the same age\n"
        test2_pass = (code2 == 0 and out2 == expected2)
        
        return test1_pass and test2_pass
    except Exception:
        return False

def alphabetically_last_check(path: Path, output: str) -> bool:
    """
    Validate 7_alphabetically_last.py - tests all 3 scenarios:
    1. Second word alphabetically last
    2. First word alphabetically last
    3. Same word twice
    """
    try:
        # Test case 1: Second word last (scooter > car)
        code1, out1, err1 = run_task(path, "car\nscooter\n")
        expected1 = "Please type in the 1st word: Please type in the 2nd word: scooter comes alphabetically last.\n"
        test1_pass = (code1 == 0 and out1 == expected1)
        
        # Test case 2: First word last (zorro > batman)
        code2, out2, err2 = run_task(path, "zorro\nbatman\n")
        expected2 = "Please type in the 1st word: Please type in the 2nd word: zorro comes alphabetically last.\n"
        test2_pass = (code2 == 0 and out2 == expected2)
        
        # Test case 3: Same word
        code3, out3, err3 = run_task(path, "python\npython\n")
        expected3 = "Please type in the 1st word: Please type in the 2nd word: You gave the same word twice.\n"
        test3_pass = (code3 == 0 and out3 == expected3)
        
        return test1_pass and test2_pass and test3_pass
    except Exception:
        return False

def age_check_check(path: Path, output: str) -> bool:
    """
    Validate 8_age_check.py - tests all 3 scenarios:
    1. Normal age (5+)
    2. Under 5
    3. Negative age
    """
    try:
        # Test case 1: Normal age
        code1, out1, err1 = run_task(path, "13\n")
        expected1 = "What is your age? Ok, you're 13 years old\n"
        test1_pass = (code1 == 0 and out1 == expected1)
        
        # Test case 2: Under 5
        code2, out2, err2 = run_task(path, "2\n")
        expected2 = "What is your age? I suspect you can't write quite yet...\n"
        test2_pass = (code2 == 0 and out2 == expected2)
        
        # Test case 3: Negative
        code3, out3, err3 = run_task(path, "-4\n")
        expected3 = "What is your age? That must be a mistake\n"
        test3_pass = (code3 == 0 and out3 == expected3)
        
        return test1_pass and test2_pass and test3_pass
    except Exception:
        return False

def nephews_check(path: Path, output: str) -> bool:
    """
    Validate 9_nephews.py - tests all 3 scenarios:
    1. Mickey Mouse's nephew (Morty or Ferdie)
    2. Donald Duck's nephew (Huey, Dewey, or Louie)
    3. Not a nephew
    """
    try:
        # Test case 1: Mickey's nephew
        code1, out1, err1 = run_task(path, "Morty\n")
        expected1 = "Please type in your name: I think you might be one of Mickey Mouse's nephews.\n"
        test1_pass = (code1 == 0 and out1 == expected1)
        
        # Test case 2: Donald's nephew
        code2, out2, err2 = run_task(path, "Huey\n")
        expected2 = "Please type in your name: I think you might be one of Donald Duck's nephews.\n"
        test2_pass = (code2 == 0 and out2 == expected2)
        
        # Test case 3: Not a nephew
        code3, out3, err3 = run_task(path, "Ken\n")
        expected3 = "Please type in your name: You're not a nephew of any character I know of.\n"
        test3_pass = (code3 == 0 and out3 == expected3)
        
        return test1_pass and test2_pass and test3_pass
    except Exception:
        return False

def leap_year_check(path: Path, output: str) -> bool:
    """
    Validate 12_leap_year.py - tests multiple scenarios:
    1. Regular leap year (divisible by 4)
    2. Not a leap year
    3. Century non-leap year (divisible by 100 but not 400)
    """
    try:
        # Test case 1: Regular leap year
        code1, out1, err1 = run_task(path, "2020\n")
        expected1 = "Please type in a year: That year is a leap year.\n"
        test1_pass = (code1 == 0 and out1 == expected1)
        
        # Test case 2: Not a leap year
        code2, out2, err2 = run_task(path, "2011\n")
        expected2 = "Please type in a year: That year is not a leap year.\n"
        test2_pass = (code2 == 0 and out2 == expected2)
        
        # Test case 3: Century non-leap (1800 divisible by 100 but not 400)
        code3, out3, err3 = run_task(path, "1800\n")
        expected3 = "Please type in a year: That year is not a leap year.\n"
        test3_pass = (code3 == 0 and out3 == expected3)
        
        return test1_pass and test2_pass and test3_pass
    except Exception:
        return False

def grades_and_points_check(path: Path, output: str) -> bool:
    """
    Validate 10_grades_and_points.py - tests all 8 grade ranges:
    1. < 0: impossible!
    2. 0-49: fail
    3. 50-59: 1
    4. 60-69: 2
    5. 70-79: 3
    6. 80-89: 4
    7. 90-100: 5
    8. > 100: impossible!
    """
    try:
        # Test case 1: Negative (impossible!)
        code1, out1, err1 = run_task(path, "-3\n")
        expected1 = "How many points [0-100]: Grade: impossible!\n"
        test1_pass = (code1 == 0 and out1 == expected1)
        
        # Test case 2: Fail (0-49)
        code2, out2, err2 = run_task(path, "37\n")
        expected2 = "How many points [0-100]: Grade: fail\n"
        test2_pass = (code2 == 0 and out2 == expected2)
        
        # Test case 3: Grade 1 (50-59)
        code3, out3, err3 = run_task(path, "55\n")
        expected3 = "How many points [0-100]: Grade: 1\n"
        test3_pass = (code3 == 0 and out3 == expected3)
        
        # Test case 4: Grade 2 (60-69)
        code4, out4, err4 = run_task(path, "65\n")
        expected4 = "How many points [0-100]: Grade: 2\n"
        test4_pass = (code4 == 0 and out4 == expected4)
        
        # Test case 5: Grade 3 (70-79)
        code5, out5, err5 = run_task(path, "76\n")
        expected5 = "How many points [0-100]: Grade: 3\n"
        test5_pass = (code5 == 0 and out5 == expected5)
        
        # Test case 6: Grade 4 (80-89)
        code6, out6, err6 = run_task(path, "85\n")
        expected6 = "How many points [0-100]: Grade: 4\n"
        test6_pass = (code6 == 0 and out6 == expected6)
        
        # Test case 7: Grade 5 (90-100)
        code7, out7, err7 = run_task(path, "95\n")
        expected7 = "How many points [0-100]: Grade: 5\n"
        test7_pass = (code7 == 0 and out7 == expected7)
        
        # Test case 8: Over 100 (impossible!)
        code8, out8, err8 = run_task(path, "150\n")
        expected8 = "How many points [0-100]: Grade: impossible!\n"
        test8_pass = (code8 == 0 and out8 == expected8)
        
        return test1_pass and test2_pass and test3_pass and test4_pass and test5_pass and test6_pass and test7_pass and test8_pass
    except Exception:
        return False

def next_leap_year_check(path: Path, output: str) -> bool:
    """
    Validate 20_the_next_leap_year.py - tests both scenarios:
    1. From non-leap year
    2. From leap year (should give next one, not same)
    """
    try:
        # Test case 1: From non-leap year
        code1, out1, err1 = run_task(path, "2023\n")
        expected1 = "Year: The next leap year after 2023 is 2024\n"
        test1_pass = (code1 == 0 and out1 == expected1)
        
        # Test case 2: From leap year (should skip to next)
        code2, out2, err2 = run_task(path, "2024\n")
        expected2 = "Year: The next leap year after 2024 is 2028\n"
        test2_pass = (code2 == 0 and out2 == expected2)
        
        return test1_pass and test2_pass
    except Exception:
        return False

def alphabetically_in_middle_check(path: Path, output: str) -> bool:
    """
    Validate 13_alphabetically_in_the_middle.py - tests multiple orderings:
    1. x, c, p → middle is p
    2. C, B, A → middle is B
    3. a, b, c → middle is b (already sorted)
    """
    try:
        # Test case 1: x, c, p (from grader example)
        code1, out1, err1 = run_task(path, "x\nc\np\n")
        expected1 = "1st letter: 2nd letter: 3rd letter: The letter in the middle is p\n"
        test1_pass = (code1 == 0 and out1 == expected1)
        
        # Test case 2: C, B, A (from sample output - reverse order)
        code2, out2, err2 = run_task(path, "C\nB\nA\n")
        expected2 = "1st letter: 2nd letter: 3rd letter: The letter in the middle is B\n"
        test2_pass = (code2 == 0 and out2 == expected2)
        
        # Test case 3: a, b, c (already sorted)
        code3, out3, err3 = run_task(path, "a\nb\nc\n")
        expected3 = "1st letter: 2nd letter: 3rd letter: The letter in the middle is b\n"
        test3_pass = (code3 == 0 and out3 == expected3)
        
        return test1_pass and test2_pass and test3_pass
    except Exception:
        return False

def gift_tax_calculator_check(path: Path, output: str) -> bool:
    """
    Validate 14_gift_tax_calculator.py - tests all 6 tax brackets:
    1. < 5000: no tax
    2. 5000-25000: 100 + (value - 5000) * 0.08
    3. 25000-55000: 1700 + (value - 25000) * 0.10
    4. 55000-200000: 4700 + (value - 55000) * 0.12
    5. 200000-1000000: 22100 + (value - 200000) * 0.15
    6. >= 1000000: 142100 + (value - 1000000) * 0.17
    """
    try:
        # Test case 1: No tax (< 5000)
        code1, out1, err1 = run_task(path, "3500\n")
        expected1 = "Value of gift: No tax!\n"
        test1_pass = (code1 == 0 and out1 == expected1)
        
        # Test case 2: First bracket (5000-25000) - boundary test
        code2, out2, err2 = run_task(path, "5000\n")
        expected2 = "Value of gift: Amount of tax: 100.0 euros\n"
        test2_pass = (code2 == 0 and out2 == expected2)
        
        # Test case 3: Second bracket (25000-55000)
        code3, out3, err3 = run_task(path, "27500\n")
        expected3 = "Value of gift: Amount of tax: 1950.0 euros\n"
        test3_pass = (code3 == 0 and out3 == expected3)
        
        # Test case 4: Third bracket (55000-200000)
        code4, out4, err4 = run_task(path, "100000\n")
        expected4 = "Value of gift: Amount of tax: 10100.0 euros\n"
        test4_pass = (code4 == 0 and out4 == expected4)
        
        # Test case 5: Fourth bracket (200000-1000000)
        code5, out5, err5 = run_task(path, "500000\n")
        expected5 = "Value of gift: Amount of tax: 67100.0 euros\n"
        test5_pass = (code5 == 0 and out5 == expected5)
        
        # Test case 6: Fifth bracket (>= 1000000)
        code6, out6, err6 = run_task(path, "1500000\n")
        expected6 = "Value of gift: Amount of tax: 227100.0 euros\n"
        test6_pass = (code6 == 0 and out6 == expected6)
        
        return test1_pass and test2_pass and test3_pass and test4_pass and test5_pass and test6_pass
    except Exception:
        return False

def fizzbuzz_check(path: Path, output: str) -> bool:
    """
    Validate 11_fizzbuzz.py - tests multiple scenarios:
    1. Divisible by 3 only -> Fizz
    2. Divisible by 5 only -> Buzz
    3. Divisible by both 3 and 5 -> FizzBuzz
    4. Not divisible by 3 or 5 -> prints nothing (just prompt)
    """
    try:
        # Test case 1: Divisible by 3 only (9)
        code1, out1, err1 = run_task(path, "9\n")
        expected1 = "Number: Fizz\n"
        test1_pass = (code1 == 0 and out1 == expected1)
        
        # Test case 2: Divisible by 5 only (20)
        code2, out2, err2 = run_task(path, "20\n")
        expected2 = "Number: Buzz\n"
        test2_pass = (code2 == 0 and out2 == expected2)
        
        # Test case 3: Divisible by both (45)
        code3, out3, err3 = run_task(path, "45\n")
        expected3 = "Number: FizzBuzz\n"
        test3_pass = (code3 == 0 and out3 == expected3)
        
        # Test case 4: Not divisible by either (7)
        code4, out4, err4 = run_task(path, "7\n")
        expected4 = "Number: \n"
        test4_pass = (code4 == 0 and out4 == expected4)
        
        return test1_pass and test2_pass and test3_pass and test4_pass
    except Exception:
        return False

def pin_attempts_check(path: Path, output: str) -> bool:
    """
    Validate 19_pin_and_number_of_attempts.py - tests both scenarios:
    1. Multiple attempts (4 attempts)
    2. Single attempt (correct on first try)
    """
    try:
        # Test case 1: Multiple attempts
        code1, out1, err1 = run_task(path, "3245\n1234\n0000\n4321\n")
        expected1 = "PIN: Wrong\nPIN: Wrong\nPIN: Wrong\nPIN: Correct! It took you 4 attempts\n"
        test1_pass = (code1 == 0 and out1 == expected1)
        
        # Test case 2: Correct on first try
        code2, out2, err2 = run_task(path, "4321\n")
        expected2 = "PIN: Correct! It only took you one single attempt!\n"
        test2_pass = (code2 == 0 and out2 == expected2)
        
        return test1_pass and test2_pass
    except Exception:
        return False

def story_check(path: Path, output: str) -> bool:
    """
    Validate 21_story.py - tests both termination scenarios:
    1. End with "end" keyword
    2. End with duplicate word
    """
    try:
        # Test case 1: Terminate with "end"
        code1, out1, err1 = run_task(path, "Once\nupon\na\ntime\nthere\nwas\na\ngirl\nend\n")
        # Count prompts - should be 9 (8 words + "end")
        prompt_count1 = out1.count("Please type in a word:")
        story1 = "Once upon a time there was a girl"
        test1_pass = (code1 == 0 and prompt_count1 == 9 and story1 in out1)
        
        # Test case 2: Terminate with duplicate word
        code2, out2, err2 = run_task(path, "It\nwas\na\ndark\nand\nstormy\nnight\nnight\n")
        # Count prompts - should be 8 (7 words + duplicate "night")
        prompt_count2 = out2.count("Please type in a word:")
        story2 = "It was a dark and stormy night"
        test2_pass = (code2 == 0 and prompt_count2 == 8 and story2 in out2)
        
        return test1_pass and test2_pass
    except Exception:
        return False

def extract_task_number(filename: str) -> int:
    """Extract the task number from a filename like '12_arithmetics.py' -> 12"""
    try:
        return int(filename.split('_')[0])
    except (ValueError, IndexError):
        return 999  # Put files without numbers at the end

def grade_part2():
    state = load_state()
    prev = state.get("parts", {}).get("2", {}).get("tasks", {})
    results = {}
    part_score = 0
    
    # Combine all tasks
    all_tasks = list(EXPECTED.keys()) + list(DYNAMIC_CHECKS.keys()) + list(INTERACTIVE.keys())
    total_tasks = len(all_tasks)
    
    # Store detailed results for sorted output
    task_details = {}

    if total_tasks == 0:
        print("No tasks defined yet for Part 2. Add tasks to EXPECTED, DYNAMIC_CHECKS or INTERACTIVE dictionaries.")
        # Still write an updated marksheet/points.json with zero totals
        state.setdefault("parts", {})
        state["parts"]["2"] = {"tasks": {}, "score": 0, "total": 0}
        state["total_points"] = sum(p.get("score", 0) for k, p in state["parts"].items() if k != "5")
        save_state(state)
        write_marksheet(state, get_display_user())
        return

    print("Grading Part 2 — Conditionals and Loops")
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

    # Grade dynamic check tasks (e.g., tasks needing multiple test cases)
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
        if check_func_name == "number_of_characters_check":
            code = 0
            passed_now = number_of_characters_check(path, "")
        elif check_func_name == "typecasting_check":
            code = 0
            passed_now = typecasting_check(path, "")
        elif check_func_name == "age_of_maturity_check":
            code = 0
            passed_now = age_of_maturity_check(path, "")
        elif check_func_name == "greater_than_or_equal_check":
            code = 0
            passed_now = greater_than_or_equal_check(path, "")
        elif check_func_name == "elder_check":
            code = 0
            passed_now = elder_check(path, "")
        elif check_func_name == "alphabetically_last_check":
            code = 0
            passed_now = alphabetically_last_check(path, "")
        elif check_func_name == "age_check_check":
            code = 0
            passed_now = age_check_check(path, "")
        elif check_func_name == "nephews_check":
            code = 0
            passed_now = nephews_check(path, "")
        elif check_func_name == "grades_and_points_check":
            code = 0
            passed_now = grades_and_points_check(path, "")
        elif check_func_name == "fizzbuzz_check":
            code = 0
            passed_now = fizzbuzz_check(path, "")
        elif check_func_name == "leap_year_check":
            code = 0
            passed_now = leap_year_check(path, "")
        elif check_func_name == "alphabetically_in_middle_check":
            code = 0
            passed_now = alphabetically_in_middle_check(path, "")
        elif check_func_name == "gift_tax_calculator_check":
            code = 0
            passed_now = gift_tax_calculator_check(path, "")
        elif check_func_name == "pin_attempts_check":
            code = 0
            passed_now = pin_attempts_check(path, "")
        elif check_func_name == "next_leap_year_check":
            code = 0
            passed_now = next_leap_year_check(path, "")
        elif check_func_name == "story_check":
            code = 0
            passed_now = story_check(path, "")
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
            message = "  Output format or test cases failed"
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

    state.setdefault("parts", {})
    state["parts"]["2"] = {"tasks": results, "score": part_score, "total": total_tasks}
    # Exclude Part 5 from total aggregation
    state["total_points"] = sum(p.get("score", 0) for k, p in state["parts"].items() if k != "5")
    save_state(state)
    # Write marksheet markdown
    write_marksheet(state, get_display_user())

    print("-" * 40)
    user = get_display_user()
    if user:
        print(f"{user}: your Part 2 score is {part_score}/{total_tasks}")
        print(f"{user}: your total score is {state['total_points']}")
    else:
        print(f"Part 2 score: {part_score}/{total_tasks}")
        print(f"Cumulative score: {state['total_points']}")
    print(f"(Saved to {PROGRESS})")

if __name__ == "__main__":
    grade_part2()
