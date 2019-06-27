from django.contrib import admin

# Register your models here.
from apps.user.models import User, Student2, Mentor, Program, Students_Mentor, Course, Courses_Student

admin.site.register(User)
admin.site.register(Student2)
admin.site.register(Mentor)
admin.site.register(Program)
admin.site.register(Students_Mentor)
admin.site.register(Course)
admin.site.register(Courses_Student)
