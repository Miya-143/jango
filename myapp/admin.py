from django.contrib import admin
from .models import *

admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Teacher)
admin.site.register(Enrollment)
admin.site.register(Department)
admin.site.register(Exam)
admin.site.register(Result)