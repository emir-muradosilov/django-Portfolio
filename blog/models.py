from django.db import models

# Create your models here.
class Posts(models.Model):
    tittle = models.CharField(max_length = 200)
    descriptions = models.TextField()
    date = models.DateTimeField()

    def __str__(self):
        return self.tittle



        
