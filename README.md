# Github-Automation

## About This Project :books:
This script allows user to completely automate github workflow. This script keeps track of changed files and generates a diff, then auto adds and commits(asks for a commit message) the changed files.

## Features :sparkles:

- Auto fetches repository info(uri , working branch) from local dir
- Keeps track of changed files
- Adds changed file,diff to json file
- Calculates diff for changed files
- Auto performs git commands for changed files(Need to pass commit messages)
- Auto performs git commands for uncommited files on script startup

## How To Run :runner:

To run the script use following commands

1. Get all the requirements
    ```bash
    pip install -r ./requirements.txt
    ```
2. Run the installation script
    ```bash
    python3 install.py
    ```
3. Enter the project directory where changes are to be listened
    ```bash
    Enter installation directory: project_dir
    ```
4. goto your project directory
    ```bash
    cd project_dir
    ```

5. Run the python script to listen for changes
    ```python
    python3 ./auto-scripts/main.py
    ```

***Note:** This script listens to all nested files, ignoring all the directories and files present in .gitignore. If you want to add custom folders that you want the script to ignore add them in .gitignore. **Add all build directories or any directory that contains modules like: node_modules to .gitignore***

