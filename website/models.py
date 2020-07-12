from django.db import models
from datetime import datetime
# Create your models here.
class students(models.Model):

    chosse =[
        ('male','male'),
        ('female','female'),
        ('other','other')
    ]
    name = models.CharField(max_length=50, null= True, unique=True,db_column="names")
    age = models.IntegerField( null= True, default=5)
    gender = models.CharField(max_length=50, null= True, choices=chosse)
    agree=models.BooleanField(null= True)
    created=models.DateField(null= True)
    default=models.DateTimeField(null= True, default=datetime.now)
    email=models.EmailField(null= True)
    text=models.TextField(null= True)
    
    image=models.ImageField(null= True)

    class Meta():
        verbose_name_plural= "students"
        db_table= "stds"
        ordering=["name"]

    def __str__(self):
        return self.name