# 🖥️ Local Development Setup Guide

This guide will walk you through setting up a complete local development environment for this Python course on **Windows** or **macOS**.

> **Note:** You may already have VS Code installed, logged in with GitHub, and Python installed locally. Depending on your situation, some or all of the following steps may not be required. You can complete all tasks using [GitHub Codespaces](.devcontainer/README.md) directly in your browser, especially for the first part of the course. However, we recommend setting up a local environment as well for a better learning experience and offline access.
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
---

### 🍎 MacOS

#### Using Official Installer

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

---

## 2. Install Git

Git is required for version control and cloning this repository.

### 🪟 Windows

#### Git for Windows 

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

---

### 🍎 MacOS

####  Using Xcode Command Line Tools (Simplest)

1. **Install:**
   ```bash
   xcode-select --install
   ```
   - A popup will appear - click **"Install"**

2. **Verify:**
   ```bash
   git --version
   ```

---

### Configure Git (All Platforms)

After installing, set your name and email:

```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

---

## 3. Install GitHub Desktop (Optional)

GitHub Desktop provides a visual interface for Git. **This is optional**. You can use command line Git instead.

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

### 🍎 MacOS

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

Now that you have Git and VS Code set up, let's clone your exercise repository to your local device.

### Clone Using VS Code Terminal 

This method uses the command line directly in VS Code.

1. **Get Your Repository URL:**
   - Go to your GitHub repository in a web browser
   - Click the green **"<> Code"** button
   - Select **HTTPS** tab
   - Click the copy icon to copy the URL
   - It should look like: `https://github.com/YOUR-USERNAME/REPO-NAME.git`

2. **Open VS Code:**
   - Launch Visual Studio Code

3. **Open the Terminal:**
   - Press `` Ctrl+` `` (backtick key) or
   - Go to **Terminal → New Terminal** from the menu

4. **Navigate to Your Desired Location:**
   
   Choose where you want to store your project:
   
   **Windows:**
   ```powershell
   # Navigate to your desired folder (e.g., Documents)
   cd $HOME\Documents
   
   # Or create a dedicated folder for your repos
   cd $HOME\Documents
   mkdir GitRepos
   cd GitRepos
   ```
   
   **macOS/Linux:**
   ```bash
   # Navigate to your desired folder (e.g., Documents)
   cd ~/Documents
   
   # Or create a dedicated folder for your repos
   mkdir -p ~/Documents/GitRepos
   cd ~/Documents/GitRepos
   ```

5. **Clone the Repository:**
   ```bash
   git clone https://github.com/YOUR-USERNAME/REPO-NAME.git
   ```
   
   **Example:**
   ```bash
   git clone https://github.com/dipaish/pythonpro26Assignment.git
   ```
   
   You should see output like:
   ```
   Cloning into 'pythonpro26Assignment'...
   remote: Enumerating objects: 150, done.
   remote: Counting objects: 100% (150/150), done.
   remote: Compressing objects: 100% (120/120), done.
   remote: Total 150 (delta 25), reused 140 (delta 20), pack-reused 0
   Receiving objects: 100% (150/150), 45.20 KiB | 2.26 MiB/s, done.
   Resolving deltas: 100% (25/25), done.
   ```

6. **Open the Cloned Repository:**
   ```bash
   code REPO-NAME
   ```
   
   **Example:**
   ```bash
   code pythonpro26Assignment
   ```
   
   This will open the repository in a new VS Code window.


### ✅ Verify the Clone

After cloning, verify the repository structure:

1. **In VS Code Explorer** (left sidebar), you should see:
   ```
   📁 pythonpro26Assignment/
   ├── 📁 part1/
   ├── 📁 part2/
   ├── 📁 part3/
   ├── 📄 README.md
   ├── 📄 LOCAL_SETUP_GUIDE.md
   └── ...
   ```

2. **In Terminal, check Git status:**
   ```bash
   git status
   ```
   
   Should show:
   ```
   On branch main
   Your branch is up to date with 'origin/main'.
   
   nothing to commit, working tree clean
   ```

### 🔄 Keeping Your Local Repository Updated

To get the latest changes from GitHub:

```bash
# Pull latest changes
git pull
```

To push your local changes to GitHub:

```bash
# Add all changed files
git add .

# Commit with a message
git commit -m "Completed task 1"

# Push to GitHub
git push
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

- Ask your instructor
---

**Happy Coding! 🎉**
