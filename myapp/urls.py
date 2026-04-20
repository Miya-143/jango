from django.urls import path
from . import views

urlpatterns = [
    path('students/', views.student_list),
    path('courses/', views.course_list),
    path('teachers/', views.teacher_list),
    path('enrollments/', views.enrollment_list),
    path('departments/', views.department_list),
    path('exams/', views.exam_list),
    path('results/', views.result_list),
]