# Prompt: Setup New Course Part with Auto-Grading

Use this prompt to create a new part (e.g., Part 3, Part 4) for the Python Programming Course with complete task files, grader, and documentation.

## Instructions for AI Agent

I want to add **Part [NUMBER]** to my Python programming course with the following tasks:

### Part [NUMBER]: [TITLE] ([TASK_COUNT] tasks)

#### Section [X.Y]: [SECTION_NAME] ([COUNT] tasks)
1. `[X.Y.1_filename].py` - [Brief description]
2. `[X.Y.2_filename].py` - [Brief description]
...

[Repeat for all sections]

---

## Required Steps

Please complete ALL of the following steps in order:

### Step 1: Create Task Files
For each task listed above:
1. Create the file: `part[N]/part[N]Exercises/tasks/[filename].py`
2. Include a comprehensive docstring with:
   - Task title and number
   - Task description
   - Interaction example (sample input/output)
   - Detailed instructions
3. Add standardized TODO comments:
   ```python
   # TODO: Write your solution below this line
   # Save your file and run it using: python [filename].py
   ```
4. **For initial setup:** Add only a `pass` statement or TODO stub (no implementation yet)
5. **For complete setup:** Implement the full solution matching the grader expectations

### Step 2: Create/Update Grader
Create `part[N]/part[N]Exercises/tasks/grade_part[N].py` with:

1. **Standard imports and paths:**
   ```python
   from __future__ import annotations
   import json, os, sys, subprocess, time, re, shutil
   from pathlib import Path
   
   ROOT = Path(__file__).resolve().parents[1]  # part[N]Exercises
   REPO_ROOT = ROOT.parent                      # part[N] folder
   WORKSPACE_ROOT = REPO_ROOT.parent            # workspace root
   PROGRESS = WORKSPACE_ROOT / ".progress" / "points.json"
   PROGRESS_DIR = PROGRESS.parent
   MARKSHEET_DIR = WORKSPACE_ROOT / ".progress"
   ```

2. **Test dictionaries:**
   - `EXPECTED = {}` for non-interactive tasks (output-only tests)
   - `INTERACTIVE = {}` for tasks requiring stdin input
   
   Format for INTERACTIVE:
   ```python
   "filename.py": {
       "inputs": ["input1", "input2", ...],
       "expected_output": "exact expected output with \\n for newlines"
   }
   ```

3. **Include these functions:**
   - `load_state()` - Load progress from JSON
   - `save_state(state)` - Save progress to JSON
   - `write_marksheet(state, user)` - Generate markdown report with 4-scale grading
   - `get_display_user()` - Detect username (env/gh/git/OS)
   - `has_implementation(pyfile)` - **NEW: Verify file contains actual code (not just TODO/docstrings)**
   - `run_task(pyfile, input_data)` - Execute task with 5s timeout
   - `grade_part[N]()` - Main grading loop

4. **Grading logic (UPDATED - Academic Integrity):**
   - Detect all tasks from EXPECTED + INTERACTIVE
   - **Check `has_implementation()` BEFORE running each task**
   - Award `FAIL (no implementation)` if file is empty/TODO-only
   - Compare actual vs expected output (exact match)
   - **Live evaluation only (NO sticky passes - tasks re-evaluated every run)**
   - **Exclude Part 5 from total_points calculation** (optional content)
   - Calculate 4-scale grade: Fail (0-49%), 1 (50-64%), 2 (65-84%), 3 (85-100%)
   - Update Part [N] score and cumulative total
   - Generate/update workspace-level marksheet

### Step 3: Run the Grader
Execute the grader to validate:
```bash
python part[N]/part[N]Exercises/tasks/grade_part[N].py
```

Expected initial output: `0/[TASK_COUNT]` passing (if tasks are stubs)

Verify:
- All tasks detected by grader
- `.progress/points.json` updated with Part [N] entry
- `.progress/marksheet.md` regenerated with Part [N] progress bar

### Step 4: Create Part [N] README
Create `part[N]/README.md` with:

```markdown
# Part [N]: [TITLE] ([TASK_COUNT] points)

📚 Topics: [topic1, topic2, topic3]

📖 Reading materials: [URL if available]

## Folders
- `part[N]Exercises/tasks/` — Write your solutions here
- `.progress/` — Your scores are saved here

## Instructions
1. Write each solution in: `part[N]Exercises/tasks/`
2. Test a task:
   
   Windows (PowerShell/CMD)
   \`\`\`bat
   python part[N]Exercises\\tasks\\[X.Y.Z_example].py
   \`\`\`

   macOS/Linux
   \`\`\`bash
   python part[N]/part[N]Exercises/tasks/[X.Y.Z_example].py
   \`\`\`

3. Grade Part [N]:

   Windows
   \`\`\`bat
   cd part[N]\\part[N]Exercises\\tasks
   python grade_part[N].py
   \`\`\`

   macOS/Linux
   \`\`\`bash
   cd part[N]/part[N]Exercises/tasks
   python grade_part[N].py
   \`\`\`

Each task is worth 1 point. Your score persists across grading sessions.

---

## Task Overview ([TASK_COUNT] total)

| Section | Tasks | Topics |
|---------|-------|--------|
| [X.Y] [Section Name] | [COUNT] | [topics] |
| [X.Z] [Section Name] | [COUNT] | [topics] |

### Task Files Location
All tasks are in: `part[N]Exercises/tasks/`

> Tip: Open each task file to see detailed instructions and sample input/output.

---

## Grading
Run the grader to check your solutions:

Windows
\`\`\`bat
cd part[N]\\part[N]Exercises\\tasks
python grade_part[N].py
\`\`\`

macOS/Linux
\`\`\`bash
cd part[N]/part[N]Exercises/tasks
python grade_part[N].py
\`\`\`

The auotmated grader will:
- ✓ Check each task's output against expected results
- ✓ **Verify files contain actual implementation (not just TODO stubs)**
- ✓ Award 1 point per correct task ([TASK_COUNT] points total)
- ✓ Save your cumulative score to: `workspace/.progress/points.json`
- ✓ Generate a progress report at: `workspace/.progress/marksheet.md`
- ✓ Show your Part [N] score and total score across all parts
- ✓ **Calculate grade: Fail / 1 / 2 / 3 based on percentage**

**Important:** Tasks are evaluated based on their current implementation each time the grader runs.
If you delete your solution, the task will fail on the next grading run.

---

## Save Your Work — Git Commit & Push

Important: After completing tasks, commit and push your changes to GitHub.

Step 1: Check what changed
\`\`\`bash
git status
\`\`\`

Step 2: Add your completed task files
\`\`\`bash
# Add specific files
git add part[N]/part[N]Exercises/tasks/[X.Y.Z_example].py

# OR add all changed files at once
git add .
\`\`\`

Step 3: Commit with a message
\`\`\`bash
git commit -m "Complete Part [N] tasks: [task names]"
\`\`\`

Step 4: Push to GitHub
\`\`\`bash
git push
\`\`\`

> Best Practice: Commit after completing each task or section to track progress and create a backup.

> Reminder: Your local progress (`workspace/.progress/`) is tracked. Push regularly to avoid losing work!

---

## Summary

- Total Points: [TASK_COUNT]
- Sections: [NUMBER] ([list section names])
- Key Concepts: [list main concepts]
- Progress Tracking: Scores saved in `workspace/.progress/points.json`
- Progress Report: View in `workspace/.progress/marksheet.md`

Good luck and have fun! 🚀
```

### Step 5: Update Main README
Update `README.md` (workspace root):

1. **Update Course Overview table:**
   ```markdown
   | Part [N] | [TITLE] | [TASK_COUNT] | Scaffolded |
   ```
   Note: Use "Scaffolded" (not "Complete") to indicate structure exists but solutions need implementation.

2. **Add Part [N] section with all tasks:**
   ```markdown
   ## Part [N]: [TITLE] ([TASK_COUNT] tasks)
   
   ### Section [X.Y]: [SECTION_NAME] ([COUNT])
   1. `[filename].py` - [description]
   ...
   ```

3. **Update total task count at the top**

### Step 6: Verify Integration
1. Run the Part [N] grader again
2. Check `.progress/marksheet.md` shows Part [N] with progress bar
3. Verify total points updated correctly
4. Test running 1-2 individual task files

### Step 7: (Optional) Implement Solutions
If you want working solutions instead of stubs:
1. Read each task's docstring carefully
2. Implement the solution matching the grader's expected output exactly
3. Pay attention to:
   - Exact prompt text (including spaces, colons, punctuation)
   - Output formatting (spaces, newlines, number precision)
   - Edge cases mentioned in instructions
4. Re-run grader to verify all tests pass

---

## Example Usage

### For Part 3 with 34 tasks:

```
I want to add Part 3 to my Python programming course with the following tasks:

### Part 3: Loops & Functions (34 tasks)

#### Section 3.1: Loops with conditions (7)
1. `3.1.1_print_numbers.py` - Print numbers from 1 to n
2. `3.1.2_fix_the_code_countdown.py` - Fix infinite loop bug
3. `3.1.3_numbers.py` - Print numbers with while loop
4. `3.1.4_powers_of_two.py` - Print powers of 2 up to n
5. `3.1.5_powers_of_base_n.py` - Powers of user-specified base
6. `3.1.6_sum_of_consecutive_numbers_v1.py` - Sum from 1 to n
7. `3.1.7_sum_of_consecutive_numbers_v2.py` - Sum with upper limit

#### Section 3.2: Working with strings (15)
[... list all tasks ...]

[... continue for all sections ...]
```

Then follow all steps above.

---

## Testing Checklist

After completing all steps, verify:

- [ ] All task files created in `part[N]/part[N]Exercises/tasks/`
- [ ] Each task has proper docstring and TODO comments
- [ ] Grader created: `grade_part[N].py`
- [ ] Grader detects all [TASK_COUNT] tasks
- [ ] Grader runs without errors
- [ ] `.progress/points.json` includes Part [N] entry
- [ ] `.progress/marksheet.md` shows Part [N] with progress bar
- [ ] Part [N] README created with all sections
- [ ] Main README updated with Part [N] details
- [ ] Total task count is correct in main README
- [ ] Can run individual task files
- [ ] Git workflow instructions included in Part README

---

## Notes

- **Academic Integrity Protection:** The `has_implementation()` function prevents credit for empty files, TODO stubs, or deleted solutions. Students must have actual working code to receive points.
- **Live Evaluation:** Tasks are re-evaluated on every grader run. No "sticky passes" - deleting a solution causes it to fail again.
- **Part 5 Exclusion:** Part 5 is optional and excluded from total points calculation (max = 143 from Parts 1,2,3,4,6).
- **4-Scale Grading:** Fail (<50%), 1 (50-64%), 2 (65-84%), 3 (85-100%) calculated from total/143.
- **Exact output matching:** Grader uses exact string comparison. Even a single space or newline difference will cause failure.
- **Timeout:** All tasks have 5-second execution timeout to prevent infinite loops.
- **Username detection:** Grader attempts to detect GitHub username via env vars, gh CLI, git config, or OS username.
- **Marksheet format:** Auto-generated with progress bars (10 chars), percentages, and per-part details.
- **File naming:** Use underscores: `X.Y.Z_descriptive_name.py`
- **No solutions in stubs:** Initial task files should have TODO and `pass` only, unless specifically implementing solutions.

---

## Common Issues & Solutions

1. **Task shows "FAIL (no implementation)"**
   - File contains only TODO comments or docstrings
   - Add actual code implementation below the TODO line
   - Must have at least one substantive line of code (not just `pass` or imports)

2. **Grader shows "String replacement failed"**
   - Check for exact whitespace in task output
   - Verify newlines: use `\n` explicitly
   - Check for trailing spaces or missing line breaks

3. **Task output differs by precision (floats)**
   - Note in task docstring if precision is intentional
   - Use format strings: `f"{value:.1f}"` for consistent decimals

4. **Interactive tasks hang**
   - Ensure `inputs` list has enough entries
   - Check for infinite loops in task code
   - Timeout (5s) will kill hanging tasks

5. **Marksheet not updating**
   - Verify `WORKSPACE_ROOT` path is correct
   - Check `.progress/` directory permissions
   - Ensure `write_marksheet()` is called in grader

6. **Tasks not detected**
   - Check filename matches grader dictionary key exactly
   - Verify file is in `part[N]Exercises/tasks/` directory
   - Run grader from correct directory

7. **Points.json manually edited but grader overwrites**
   - This is intentional - graders recalculate scores from actual code on every run
   - Manual edits to progress files are always overwritten
   - Prevents score manipulation

---

## File Structure Reference

```
workspace/
├── README.md                           # Main course overview
├── .progress/
│   ├── points.json                     # Cumulative scores (all parts)
│   └── marksheet.md                    # Auto-generated progress report
├── part[N]/
│   ├── README.md                       # Part-specific instructions
│   └── part[N]Exercises/
│       └── tasks/
│           ├── [X.Y.1_task].py        # Task files
│           ├── [X.Y.2_task].py
│           ├── ...
│           └── grade_part[N].py       # Grader script
```

---

## Quick Reference: Grader Test Entry Formats

**Non-interactive (output only):**
```python
EXPECTED = {
    "filename.py": "Expected output line 1\nExpected output line 2\n"
}
```

**Interactive (with input):**
```python
INTERACTIVE = {
    "filename.py": {
        "inputs": ["input1", "input2"],
        "expected_output": "Prompt: Prompt: Result\n"
    }
}
```

## Required: Academic Integrity Function

**MUST include this function in every grader:**

```python
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
        lines = content.split('\n')
        code_lines = []
        in_docstring = False
        docstring_char = None
        
        for line in lines:
            stripped = line.strip()
            
            # Track docstring boundaries
            if '"""' in stripped or "'''" in stripped:
                if not in_docstring:
                    docstring_char = '"""' if '"""' in stripped else "'''"
                    in_docstring = True
                    if stripped.count(docstring_char) >= 2:
                        in_docstring = False
                    continue
                else:
                    in_docstring = False
                    continue
            
            if in_docstring:
                continue
            
            # Skip comments and empty lines
            if not stripped or stripped.startswith('#'):
                continue
            
            # Skip TODO comments
            if 'TODO' in stripped.upper() and '#' in stripped:
                continue
            
            code_lines.append(stripped)
        
        # Must have substantive code (not just imports/pass)
        substantive_code = [line for line in code_lines 
                          if line and line != 'pass' 
                          and not line.startswith('import ') 
                          and not line.startswith('from ')]
        
        return len(substantive_code) > 0
    except Exception:
        return False
```

**Use in grading loop:**

```python
# Before running each task, check for implementation
for fname, expected in EXPECTED.items():
    path = ROOT / "tasks" / fname
    
    # Check if file has actual implementation
    if not has_implementation(path):
        results[fname] = False
        print(f"{fname:30}  FAIL (no implementation)")
        continue
    
    # Only run if implementation exists
    code, out, err = run_task(path)
    passed = (code == 0 and out == expected)
    # ... continue grading
```

**Exclude Part 5 from total points:**

```python
# In grade_partX.py, after saving part results:
state.setdefault("parts", {})
state["parts"]["X"] = {"tasks": results, "score": part_score, "total": total_tasks}

# IMPORTANT: Exclude Part 5 from cumulative total (optional content)
state["total_points"] = sum(
    p.get("score", 0) 
    for k, p in state["parts"].items() 
    if k != "5"  # Part 5 is optional
)

save_state(state)
write_marksheet(state, get_display_user())
```

**4-Scale Grading in Marksheet:**

The `write_marksheet()` function should calculate and display:

```python
# Calculate grade based on percentage (excluding Part 5)
total_points = state.get("total_points", 0)
max_points = 143  # Total excluding Part 5's 25 points
percentage = (total_points / max_points * 100) if max_points > 0 else 0

if percentage < 50:
    grade = "Fail"
elif percentage < 65:
    grade = "1"
elif percentage < 85:
    grade = "2"
else:
    grade = "3"

# Display in marksheet:
# **Total points:** {total_points}/143
# **Grade:** {grade} ({percentage:.1f}%)
```

---

## Automation Tips

1. **Batch file creation:** Use a Python script to generate all task files from a list
2. **Template-based:** Create a task file template and fill in per-task details
3. **Grader generation:** Build grader dictionary from a CSV/JSON spec file
4. **README generation:** Auto-generate README sections from task metadata

---

This prompt ensures consistent, complete setup of new course parts with:
- ✅ Proper file structure
- ✅ Comprehensive documentation
- ✅ Working auto-grader with live evaluation (no sticky passes)
- ✅ **Academic integrity protection (implementation verification)**
- ✅ **4-scale grading system (Fail/1/2/3)**
- ✅ **Part 5 exclusion from totals (optional content)**
- ✅ Student-friendly instructions
- ✅ Git workflow guidance
- ✅ Integration with existing parts
- ✅ **Teacher guide for verification (TEACHER_GUIDE.md)**

---

## Change Log (Recent Updates)

### Version 2.0 - Academic Integrity & Live Grading (Oct 2025)

**Breaking Changes:**
- ❌ Removed sticky-pass behavior (tasks re-evaluated every run)
- ✅ Added `has_implementation()` verification function
- ✅ Part 5 now excluded from total points (143 max instead of 168)
- ✅ 4-scale grading system: Fail / 1 / 2 / 3
- ✅ Tasks show `FAIL (no implementation)` if empty/TODO-only

**What This Means:**
- Students must have actual code to get points
- Deleting solutions causes tasks to fail again
- Prevents score manipulation via JSON editing
- Teacher workflow: clone repo → run graders → check marksheet
- See `TEACHER_GUIDE.md` for complete academic integrity documentation

**Migration Notes:**
- All 6 graders updated with new verification logic
- Old progress files compatible (just re-evaluated live)
- README files updated to reflect "Scaffolded" status and live grading
- Marksheet now shows grade (Fail/1/2/3) and percentage
