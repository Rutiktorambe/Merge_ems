Setting up Git on Windows 11 and learning basic Git commands (clone, pull, commit, push) involves the following steps:

---

### 1. **Install Git**

1. **Download Git**:

   - Go to the [official Git website](https://git-scm.com/).
   - Download the latest Git version for Windows.

2. **Install Git**:

   - Run the downloaded installer.
   - During installation:
     - Choose the editor you'd like to use (e.g., Vim, VS Code, etc.).
     - Opt for the default settings unless you need something specific.

3. **Verify installation**:
   - Open **Command Prompt** or **PowerShell**.
   - Type: `git --version`
   - You should see the installed Git version.

---

### 2. **Configure Git**

Before using Git, configure your user details:

```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

To verify the configuration:

```bash
git config --list
```

---

### 3. **Clone a Repository**

To clone a repository:

1. Copy the repository URL (from GitHub, GitLab, etc.).
2. Open the terminal and run:

```bash
git clone <repository_url>
```

Example:

```bash
git clone https://github.com/username/repository.git
```

---

### 4. **Pull Changes**

To fetch and merge updates from the remote repository:

```bash
git pull origin <branch_name>
```

Example:

```bash
git pull origin main
```

---

### 5. **Add Changes**

After modifying files in the repository:

1. Check the status of changes:

   ```bash
   git status
   ```

2. Stage the changes:

   ```bash
   git add <file_name>
   ```

   Or stage all changes:

   ```bash
   git add .
   ```

---

### 6. **Commit Changes**

Save your staged changes with a message:

```bash
git commit -m "Your commit message"
```

---

### 7. **Push Changes**

Upload your commits to the remote repository:

```bash
git push origin <branch_name>
```

Example:

```bash
git push origin main
```

---

### 8. **Create a Pull Request (PR)**

If you're collaborating on GitHub:

1. Push your branch to the repository.
2. Go to the repository page on GitHub.
3. Navigate to the **Pull Requests** tab.
4. Click **New Pull Request** and follow the instructions.

---

### 9. **Basic Workflow Summary**

1. Clone the repository: `git clone <url>`
2. Make changes to files.
3. Stage changes: `git add .`
4. Commit changes: `git commit -m "message"`
5. Pull the latest changes: `git pull origin <branch>`
6. Push your changes: `git push origin <branch>`

This workflow helps you keep your code synchronized with the team and the remote repository. Let me know if you need further clarification!
