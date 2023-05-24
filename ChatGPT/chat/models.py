from django.db import models

# Create your models here.
class Chat(models.Model):
    text = models.CharField(max_length=500)
    gpt = models.CharField(max_length=17000)
    date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    
    def __str__(self):
        return self.text
    
class Hotel(models.Model):
    name = models.CharField(max_length=50)
    img_url = models.CharField(max_length=500, blank=True, null=True)
    
    def __str__(self):
        return self.name
    
class Processes(models.Model):
    name = models.CharField(max_length=50)
    img_url = models.CharField(max_length=500, blank=True, null=True)
    
    def __str__(self):
        return self.name
