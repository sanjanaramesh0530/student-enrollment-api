from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect("students.db")
    conn.row_factory = sqlite3.Row
    return conn


# Create the database and students table
def init_db():
    conn = get_db_connection()

    conn.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            course TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL
        )
    """)

    conn.commit()
    conn.close()


# GET - all students
@app.route("/students", methods=["GET"])
def get_students():
    conn = get_db_connection()

    students = conn.execute(
        "SELECT * FROM students"
    ).fetchall()

    conn.close()

    return jsonify([dict(student) for student in students])


# GET - one student
@app.route("/students/<int:id>", methods=["GET"])
def get_student(id):
    conn = get_db_connection()

    student = conn.execute(
        "SELECT * FROM students WHERE id = ?",
        (id,)
    ).fetchone()

    conn.close()

    if student is None:
        return jsonify({"error": "Student not found"}), 404

    return jsonify(dict(student))


# POST - enroll a student
@app.route("/students", methods=["POST"])
def add_student():
    data = request.get_json()

    name = data.get("name")
    age = data.get("age")
    course = data.get("course")
    email = data.get("email")

    if not name or not age or not course or not email:
        return jsonify({"error": "All fields are required"}), 400

    conn = get_db_connection()

    try:
        cursor = conn.execute(
            """
            INSERT INTO students (name, age, course, email)
            VALUES (?, ?, ?, ?)
            """,
            (name, age, course, email)
        )

        conn.commit()
        student_id = cursor.lastrowid

    except sqlite3.IntegrityError:
        conn.close()
        return jsonify({"error": "Email already exists"}), 400

    conn.close()

    return jsonify({
        "message": "Student enrolled successfully",
        "student_id": student_id
    }), 201


# PUT - update entire student
@app.route("/students/<int:id>", methods=["PUT"])
def update_student(id):
    data = request.get_json()

    name = data.get("name")
    age = data.get("age")
    course = data.get("course")
    email = data.get("email")

    if not name or not age or not course or not email:
        return jsonify({"error": "All fields are required"}), 400

    conn = get_db_connection()

    cursor = conn.execute(
        """
        UPDATE students
        SET name = ?, age = ?, course = ?, email = ?
        WHERE id = ?
        """,
        (name, age, course, email, id)
    )

    conn.commit()
    conn.close()

    if cursor.rowcount == 0:
        return jsonify({"error": "Student not found"}), 404

    return jsonify({
        "message": "Student updated successfully"
    })


# PATCH - partially update student
@app.route("/students/<int:id>", methods=["PATCH"])
def patch_student(id):
    data = request.get_json()

    conn = get_db_connection()

    student = conn.execute(
        "SELECT * FROM students WHERE id = ?",
        (id,)
    ).fetchone()

    if student is None:
        conn.close()
        return jsonify({"error": "Student not found"}), 404

    name = data.get("name", student["name"])
    age = data.get("age", student["age"])
    course = data.get("course", student["course"])
    email = data.get("email", student["email"])

    conn.execute(
        """
        UPDATE students
        SET name = ?, age = ?, course = ?, email = ?
        WHERE id = ?
        """,
        (name, age, course, email, id)
    )

    conn.commit()
    conn.close()

    return jsonify({
        "message": "Student partially updated"
    })


# DELETE - delete student
@app.route("/students/<int:id>", methods=["DELETE"])
def delete_student(id):
    conn = get_db_connection()

    cursor = conn.execute(
        "DELETE FROM students WHERE id = ?",
        (id,)
    )

    conn.commit()
    conn.close()

    if cursor.rowcount == 0:
        return jsonify({"error": "Student not found"}), 404

    return jsonify({
        "message": "Student deleted successfully"
    })


if __name__ == "__main__":
    init_db()
    app.run(debug=True)
    