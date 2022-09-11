from django.db import models

# Create your models here.

class Subject(models.Model):
    id_sj = models.CharField(max_length=10, primary_key = True)
    name_sj = models.CharField(max_length=100)
    sem_sj = models.IntegerField()
    year_sj = models.IntegerField()
    seat_sj = models.IntegerField()
    status = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.id_sj} ({self.name_sj})"

class Student(models.Model):
    id_stu = models.CharField(max_length=10, primary_key = True)
    name_stu = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.id_stu} {self.name_stu}"


class Apply(models.Model):
    id_stu =  models.ForeignKey(Student, on_delete=models.CASCADE, related_name="stuApply")
    id_sj =  models.ForeignKey(Subject, on_delete=models.CASCADE, related_name="sjApply")

    def __str__(self):
        return f"{self.id_stu} {self.id_sj}"