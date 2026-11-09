# CLI App Project Overview

My project is a command line quiz game where users can play quizzes, take their pick at a subject, and view their highscores for each subject.

## Key Features and Usage

When the CLI App is run, the user is shown an menu of options and is prompted to "Choose an option (1-4)". The options are:

1. Start Quiz
2. View High Scores
3. Choose Subject
4. Quit

## Setup

**To start, follow these steps:**

```sh
git clone git@github.com:jacgordon/CLI-Application-Project-Quiz-Game.git
cd CLI-Application-Project-Quiz-Game

# Create a virtual environment in a folder named .venv, then turn it on
python3 -m venv .venv
source .venv/bin/activate

# Install pytest into the virtual environment
pip install pytest

# Run the application
python3 src/main.py

# If you need to end the program abruptly, use Control+C
```


This file is yours to write. When your project works, replace everything here
with a description of what you built: what it does, how to run it, and a usage
example. Write it for someone who has never seen your project before.

For an example of what a finished one looks like, see the
[Task Manager Case Study](https://github.com/The-Marcy-Lab-School/swe-casestudy-1-cli-task-manager),
which is a working Python CLI app with investigation questions to work
through.
