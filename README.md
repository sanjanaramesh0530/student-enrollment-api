# Student Enrollment API

A RESTful Student Enrollment API built using Python, Flask, and SQLite.

This API allows users to create, view, update, partially update, and delete student enrollment records.

## 🚀 Live API

The API is deployed on Render:

https://student-enrollment-api-045f.onrender.com

## 🛠️ Technologies Used

- Python
- Flask
- SQLite
- REST API
- JSON
- Gunicorn
- Render
- Git & GitHub

## 📌 Features

- Add a new student
- Get all students
- Get a specific student
- Update complete student details
- Partially update student details
- Delete a student
- Store student data in SQLite database

## 🔗 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/students` | Get all students |
| GET | `/students/<id>` | Get a specific student |
| POST | `/students` | Enroll a new student |
| PUT | `/students/<id>` | Update all student details |
| PATCH | `/students/<id>` | Partially update student details |
| DELETE | `/students/<id>` | Delete a student |

## 📋 Student Data

Each student contains:

- ID
- Name
- Age
- Course
- Email

## ➕ Add a Student

### Endpoint

```text
POST /students