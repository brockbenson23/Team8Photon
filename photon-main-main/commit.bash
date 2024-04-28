#!/bin/bash

# Prompt user for commit message
echo "Enter commit message:"
read commit_message

git add .
git commit -m "$commit_message"
git push -u origin
