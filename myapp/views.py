from django.http import JsonResponse
from .models import *
from django.views.decorators.csrf import csrf_exempt
import json

# Student View
def student_list(request):
    data = list(Student.objects.values())
    return JsonResponse(data, safe=False)

# Course View
def course_list(request):
    data = list(Course.objects.values())
    return JsonResponse(data, safe=False)

# Teacher View
def teacher_list(request):
    data = list(Teacher.objects.values())
    return JsonResponse(data, safe=False)

# Enrollment View
def enrollment_list(request):
    data = list(Enrollment.objects.values())
    return JsonResponse(data, safe=False)

# Department View
def department_list(request):
    data = list(Department.objects.values())
    return JsonResponse(data, safe=False)

# Exam View
def exam_list(request):
    data = list(Exam.objects.values())
    return JsonResponse(data, safe=False)

# Result View
def result_list(request):
    data = list(Result.objects.values())
    return JsonResponse(data, safe=False)