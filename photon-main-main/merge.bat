@echo off

REM Prompt user for branch name to merge
set /p branch_name=Enter the name of the branch to merge with main:

REM Check if branch name is provided
if "%branch_name%"=="" (
    echo Error: Branch name cannot be empty.
    exit /b 1
)

REM Check if branch exists
git show-ref --verify --quiet "refs/heads/%branch_name%" > nul 2>&1
if %errorlevel% neq 0 (
    echo Error: Branch '%branch_name%' does not exist.
    exit /b 1
)

REM Inform user about the merge process
echo Pulling changes from main branch...
git checkout main
git pull origin main

echo Merging branch '%branch_name%' into main...
git merge "%branch_name%"

echo Pushing changes to main branch...
git push -u origin main

echo Merge completed successfully.

