# 🖥️ Local Development Setup Guide

This guide will walk you through setting up a complete local development environment for this Python course on **Windows**, **macOS**, or **Linux**.

> **💡 Don't want to install anything?** Use [GitHub Codespaces](https://github.com/dipaish/pythonpro26/tree/main/.devcontainer) instead! It's free, browser-based, and requires zero setup.

---

## 📋 Table of Contents

1. [Install Python](#1-install-python)
2. [Install Git](#2-install-git)
3. [Install GitHub Desktop (Optional)](#3-install-github-desktop-optional)
4. [Install Visual Studio Code](#4-install-visual-studio-code)
5. [Setup VS Code for Python](#5-setup-vs-code-for-python)
6. [Sign in with GitHub Account](#6-sign-in-with-github-account)
7. [Clone This Repository](#7-clone-this-repository)
8. [Verify Your Setup](#8-verify-your-setup)
9. [Troubleshooting](#9-troubleshooting)

---

## 1. Install Python

You need **Python 3.11 or higher** for this course.

### 🪟 Windows

1. **Download Python:**
   - Visit [python.org/downloads](https://www.python.org/downloads/)
   - Click **"Download Python 3.11.x"** (or newer version)

2. **Run the Installer:**
   - ✅ **IMPORTANT:** Check **"Add Python to PATH"** at the bottom of the installer
   - Click **"Install Now"**
   - Wait for installation to complete

3. **Verify Installation:**
   ```powershell
   python --version
   ```
   Should show: `Python 3.11.x` or higher

### 🍎 macOS

#### Option A: Using Official Installer (Recommended for Beginners)

1. **Download Python:**
   - Visit [python.org/downloads](https://www.python.org/downloads/)
   - Click **"Download Python 3.11.x"** (or newer)

2. **Run the Installer:**
   - Open the downloaded `.pkg` file
   - Follow the installation wizard
   - Click **"Install"** and enter your password when prompted

3. **Verify Installation:**
   ```bash
   python3 --version
   ```
   Should show: `Python 3.11.x` or higher

#### Option B: Using Homebrew (For Advanced Users)

1. **Install Homebrew** (if not already installed):
   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```

2. **Install Python:**
   ```bash
   brew install python@3.11
   ```

3. **Verify:**
   ```bash
   python3 --version
   ```

### 🐧 Linux (Ubuntu)

1. **Update package list:**
   ```bash
   sudo apt update
   ```

2. **Install Python 3.11:**
   ```bash
   sudo apt install python3.11 python3.11-venv python3-pip
   ```

3. **Verify:**
   ```bash
   python3.11 --version
   ```

---

## 2. Install Git

Git is required for version control and cloning this repository.

### 🪟 Windows

#### Option A: Git for Windows (Recommended)

1. **Download:**
   - Visit [git-scm.com/download/win](https://git-scm.com/download/win)
   - Download will start automatically

2. **Run Installer:**
   - Use **default settings** (just click "Next" through all screens)
   - Key settings to note:
     - Default editor: VS Code (if already installed) or Vim
     - PATH environment: "Git from the command line and also from 3rd-party software"
     - Line ending conversions: "Checkout Windows-style, commit Unix-style"

3. **Verify:**
   ```powershell
   git --version
   ```

#### Option B: Via Package Manager (Advanced)

Using **Chocolatey**:
```powershell
choco install git
```

Using **Winget**:
```powershell
winget install Git.Git
```

### 🍎 macOS

#### Option A: Using Xcode Command Line Tools (Simplest)

1. **Install:**
   ```bash
   xcode-select --install
   ```
   - A popup will appear - click **"Install"**

2. **Verify:**
   ```bash
   git --version
   ```

#### Option B: Using Homebrew

1. **Install:**
   ```bash
   brew install git
   ```

2. **Verify:**
   ```bash
   git --version
   ```

### 🐧 Linux (Ubuntu)

```bash
sudo apt update
sudo apt install git
```

**Verify:**
```bash
git --version
```

### Configure Git (All Platforms)

After installing, set your name and email:

```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

---

## 3. Install GitHub Desktop (Optional)

GitHub Desktop provides a visual interface for Git. **This is optional** - you can use command-line Git instead.

### 🪟 Windows & 🍎 macOS

1. **Download:**
   - Visit [desktop.github.com](https://desktop.github.com/)
   - Click **"Download for Windows"** or **"Download for macOS"**

2. **Install:**
   - **Windows:** Run the downloaded `.exe` file
   - **macOS:** Drag the app to your Applications folder

3. **Sign In:**
   - Open GitHub Desktop
   - Click **"Sign in to GitHub.com"**
   - Authorize in your browser
   - Return to GitHub Desktop

### 🐧 Linux (Ubuntu)

GitHub Desktop is not officially supported on Linux. Ubuntu users can use:

- **Command-line Git** (recommended - already installed in Step 2)
- **GitKraken:** [gitkraken.com](https://www.gitkraken.com/) (free for public repos)
- **GitAhead:** [gitahead.github.io/gitahead.com](https://gitahead.github.io/gitahead.com/) (open source)

---

## 4. Install Visual Studio Code

### 🪟 Windows

1. **Download:**
   - Visit [code.visualstudio.com](https://code.visualstudio.com/)
   - Click **"Download for Windows"**

2. **Install:**
   - Run the downloaded installer
   - ✅ Check **"Add to PATH"** (important!)
   - ✅ Check **"Create a desktop icon"** (optional)
   - ✅ Check **"Add 'Open with Code' action to context menu"** (recommended)

3. **Verify:**
   - Open Command Prompt or PowerShell
   ```powershell
   code --version
   ```

### 🍎 macOS

1. **Download:**
   - Visit [code.visualstudio.com](https://code.visualstudio.com/)
   - Click **"Download for Mac"**

2. **Install:**
   - Open the downloaded `.zip` file
   - Drag **Visual Studio Code** to your **Applications** folder

3. **Add to PATH:**
   - Open VS Code
   - Press `Cmd+Shift+P` (Command Palette)
   - Type: `Shell Command: Install 'code' command in PATH`
   - Press Enter

4. **Verify:**
   ```bash
   code --version
   ```

### 🐧 Linux (Ubuntu)

1. **Install via Snap (Easiest):**
   ```bash
   sudo snap install --classic code
   ```

2. **Or via APT:**
   ```bash
   # Add Microsoft GPG key and repository
   wget -qO- https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > packages.microsoft.gpg
   sudo install -D -o root -g root -m 644 packages.microsoft.gpg /etc/apt/keyrings/packages.microsoft.gpg
   sudo sh -c 'echo "deb [arch=amd64,arm64,armhf signed-by=/etc/apt/keyrings/packages.microsoft.gpg] https://packages.microsoft.com/repos/code stable main" > /etc/apt/sources.list.d/vscode.list'
   
   # Install
   sudo apt update
   sudo apt install code
   ```

**Verify:**
```bash
code --version
```

---

## 5. Setup VS Code for Python

### Install Essential Extensions

1. **Open VS Code**

2. **Open Extensions View:**
   - Press `Ctrl+Shift+X` (Windows/Linux) or `Cmd+Shift+X` (macOS)
   - Or click the Extensions icon in the sidebar

3. **Install These Extensions:**

   Search and install each one:

   | Extension | Publisher | Description |
   |-----------|-----------|-------------|
   | **Python** | Microsoft | Essential Python support |
   | **Pylance** | Microsoft | Fast Python language server |
   | **Python Debugger** | Microsoft | Debugging support |
   | **Python Indent** | Kevin Rose | Better auto-indentation |
   | **autoDocstring** | Nils Werner | Generate docstrings |
   | **Python Environment Manager** | Don Jayamanne | Manage Python environments |

4. **Optional but Recommended:**

   | Extension | Publisher | Description |
   |-----------|-----------|-------------|
   | **GitHub Copilot** | GitHub | AI code assistant (free for students!) |
   | **GitLens** | GitKraken | Enhanced Git features |
   | **Error Lens** | Alexander | Inline error messages |
   | **Material Icon Theme** | Philipp Kief | Better file icons |

### Configure Python Settings

1. **Open Settings:**
   - Press `Ctrl+,` (Windows/Linux) or `Cmd+,` (macOS)

2. **Add These Settings:**

   Click the **"Open Settings (JSON)"** icon in the top right, then add:

   ```json
   {
       "editor.fontSize": 14,
       "editor.tabSize": 4,
       "editor.insertSpaces": true,
       "files.autoSave": "afterDelay",
       "files.autoSaveDelay": 1000,
       "python.languageServer": "Pylance",
       "python.analysis.typeCheckingMode": "basic",
       "python.terminal.activateEnvironment": true,
       "editor.formatOnSave": false,
       "[python]": {
           "editor.defaultFormatter": "ms-python.python",
           "editor.tabSize": 4
       }
   }
   ```

---

## 6. Sign in with GitHub Account

Signing in syncs your settings and enables GitHub features.

### In VS Code:

1. **Click the Account Icon:**
   - Bottom-left corner of VS Code
   - Or look for "Accounts" in the sidebar

2. **Click "Sign in to Sync Settings"**

3. **Choose "Sign in with GitHub"**

4. **Authorize in Browser:**
   - Browser will open
   - Click **"Authorize Visual-Studio-Code"**
   - Return to VS Code

### Benefits:

- ✅ Sync settings across devices
- ✅ Access GitHub Copilot (if eligible)
- ✅ Clone private repositories
- ✅ Create/manage pull requests

---

## 7. Clone This Repository

Now you're ready to get the course files!

### Method A: Using VS Code (Recommended)

1. **Open VS Code**

2. **Open Command Palette:**
   - Press `Ctrl+Shift+P` (Windows/Linux) or `Cmd+Shift+P` (macOS)

3. **Type:** `Git: Clone`

4. **Enter Repository URL:**
   ```
   https://github.com/YOUR_USERNAME/pythonpro26.git
   ```
   *(Replace `YOUR_USERNAME` with the actual repository owner)*

5. **Choose Location:**
   - Select where to save the repository
   - Recommended: Create a `GitRepos` or `Projects` folder

6. **Open Repository:**
   - VS Code will ask "Would you like to open the cloned repository?"
   - Click **"Open"**

### Method B: Using GitHub Desktop

1. **Open GitHub Desktop**

2. **File → Clone Repository**

3. **Enter URL:**
   ```
   https://github.com/YOUR_USERNAME/pythonpro26.git
   ```

4. **Choose Local Path** and click **"Clone"**

5. **Open in VS Code:**
   - Click **"Open in Visual Studio Code"**

### Method C: Using Command Line

1. **Open Terminal** (or Command Prompt/PowerShell on Windows)

2. **Navigate to desired location:**
   ```bash
   cd ~/Documents  # or wherever you want
   ```

3. **Clone:**
   ```bash
   git clone https://github.com/YOUR_USERNAME/pythonpro26.git
   ```

4. **Open in VS Code:**
   ```bash
   cd pythonpro26
   code .
   ```

---

## 8. Verify Your Setup

Let's make sure everything works!

### Test 1: Python is Working

1. **Open Terminal in VS Code:**
   - Press `` Ctrl+` `` (backtick) or go to **Terminal → New Terminal**

2. **Check Python version:**
   ```bash
   # Windows:
   python --version
   
   # macOS/Linux:
   python3 --version
   ```
   
   Should show `Python 3.11.x` or higher

### Test 2: Run a Simple Task

1. **Navigate to Part 1:**
   ```bash
   cd part1/part1Exercises/tasks
   ```

2. **Run a task:**
   ```bash
   # Windows:
   python 1_emoticon.py
   
   # macOS/Linux:
   python3 1_emoticon.py
   ```

3. **Expected Output:**
   ```
   :-()
   ```

### Test 3: Run the Grader

1. **Run Part 1 grader:**
   ```bash
   # Windows:
   python grade_part1.py
   
   # macOS/Linux:
   python3 grade_part1.py
   ```

2. **Check Progress:**
   - Open `.progress/marksheet.md` to see your scores

### Test 4: Python Extension Works

1. **Open any `.py` file**

2. **Check Bottom-Right Corner:**
   - Should show Python version (e.g., "Python 3.11.5")
   - If it says "Select Python Interpreter," click it and choose one

3. **Hover Over Code:**
   - Hover over `print` - should show documentation popup
   - If not, Pylance might still be loading (wait 10-20 seconds)

---

## 9. Troubleshooting

### ❌ Python Not Found

**Error:** `'python' is not recognized as an internal or external command`

**Solution:**

- **Windows:**
  - Reinstall Python with **"Add to PATH"** checked
  - Or manually add to PATH: [Guide](https://realpython.com/add-python-to-path/)

- **macOS/Linux:**
  - Use `python3` instead of `python`
  - Or create an alias: `alias python=python3`

### ❌ VS Code Can't Find Python

**Problem:** VS Code shows "Select Python Interpreter"

**Solution:**

1. Press `Ctrl+Shift+P` (or `Cmd+Shift+P`)
2. Type: `Python: Select Interpreter`
3. Choose the Python 3.11+ version from the list

### ❌ Git Commands Don't Work

**Error:** `'git' is not recognized`

**Solution:**

- Restart VS Code/Terminal after installing Git
- On Windows, make sure you selected "Add to PATH" during install
- Check if installed: `git --version`

### ❌ Extensions Not Loading

**Problem:** Python extension installed but not working

**Solution:**

1. **Reload VS Code:**
   - Press `Ctrl+Shift+P` → `Developer: Reload Window`

2. **Check Extension Status:**
   - Extensions panel → Look for errors
   - Click gear icon → "Extension Settings"

3. **Reinstall Extension:**
   - Right-click extension → "Uninstall"
   - Restart VS Code
   - Reinstall from Extensions marketplace

### ❌ Permission Errors (macOS/Ubuntu)

**Error:** `Permission denied` when running Python/pip

**Solution:**

- **Don't use `sudo` with pip!**
- Use: `python3 -m pip install --user package_name`
- Or create a virtual environment:
  ```bash
  python3 -m venv .venv
  source .venv/bin/activate
  ```

### ❌ Auto-Save Not Working

**Problem:** Changes not saving automatically

**Solution:**

1. Go to: **File → Preferences → Settings**
2. Search: `auto save`
3. Set to: **afterDelay**
4. Set delay: **1000** ms

### ❌ Grader Shows "FAIL (no implementation)"

**Problem:** All tasks fail even though you wrote code

**Cause:** Your code might be in comments or not actually implementing the logic

**Solution:**

- Make sure your code is **outside** the docstring quotes
- Remove `pass` statements
- Actually implement the function logic
- See [setup_new_part_prompt.md](setup_new_part_prompt.md) for details

---

## 🎓 Next Steps

Now that your environment is set up:

1. **Read the [Main README](https://github.com/dipaish/pythonpro26#readme)** for course overview
2. **Start with [Part 1](part1.md)**
3. **Run tasks:** `python task_name.py`
4. **Check progress:** `python grade_part1.py`
5. **Track scores:** Open `.progress/marksheet.md`

---

## 💡 Tips

- **Use VS Code's integrated terminal** - It's already in the right directory!
- **Learn keyboard shortcuts:**
  - Run Python file: `Ctrl+Shift+P` → `Python: Run Python File in Terminal`
  - Toggle terminal: `` Ctrl+` ``
  - Open file quickly: `Ctrl+P`
- **Install GitHub Copilot** if you're a student (free!) - [Education benefits](https://education.github.com/)
- **Use Git regularly:**
  - Commit after each completed task: `git commit -m "Completed task X"`
  - Push to GitHub: `git push`

---

## 📚 Additional Resources

- [Python Official Tutorial](https://docs.python.org/3/tutorial/)
- [VS Code Python Documentation](https://code.visualstudio.com/docs/python/python-tutorial)
- [Git Handbook](https://guides.github.com/introduction/git-handbook/)
- [VS Code Keyboard Shortcuts](https://code.visualstudio.com/shortcuts/keyboard-shortcuts-windows.pdf)

---

## 🆘 Still Having Issues?

- Check [GitHub Issues](https://github.com/dipaish/pythonpro26/issues)
- Ask your instructor
- Or try [GitHub Codespaces](https://github.com/dipaish/pythonpro26/tree/main/.devcontainer) - zero setup required!

---

**Happy Coding! 🎉**
