# Smart Internship Management System

A console-based Internship Management System built in Python using Object-Oriented Programming. It allows you to register interns, assign and track tasks, calculate performance scores, and generate reports — with all data automatically saved to and loaded from a local file.

## Features

- Register a new intern with a unique auto-generated ID
- Assign multiple tasks to an intern
- Update task status (Pending / In Progress / Completed)
- Search intern by name or ID
- View all pending tasks
- View all completed tasks
- View intern rankings (leaderboard)
- View a full summary report
- View all registered interns
- Automatic save to file after every change
- Automatic load of saved data when the program starts

## Unique ID Format

Every intern is assigned an ID in the format:

```
INT-2026-001
```

The year is fixed to the current batch, and the number increments automatically. IDs are always checked for uniqueness before being assigned.

## Scoring System

Each task contributes to an intern's total score:

| Task Status   | Points |
|---------------|--------|
| Completed     | 12     |
| In Progress   | 6      |
| Pending       | 0      |

**Bonus:** an intern gets an extra **+5 points** if they have completed 3 or more tasks.

## Ranking System

Based on total score, each intern receives a rank:

| Score Range | Rank            |
|-------------|-----------------|
| 45+         | Star Performer  |
| 25–44       | Rising Talent   |
| 10–24       | On Track        |
| 0–9         | Just Started    |

## Duplicate Prevention

Before registering a new intern, the system checks if an intern with the same **name and email** already exists. If found, registration is blocked.

## File Handling

All intern data (ID, name, email, and tasks) is saved to `intern_records.txt` in a simple pipe-delimited format:

```
INT-2026-001|John Smith|john@test.com|Build API::Completed;;Write Docs::Pending;;
```

This file is automatically read on startup so no data is lost between sessions.

## How to Run

Requires Python 3.

```bash
python3 internship_system.py
```

## Dashboard Menu

```
========== AI Internship Dashboard ==========
1. Register Intern
2. Assign Task
3. Update Task Status
4. Search Intern
5. View Pending Tasks
6. View Completed Tasks
7. View Rankings
8. Generate Report
9. View All Interns
10. Exit
==============================================
```

## Project Structure

```
internship_system.py     -> Main application file
intern_records.txt       -> Auto-generated data file (created after first run)
README.md                -> Project documentation
```

## Technologies Used

- Python 3
- Object-Oriented Programming (Classes & Objects)
- File Handling (read/write)
- Exception Handling