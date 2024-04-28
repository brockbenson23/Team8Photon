@echo off

REM Prompt user for commit message
set /p commit_message=Enter commit message:

REM Add all changes
git add .

REM Commit changes with the provided message
git commit -m "%commit_message%"

REM Push changes to the remote repository
git push -u origin

