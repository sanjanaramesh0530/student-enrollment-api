# Student Enrollment API

A RESTful Student Enrollment API built using Python, Flask, and SQLite.

## Features

- Enroll a student
- View all students
- View a specific student
- Update student details
- Partially update student details
- Delete a student
- Basic error handling

## Technologies Used

- Python
- Flask
- SQLite
- REST API
- JSON
- Git & GitHub

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/students` | Get all students |
| GET | `/students/<id>` | Get a specific student |
| POST | `/students` | Enroll a new student |
| PUT | `/students/<id>` | Update all student details |
| PATCH | `/students/<id>` | Partially update student details |
| DELETE | `/students/<id>` | Delete a student |

## Student Data

Each student contains:

- ID
- Name
- Age
- Course
- Email

## How to Run Locally

### 1. Clone the repository

```bash
git clone YOUR_REPOSITORY_URL