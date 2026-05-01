# 🎓 College Management System (Django Project)

## 📌 Project Overview

This project is a **College Management System** built using Django.
It provides backend APIs to manage students, courses, teachers, departments, exams, enrollments, and results.

The system follows a structured approach using **models, views, and URLs**, and returns data in **JSON format**.

---

## 🚀 Features

* Manage Students, Courses, Teachers, Departments
* Enrollment system for students and courses
* Exam and Result management
* REST-like API endpoints
* Dynamic URLs for accessing specific records
* Admin panel for data management

---

## 🛠️ Tech Stack

* **Backend:** Django (Python)
* **Database:** SQLite (default)
* **API Format:** JSON
* **Tools:** VS Code, Postman

---

## 📂 Project Structure

```
college_project/
│
├── college_project/   # Main project settings
│   └── urls.py
│
├── myapp/             # Application
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── admin.py
│
└── manage.py
```

---

## 🧱 Models (Schemas)

The project includes the following models:

1. Student
2. Course
3. Teacher
4. Enrollment
5. Department
6. Exam
7. Result

---

## ⚙️ Installation & Setup

### 1. Clone the repository

```
git clone <your-repo-link>
cd college_project
```

### 2. Create virtual environment

```
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies

```
pip install django
```

### 4. Run migrations

```
python manage.py makemigrations
python manage.py migrate
```

### 5. Create superuser

```
python manage.py createsuperuser
```

### 6. Run server

```
python manage.py runserver
```

---

## 🔐 Admin Panel

Access admin panel:

```
http://127.0.0.1:8000/admin/
```

---

## 🌐 API Endpoints

### 📌 Get All Data

* `/api/students/`
* `/api/courses/`
* `/api/teachers/`
* `/api/enrollments/`
* `/api/departments/`
* `/api/exams/`
* `/api/results/`

---

### 📌 Dynamic URLs (Single Record)

* `/api/students/<id>/`
* `/api/courses/<id>/`
* `/api/results/<id>/`

Example:

```
http://127.0.0.1:8000/api/students/1/
```

---

### 📌 Update Data (PUT)

```
/api/students/update/<id>/
```

---

## 🧪 Testing APIs

You can test APIs using:

* Browser (for GET)
* Postman (for POST, PUT, DELETE)

---

## 📊 Sample JSON Response

```json
{
  "id": 1,
  "name": "John",
  "email": "john@gmail.com",
  "age": 20
}
```

---

## 🔥 Future Enhancements

* Add full CRUD operations (POST, PUT, DELETE)
* Use Django REST Framework
* Add authentication & authorization
* Connect frontend (React / Angular)
* Deploy project online

---

## 👩‍💻 Author

**Sowmiya**

---

## 📌 Conclusion

This project demonstrates a basic backend system using Django with multiple models, API handling, and dynamic routing. It is useful for understanding real-world application structure.

---
