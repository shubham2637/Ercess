from django.db import models

# Create your models here.
class user(models.Model):
    Name = models.CharField(max_length=256)
    email = models.EmailField()
    password = models.CharField(max_length=128)

    def __str__(self):
        return f"{self.id} {self.Name} {self.email}"
