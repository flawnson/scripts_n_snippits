#!/bin/bash

# TODO: Write script for using Github API to create new repositories through CLI

echo "Paste link to repo here (be sure to check for visibility)"
read REPO_LINK

# Change remote origin/upstream url to the newly created repo
git remote set-url origin REPO_LINK

# Pull with permission to merge unrelated histories (may fail if README.d is not consistent)
git pull --allow-unrelated-histories

# Clear README.md (must manually fix later)
rm README.md
touch README.md

# Adding empty README.md to new repo
git add README.md
git commit -m "Fixed README.md for first commit"
git push

echo "Redirect of repo completed"

