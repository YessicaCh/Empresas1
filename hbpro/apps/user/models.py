from django.db import models


class User(models.Model):
    nick_name = models.CharField(max_length=50, blank='False', null='False')
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    password = models.CharField(max_length=100, blank='False')
    age = models.IntegerField()
    e_mail = models.CharField(max_length=50, blank='False')
    number_phone = models.IntegerField(blank='False', null='True')
    github = models.CharField(max_length=50)
    Student_Mentor = models.BooleanField(
        default=True)  # True = Student, False = Mentor

    def __str__(self):
        return (self.name)


class Student2(User):
    is_working = models.BooleanField(default=False)

    def __str__(self):
        return self.nick_name


class Mentor(User, models.Model):
    is_mentorizing = models.BooleanField(default=False)

    def __str__(self):
        return (self.nick_name)


class Program(models.Model):
    year = models.SmallIntegerField()
    title = models.CharField(max_length=50)

    def __str__(self):
        return (self.title)


class Students_Mentor(models.Model):
    mentor = models.ForeignKey(Mentor, on_delete=models.CASCADE)  # One to many = foreign
    studentA = models.ForeignKey(Student2, null=True, related_name='studentA', on_delete=models.CASCADE)
    studentB = models.ForeignKey(Student2, null=True, related_name='studentB', on_delete=models.CASCADE)
    program = models.ForeignKey(Program, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)



class Course(models.Model):
    name = models.CharField(max_length=50)
    program = models.ForeignKey(Program, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)


class Courses_Student(models.Model):    
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    student2 = models.ForeignKey(Student2, on_delete=models.CASCADE)
    #studentsMentor = models.ForeignKey(Students_Mentor, on_delete=models.CASCADE)
    percentage = models.IntegerField()

    def __str__(self):
        return str(self.course.id)
