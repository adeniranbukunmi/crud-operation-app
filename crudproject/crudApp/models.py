from django.db import models

# Create your models here.
class StudentDetails(models.Model):
    name=models.CharField(max_length=25, blank=True, null=False )
    email=models.EmailField()
    age=models.IntegerField()
    gender=models.CharField(max_length=25, blank=True, null=False)

    def __str__(self):
        return self.name