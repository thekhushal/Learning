# LinuxBridge Setup Reference

## Objective

Create simple shell commands to quickly transfer files between WSL (Linux) and Windows without repeatedly typing long file paths.

---

# 1. Windows Folder Created

Created a shared folder on Windows:

```text
C:\Non_System_Files\Workspace\LinuxBridge
```

This acts as a bridge between Windows and WSL.

Its WSL path is:

```bash
/mnt/c/Non_System_Files/Workspace/LinuxBridge
```

---

# 2. Bash Configuration

Since I work as the **root** user in WSL, all configuration was done under `/root`.

### File modified

```bash
/root/.bashrc
```

### Change made

Added the following line:

```bash
source ~/.bash_functions
```

Purpose:

Every new Bash terminal automatically loads all custom shell functions defined in `.bash_functions`.

Whenever `.bash_functions` is edited, reload it using:

```bash
source ~/.bashrc
```

---

# 3. Custom Functions File

Created a new file:

```bash
/root/.bash_functions
```

This file contains all of my personal shell commands.

The idea is that any future utility I create can simply be added here.

---

# 4. Current Utility

Created two custom commands:

## Push

Copies (or moves) files from the current Linux directory to LinuxBridge.

Examples:

```bash
push report.pdf
push image.png notes.txt
push *.ipynb
push MyProject
push --move report.pdf
```

---

## Pull

Copies (or moves) files from LinuxBridge back into the current Linux directory.

Examples:

```bash
pull report.pdf
pull *.png
pull MyProject
pull --move report.pdf
```

---

# 5. Features

Current implementation supports:

* Single file
* Multiple files
* Wildcards (`*.txt`)
* Directories
* Copy
* Move (`--move`)
* Success/error messages
* Summary of completed operations

---

# 6. Current `.bashrc` Change

```bash
source ~/.bash_functions
```

---

# 7. Current `.bash_functions`

```bash
# Shared path
LINUX_BRIDGE="/mnt/c/Non_System_Files/Workspace/LinuxBridge"

push() {
    local operation="cp"

    if [[ "$1" == "--move" ]]; then
        operation="mv"
        shift
    fi

    if [[ $# -eq 0 ]]; then
        echo "Usage: push [--move] <file|folder>..."
        return 1
    fi

    local success=0
    local failed=0

    for item in "$@"; do
        if [[ ! -e "$item" ]]; then
            echo "❌ '$item' not found"
            ((failed++))
            continue
        fi

        if [[ -d "$item" && "$operation" == "cp" ]]; then
            cp -r "$item" "$LINUX_BRIDGE"
        else
            "$operation" "$item" "$LINUX_BRIDGE"
        fi

        if [[ $? -eq 0 ]]; then
            echo "✓ $(basename "$item")"
            ((success++))
        else
            echo "❌ $(basename "$item")"
            ((failed++))
        fi
    done

    echo
    echo "$success succeeded, $failed failed."
}

pull() {
    local operation="cp"

    if [[ "$1" == "--move" ]]; then
        operation="mv"
        shift
    fi

    if [[ $# -eq 0 ]]; then
        echo "Usage: pull [--move] <file|folder>..."
        return 1
    fi

    local success=0
    local failed=0

    for item in "$@"; do
        if [[ ! -e "$LINUX_BRIDGE/$item" ]]; then
            echo "❌ '$item' not found in LinuxBridge"
            ((failed++))
            continue
        fi

        if [[ -d "$LINUX_BRIDGE/$item" && "$operation" == "cp" ]]; then
            cp -r "$LINUX_BRIDGE/$item" .
        else
            "$operation" "$LINUX_BRIDGE/$item" .
        fi

        if [[ $? -eq 0 ]]; then
            echo "✓ $(basename "$item")"
            ((success++))
        else
            echo "❌ $(basename "$item")"
            ((failed++))
        fi
    done

    echo
    echo "$success succeeded, $failed failed."
}
```

---

# 8. Future Improvements

Potential additions:

* `bridge ls` — list bridge contents
* `bridge clear` — empty bridge
* `bridge size` — show bridge size
* `bridge path` — print bridge location
* `bridge open` — open bridge directory
* Replace `cp` with `rsync` for copy operations
* Add `--help`
* Add tab completion

---

# 9. Context for Future ChatGPT Conversations

If I paste this document into a new chat, ChatGPT should understand that:

* I use WSL as the root user.
* My custom shell functions live in `/root/.bash_functions`.
* They are loaded from `/root/.bashrc` using `source ~/.bash_functions`.
* I created a Windows/Linux shared folder at `C:\Non_System_Files\Workspace\LinuxBridge`.
* The `push` and `pull` commands are my personal utilities for transferring files between WSL and Windows.
* Any future work should extend this toolkit rather than replacing it.
