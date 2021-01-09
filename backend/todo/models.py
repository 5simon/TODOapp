from django.db import models

# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length = 120)
    description = models.TextField()
    completed = models.BooleanField(default = False)

    #funcs
    def _str_(self):
        return self.title


# when the model is created, man has to run thie command: 
#-> python manage.py makemigrations todo 
#-> python manage.py migrate todo
