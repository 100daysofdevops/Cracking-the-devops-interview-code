#!/bin/sh

# Regular expression to search for 'WorkItem: [number]'
PATTERN="WorkItem: [0-9]+"

# Read the commit message from the file provided by Git
COMMIT_MSG_FILE=$1
COMMIT_MSG=$(cat $COMMIT_MSG_FILE)

# Check if the commit message matches the pattern
if ! echo "$COMMIT_MSG" | grep -qE "$PATTERN"; then
  echo "ERROR: Commit message does not contain a work item."
  echo "Please include a work item in the format 'WorkItem: 123'."
  exit 1
fi

exit 0
