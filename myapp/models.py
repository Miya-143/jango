from django.db import models

# 1. Student
class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    age = models.IntegerField()

    def __str__(self):
        return self.name

# 2. Course
class Course(models.Model):
    title = models.CharField(max_length=100)
    duration = models.IntegerField()

    def __str__(self):
        return self.title

# 3. Teacher
class Teacher(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)

# 4. Enrollment
class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

# 5. Department
class Department(models.Model):
    name = models.CharField(max_length=100)

# 6. Exam
class Exam(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date = models.DateField()

# 7. Result
class Result(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    marks = models.IntegerField()