#!/usr/bin/env python3
"""
Part 6 Grader — awards 1 point per correct task and persists progress.
Usage:
    python part6/grade_part6.py
    (Windows) python part6\\grade_part6.py
"""
from __future__ import annotations
import json, os, sys, subprocess, time, re, shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent       # part6 folder
WORKSPACE_ROOT = ROOT.parent                 # repository/workspace root
# Use shared workspace-level progress file for all parts
PROGRESS = WORKSPACE_ROOT / ".progress" / "points.json"
PROGRESS_DIR = PROGRESS.parent
MARKSHEET_DIR = WORKSPACE_ROOT / ".progress"

EXPECTED = {
    # Section 6.1 - Reading files (function outputs with test data files)
    "1_largest_number.py": "1100\n",
    # Section 6.2 - Writing files (check file creation/content)
    "10_inscription.py": "Hi John, we hope you enjoy learning Python with us! Best, Mooc.fi Team\n",
}

INTERACTIVE = {
    # Section 6.1 - Reading files (interactive)
    "4_course_grading_part1.py": {
        "inputs": [],
        "expected_output": "Peter Python 21\nJean Java 27\n"
    },
    "5_course_grading_part2.py": {
        "inputs": [],
        "expected_output": "Peter Python 21 34 55\nJean Java 27 50 77\n"
    },
    "7_spell_checker.py": {
        "inputs": ["I love Python and Java but COBOL is old"],
        "expected_output": "Enter text: I love Python and Java but *COBOL* is old\n"
    },
    # Section 6.2 - Writing files (interactive)
    "11_diary.py": {
        "inputs": ["1", "Today was a good day", "1", "I learned about file handling", "2", "0"],
        "expected_output": "1 - add an entry, 2 - read entries, 0 - quit\nFunction: Diary entry: Diary saved\n1 - add an entry, 2 - read entries, 0 - quit\nFunction: Diary entry: Diary saved\n1 - add an entry, 2 - read entries, 0 - quit\nFunction: Entries:\nToday was a good day\nI learned about file handling\n1 - add an entry, 2 - read entries, 0 - quit\nFunction: Bye now!\n"
    },
    "15_word_search.py": {
        "inputs": ["ca*"],
        "expected_output": "Search term: ['cat', 'car', 'carbon', 'california', 'caring', 'catapult', 'care', 'calm']\n"
    },
    "16_dictionary_file.py": {
        "inputs": ["1", "auto", "car", "1", "roska", "garbage", "1", "laukku", "bag", "2", "bag", "2", "car", "2", "laukku", "3"],
        "expected_output": "1 - Add word, 2 - Search, 3 - Quit\nFunction: The word in Finnish: The word in English: Dictionary entry added\n1 - Add word, 2 - Search, 3 - Quit\nFunction: The word in Finnish: The word in English: Dictionary entry added\n1 - Add word, 2 - Search, 3 - Quit\nFunction: The word in Finnish: The word in English: Dictionary entry added\n1 - Add word, 2 - Search, 3 - Quit\nFunction: Search term: roska - garbage\nlaukku - bag\n1 - Add word, 2 - Search, 3 - Quit\nFunction: Search term: auto - car\n1 - Add word, 2 - Search, 3 - Quit\nFunction: Search term: laukku - bag\n1 - Add word, 2 - Search, 3 - Quit\nFunction: Bye!\n"
    },
    # Section 6.3 - Handling errors (interactive)
    "17_reading_input.py": {
        "inputs": ["2", "fifteen", "8"],
        "expected_output": "Please type in a number: You must type in an integer between 5 and 10\nPlease type in a number: You must type in an integer between 5 and 10\nPlease type in a number: You typed in: 8\n"
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
    MARKSHEET_DIR.mkdir(parents=True, exist_ok=True)
    lines = []
    title_name = user if user else "Student"
    lines.append("# Basics of Programming")
    lines.append("")
    lines.append(f"## Hi {title_name}, check your scores below!")
    lines.append("")
    lines.append(f"Last updated: {state.get('updated_at','')}")
    lines.append("")
    lines.append("| Part | Score | Max | Percent | Progress |")
    lines.append("|------|-------|-----|---------|----------|")
    parts = state.get("parts", {})
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
        filled = int(round((score / total) * 10)) if total else 0
        bar = "█" * filled + "░" * (10 - filled)
        lines.append(f"| Part {part_key} | {score} | {total} | {percent}% | {bar} |")
    lines.append("")
    # Calculate total points (Parts 1-4, 6: 31+22+34+37+9 = 133)
    max_points = sum(p.get("total", 0) for k, p in parts.items())
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
    try:
        proc = subprocess.run(args, cwd=str(cwd) if cwd else None, text=True, capture_output=True, timeout=timeout)
        return proc.returncode, proc.stdout.strip()
    except Exception:
        return 1, ""

def get_display_user() -> str | None:
    for key in ("GITHUB_USER", "GITHUB_USERNAME", "GH_USER"):
        v = os.environ.get(key)
        if v:
            return v.strip()
    if shutil.which("gh"):
        rc, out = _run_capture(["gh", "api", "user", "--jq", ".login"])
        if rc == 0 and out:
            return out
    rc, out = _run_capture(["git", "-C", str(WORKSPACE_ROOT), "config", "--get", "user.name"])
    if rc == 0 and out:
        return out
    rc, url = _run_capture(["git", "-C", str(WORKSPACE_ROOT), "config", "--get", "remote.origin.url"])
    if rc == 0 and url:
        m = re.search(r"github\.com[/:]([^/\s]+)/", url, re.IGNORECASE)
        if m:
            return m.group(1)
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

def extract_task_number(filename: str) -> int:
    """Extract the task number from a filename like '15_word_search.py' -> 15"""
    try:
        return int(filename.split('_')[0])
    except (ValueError, IndexError):
        return 999  # Put files without numbers at the end

def grade_part6():
    state = load_state()
    prev = state.get("parts", {}).get("6", {}).get("tasks", {})
    results = {}
    task_details = {}
    part_score = 0
    all_tasks = list(EXPECTED.keys()) + list(INTERACTIVE.keys())
    total_tasks = len(all_tasks)

    if total_tasks == 0:
        print("No tasks defined yet for Part 6. Add tasks to EXPECTED or INTERACTIVE dictionaries.")
        return

    print("Grading Part 6")
    print()

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

    for fname, test_spec in INTERACTIVE.items():
        path = ROOT / fname
        
        # Clean up diary.txt before testing 11_diary.py
        if fname == "11_diary.py":
            diary_file = ROOT / "diary.txt"
            if diary_file.exists():
                diary_file.unlink()
        
        # Clean up dictionary.txt before testing 16_dictionary_file.py
        if fname == "16_dictionary_file.py":
            dict_file = ROOT / "dictionary.txt"
            if dict_file.exists():
                dict_file.unlink()
        
        # Check if file has actual implementation
        if not has_implementation(path):
            results[fname] = False
            task_details[fname] = {
                "status": "FAIL",
                "message": "(no implementation)",
                "passed": False
            }
            continue
        
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
    state["parts"]["6"] = {"tasks": results, "score": part_score, "total": total_tasks}
    # Calculate cumulative total points
    state["total_points"] = sum(p.get("score", 0) for k, p in state["parts"].items())
    save_state(state)
    write_marksheet(state, get_display_user())

    print()
    user = get_display_user()
    if user:
        print(f"{user}: your Part 6 score is {part_score}/{total_tasks}")
        print(f"{user}: your total score is {state['total_points']}")
    else:
        print(f"Part 6 score: {part_score}/{total_tasks}")
        print(f"Cumulative score: {state['total_points']}")
    print(f"(Saved to {PROGRESS})")

if __name__ == "__main__":
    grade_part6()
