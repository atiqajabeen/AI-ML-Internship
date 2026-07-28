# Internship Performance Analyzer 📊

## Day 5 Internship Task – Data Analysis & Logic Building Challenge

## Overview

The **Internship Performance Analyzer** is a data analysis project developed as part of the AI/ML internship. The main objective of this project is to understand how data is collected, cleaned, analyzed, and converted into meaningful insights before building AI/ML models.

This project uses **Python, NumPy, and Pandas** to analyze internship performance data and generate performance insights and recommendations.

---

## Project Objectives

* Create and analyze a custom internship dataset
* Practice data manipulation using Pandas
* Perform numerical calculations using NumPy
* Understand data cleaning and exploration
* Create a custom performance scoring system
* Generate automated recommendations based on performance

---

## Technologies Used

* Python
* NumPy
* Pandas
* CSV Dataset

---

## Dataset Description

A custom dataset containing information about 30 interns was created with the following attributes:

| Column                  | Description                       |
| ----------------------- | --------------------------------- |
| Intern ID               | Unique identifier for each intern |
| Name                    | Intern name                       |
| Department              | Assigned department               |
| Attendance Percentage   | Attendance rate                   |
| Tasks Assigned          | Total assigned tasks              |
| Tasks Completed         | Completed tasks count             |
| Average Submission Time | Average task submission time      |
| Daily Learning Hours    | Learning hours per day            |
| Quiz Score              | Performance in quizzes            |

---

## Analysis Performed

### 1. Top Performing Interns

Identifies the top 5 interns based on the calculated performance score.

### 2. Lowest Performing Interns

Finds the bottom 5 interns who require improvement.

### 3. Performance Score Calculation

A custom performance formula is designed to evaluate intern performance.

Example approach:

```
Performance Score =
(Quiz Score × 0.25) +
(Attendance Percentage × 0.2) +
(Task Completion Rate × 0.35)
```

The formula combines multiple factors to provide a balanced performance evaluation.

---

### 4. Performance Level Classification

Interns are categorized into:

* Excellent
* Good
* Average
* Needs Improvement

Based on their calculated performance score.

---

### 5. Department Performance Analysis

The project analyzes department-wise performance to identify the department with the highest overall performance.

---

### 6. Mentor Support Identification

Interns who have low attendance, low quiz scores, or incomplete tasks are identified and provided with improvement recommendations.

---

### 7. Statistical Analysis

The project calculates:

* Average attendance
* Mean values
* Maximum and minimum values
* Basic dataset statistics

---

### 8. Automated Recommendations

A recommendation system is created using logical conditions.

Examples:

* Low attendance → Improve consistency and participation
* Low quiz score → Practice more and review concepts
* Low task completion → Focus on task management

---

## Project Structure

```
Internship-Performance-Analyzer/

│
├── internship_dataset.csv
├── performance_analyzer.py
├── analysis_report.txt
└── README.md
```

---

## Learning Outcomes

Through this project, I learned:

* How to work with real-world structured data
* Creating and analyzing CSV datasets
* Data cleaning and exploration techniques
* Using NumPy for numerical operations
* Using Pandas for data manipulation
* Designing custom performance evaluation logic
* Generating insights from data

---

## Challenges Faced

* Designing a meaningful performance scoring formula
* Organizing and analyzing multiple performance factors
* Creating logical conditions for recommendations
* Handling and exploring structured data efficiently

---

## Future Improvements

* Add data visualization using Matplotlib
* Create an interactive dashboard
* Apply machine learning models for performance prediction
* Store data using a database
* Build a web-based performance analyzer

---

## Author

**Atiqa Jabeen**
AI/ML Internship – Day 5 Task
