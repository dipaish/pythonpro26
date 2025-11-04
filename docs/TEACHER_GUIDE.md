# Teacher Guide: Grading System & Academic Integrity

This document explains how the grading system ensures academic integrity and prevents score manipulation.

## 🛡️ Academic Integrity Features

### 1. Implementation Verification

**All graders automatically verify that task files contain actual code** before awarding points.

#### What Gets Rejected:
- ❌ Empty files
- ❌ Files with only TODO comments
- ❌ Files with only docstrings
- ❌ Files with only `import` statements
- ❌ Files with only `pass` statements
- ❌ Deleted or removed solutions

#### Example Output:
```
1_emoticon.py                   FAIL (no implementation)
2_seven_brothers.py             PASS
```

### 2. How It Works

The `has_implementation()` function in each grader:

1. **Parses the file** and removes:
   - Docstrings (triple-quoted strings)
   - Comments (lines starting with `#`)
   - TODO markers
   - Empty lines

2. **Checks for substantive code**:
   - Must have at least one line of actual code
   - Cannot be just `import` or `from` statements
   - Cannot be just `pass` statements

3. **Fails the task** if no implementation found:
   - Shows `FAIL (no implementation)` in grader output
   - Awards 0 points
   - Prevents score inflation

### 3. Live Evaluation System

**Tasks are evaluated based on their current state** - no "sticky passes":

- ✅ If a student deletes their solution after passing → task fails on next run
- ✅ If a student modifies a passing solution → re-evaluated immediately
- ✅ Scores always reflect current code state, not past achievements

This prevents students from:
- Passing tasks once then deleting implementations
- Submitting empty repos with high scores
- Gaming the system with TODO stubs

### 4. Score File Protection

While the `.progress/points.json` file stores scores, it's **regenerated on every grader run**:

```json
{
  "parts": {
    "1": {
      "tasks": {
        "1_emoticon.py": false,  // Re-evaluated each time
        "2_seven_brothers.py": true
      },
      "score": 1,
      "total": 31
    }
  },
  "total_points": 5
}
```

**Key Points:**
- Scores are recalculated from scratch each time
- Manual edits to `points.json` are overwritten immediately
- The grader runs the actual code to verify correctness
- No caching of previous results

### 5. Teacher Verification Workflow

When a student submits their work via GitHub:

#### Step 1: Clone Their Repository
```bash
git clone https://github.com/student-username/pythonpro26.git
cd pythonpro26
```

#### Step 2: Run All Graders
```bash
# Run each part's grader
python part1/part1Exercises/tasks/grade_part1.py
python part2/part2Exercises/tasks/grade_part2.py
python part3/part3Exercises/tasks/grade_part3.py
python part4/part4Exercises/tasks/grade_part4.py
python part5/part5Exercises/tasks/grade_part5.py
python part6/part6Exercises/tasks/grade_part6.py
```

#### Step 3: Check the Marksheet
```bash
cat .progress/marksheet.md
```

The marksheet shows:
- Overall score out of 143 points (Part 5 optional, not counted)
- Grade: Fail / 1 / 2 / 3
- Per-part breakdown
- Failed task files listed

#### Step 4: Spot Check Task Files

Random sample check to verify implementations:
```bash
# Pick random files from failed tasks list
cat part1/part1Exercises/tasks/1_emoticon.py
cat part3/part3Exercises/tasks/3.1.1_print_numbers.py
```

**Red flags to watch for:**
- Files with only TODO comments
- Empty or near-empty files
- Copy-pasted solutions that don't work
- Files with suspicious modification dates (all edited on same day/hour)

### 6. Common Manipulation Attempts (All Prevented)

| Attack | Student Tries | System Response |
|--------|---------------|-----------------|
| **Empty repo** | Delete all code, submit with old scores | Grader fails all tasks: `FAIL (no implementation)` |
| **Score editing** | Manually edit `points.json` to 143/143 | Grader overwrites file, recalculates from actual results |
| **TODO stubs** | Leave files as TODO templates | Grader detects no implementation, awards 0 points |
| **Partial deletion** | Keep function signature, delete body | Grader catches empty/pass-only implementations |
| **Copy .progress** | Copy someone else's progress files | Useless - grader re-evaluates their actual code |

### 7. Part 5: Optional Content

**Part 5 is excluded from the total score calculation:**

- Students can attempt Part 5 for extra practice
- Part 5 score shown but NOT counted toward 143-point total
- Grade calculated from Parts 1, 2, 3, 4, 6 only (143 points max)
- This is by design - advanced optional material

```python
# In all graders:
state["total_points"] = sum(
    p.get("score", 0) 
    for k, p in state["parts"].items() 
    if k != "5"  # Exclude Part 5
)
```

### 8. Grading Scale

**4-Scale System** (calculated from X/143):

| Grade | Percentage | Interpretation |
|-------|------------|----------------|
| **Fail** | 0-49% | Less than half completed |
| **1** | 50-64% | Passing, basic competency |
| **2** | 65-84% | Good understanding |
| **3** | 85-100% | Excellent mastery |

Example marksheet output:
```
Total points: 98/143
Grade: 2 (68.5%)
```

### 9. Best Practices for Teachers

#### ✅ Do:
- Run all graders on student submissions
- Trust the automated grading (it's thorough)
- Use marksheet.md for quick overview
- Spot-check suspicious patterns (all tasks passed suddenly)
- Review Git commit history for authentic progression

#### ❌ Don't:
- Accept score files without running graders yourself
- Trust manually edited `points.json` files
- Grade based on file existence alone
- Skip running the graders (they catch everything)

### 10. Example Grading Session

```bash
# Teacher receives submission
$ git clone https://github.com/student/pythonpro26.git
$ cd pythonpro26

# Run all graders (takes ~30 seconds)
$ for part in 1 2 3 4 5 6; do 
    python part${part}/part${part}Exercises/tasks/grade_part${part}.py
  done

# Check final results
$ cat .progress/marksheet.md

# Output shows:
# Total points: 87/143
# Grade: 2 (60.8%)
# 
# Part 1: 28/31
# Part 2: 20/22
# Part 3: 18/34
# Part 4: 15/37
# Part 5: 12/25 (optional, not counted)
# Part 6: 6/19
```

## Summary

The grading system is designed with academic integrity in mind:

1. ✅ **Implementation verification** - no credit for empty files
2. ✅ **Live evaluation** - scores reflect current code state
3. ✅ **Automatic recalculation** - manual score edits are overwritten
4. ✅ **Transparent feedback** - students see "(no implementation)" when appropriate
5. ✅ **Easy teacher workflow** - just run the graders on submitted repos

**Bottom line:** Students must have actual working code to receive points. The system is manipulation-resistant and requires minimal teacher intervention beyond running the automated graders.
