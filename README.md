# PrepTrack — Placement Preparation Performance Analyzer

## Overview

PrepTrack is a Python-based student placement readiness assessment system. It evaluates a student's practice performance, attendance, project completion status, and profile verification details to determine whether the student is ready for a placement mock interview.

The application collects student information, validates inputs, processes seven days of coding practice scores, generates performance statistics, and provides a final placement-readiness decision with recommendations.

---

## Features

### Student Information Management

* Student Name Validation
* Registration Number Input
* Graduation Year Validation
* Attendance Validation
* Project Completion Verification
* Profile Verification

### Practice Score Processing

* Processes scores for 7 practice days
* Supports absent days using `-1`
* Validates score inputs
* Calculates:

  * Attempted Days
  * Absent Days
  * Passed Days
  * Failed Days

### Performance Classification

Each attempted score is classified as:

| Score Range | Classification    |
| ----------- | ----------------- |
| 75 – 100    | Strong            |
| 60 – 74     | Satisfactory      |
| 40 – 59     | Needs Improvement |
| 0 – 39      | Critical          |

### Performance Analysis

* Total Score Calculation
* Average Score Calculation
* Highest Score Identification
* Lowest Score Identification
* First Critical Score Tracking

### Placement Readiness Evaluation

The application checks:

* Eligible Graduation Year (2025–2027)
* Attendance ≥ 75%
* At least 6 Practice Attempts
* Average Score ≥ 70
* No Critical Scores
* At Least 4 Passed Practices
* Project Completed
* Profile Verified

### Final Decision System

Displays:

* Final Status
* Primary Blocker
* Recommended Next Action

---

## Technologies Used

* Python 3
* Loops (`for`, `while`)
* Conditional Statements (`if`, `elif`, `else`)
* Boolean Expressions
* Counters and Accumulators
* Input Validation

---

## Project Structure

```text
PrepTrack/
│
├── preptrack.py
├── README.md
```

---

## Sample Execution

```text
==================================================
              PREPTRACK APPLICATION
==================================================

Enter student name: Ananya Sharma
Enter registration number: PY24038
Enter graduation year: 2026
Enter attendance percentage: 82

Has the student completed the required project?
Enter yes or no: yes

Is the student profile verified?
Enter yes or no: yes

Enter Day 1 score from 0 to 100, or -1 for absent: 80
Day 1 Result: Strong
```

---

## Placement Readiness Criteria

A student is considered **Ready for Mock Interview** only when all the following conditions are satisfied:

* Graduation Year between 2025 and 2027
* Attendance ≥ 75%
* Attempted Days ≥ 6
* Average Score ≥ 70
* No Critical Scores
* Passed Days ≥ 4
* Project Completed
* Profile Verified

---

## Output Report

The generated report includes:

### Student Profile

* Student Name
* Registration Number
* Graduation Year
* Attendance
* Project Status
* Profile Verification Status

### Practice Summary

* Total Practice Days
* Attempted Days
* Absent Days
* Passed Days
* Failed Days

### Performance Analysis

* Total Score
* Average Score
* Highest Score
* Lowest Score

### Critical Score Information

* Critical Score Found
* First Critical Day
* First Critical Score

### Final Decision

* Final Status
* Primary Blocker
* Next Action

---

## Learning Outcomes

This project demonstrates:

* Input Validation
* Looping Structures
* Conditional Logic
* Boolean Expressions
* Data Processing
* Performance Analysis
* Report Generation
* Problem Solving using Python

# Individual Contribution

**Name:** Anusha Chakkirala

**Repository URL:** [https://github.com/anushachakkirala/preptrack-anushachakkirala]

**My Main Contribution:**
I was responsible for developing the core functionality of the PrepTrack Application. My work included collecting and validating student information, processing seven days of practice scores, analyzing performance, and generating the final placement-readiness report. I also implemented the decision-making logic that determines whether a student is ready for a mock interview based on multiple eligibility criteria.

**Features I Implemented:**
I implemented several important features in the project, including student name validation, attendance validation, project completion verification, and profile verification. I also developed the module for processing seven days of practice scores, classifying performance into Strong, Satisfactory, Needs Improvement, and Critical categories, and calculating performance metrics such as total score, average score, highest score, lowest score, and passed or failed practice days. Additionally, I created the final status evaluation and recommendation system.

**Python Concepts I Used:**
The project allowed me to apply several fundamental Python concepts. I used variables and different data types to store information, conditional statements for decision-making, while loops for input validation, and for loops for processing practice scores. I also used Boolean expressions, counters, accumulators, arithmetic operators, logical operators, and formatted output statements to generate a structured report.

**Most Difficult Logic:**
The most challenging part of the project was implementing the placement-readiness evaluation. The application needed to check several conditions such as attendance, average score, graduation year eligibility, practice count, passed days, project completion, and profile verification. Ensuring that the program identified the first major blocker according to the required priority order required careful planning and testing.

**Problem I Faced:**
One of the main difficulties I faced was handling absent practice days while calculating performance statistics. Absent days should not affect the total score, average score, highest score, lowest score, or pass/fail counts. Managing these conditions correctly without producing incorrect results was challenging during development.

**How I Solved It:**
I solved this issue by using separate counters and control variables to track attempted and absent days. Whenever a student was absent, the program skipped all score-related calculations using the `continue` statement. I also used flags to correctly initialize and update the highest score, lowest score, and first critical score only for valid attempted practices. This ensured that all calculations and reports were accurate.



