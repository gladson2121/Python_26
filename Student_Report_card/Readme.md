# Student Report Card Generator

This project creates a student report card by taking each student's ID, name, and subject marks, storing them in a dictionary, calculating the average and grade, and printing a formatted report card for each student.

## Features

- Input student ID, name, and marks for each subject
- Store student data in a dictionary
- Calculate total marks and average
- Assign a grade based on performance
- Print a neatly formatted student report card
- Repeat the process for multiple students

## Project Goal

The main purpose of this project is to simplify the process of preparing academic results. Instead of calculating marks manually, the program automatically stores student marks, evaluates their performance, and prints a clean report card.

## Requirements

- Python 3.x
- Basic understanding of dictionaries, loops, and functions

## How It Works

1. Enter the student ID and name.
2. Enter marks for each subject.
3. Store the marks in a dictionary.
4. Calculate the average using the marks entered.
5. Assign a grade based on the average.
6. Display the formatted report card.

## Example Logic

```python
student = {
    "student_id": 101,
    "name": "Aisha",
    "marks": {
        "Math": 85,
        "Science": 90,
        "English": 80,
        "Computer": 88,
    }
}
```

## Example Output

```text
====================================
           STUDENT REPORT CARD
====================================
Student ID: 101
Student Name: Aisha

Subject Marks:
Math      : 85
Science   : 90
English   : 80
Computer  : 88

Average   : 85.75
Grade     : A
====================================
```

## Typical Grade Rules

- 90 - 100: A
- 80 - 89: B
- 70 - 79: C
- 60 - 69: D
- Below 60: F

## Project Structure

```text
Student_Report_card/
|-- main.py
|-- README.md
```

## License

This project is intended for learning and academic practice.
