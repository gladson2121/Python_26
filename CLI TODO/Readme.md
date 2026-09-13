# CLI TODO App

A simple command-line TODO application written in Python. The app lets you add,
view, update, complete, and delete tasks from an interactive menu.

## Features

- Add a task with a title and description
- View all tasks and their current status
- Update a task's title, description, or status
- Mark a task as complete
- Delete a task
- Exit through the application menu

## Requirements

- Python 3.10 or newer

The application uses Python structural pattern matching (`match` and `case`),
which requires Python 3.10 or newer.

## Getting Started

1. Open a terminal in the project directory:

	```text
	ClI TODO
	```

2. Run the application:

	```bash
	python todo.py
	```

	On some systems, use:

	```bash
	python3 todo.py
	```

3. Choose an option from the menu and follow the prompts.

## Menu Options

| Option | Action |
| --- | --- |
| 1 | Add a new task |
| 2 | View all tasks |
| 3 | Update an existing task |
| 4 | Delete a task |
| 5 | Mark a task as complete |
| 6 | Exit the application |

## Data Storage

Tasks are stored in memory while the application is running. They are not saved
to a file or database, so all tasks are lost when the application exits.

## Project Structure

```text
ClI TODO/
|-- todo.py
|-- Readme.md
```

## License

This project is intended for learning and personal use.
