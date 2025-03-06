from django.db import models

class Record(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=100, default="Anonymous")
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=20)
    address = models.TextField(max_length=100)
    city = models.CharField(max_length=50)

    def __str__(self):
        return (f"{self.name} {self.last_name}")
    
    

