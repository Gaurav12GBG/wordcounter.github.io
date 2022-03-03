from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE


class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=13)
    email = models.EmailField(max_length=100)
    Issue = models.TextField(max_length=250, null=True)

    class Meta:
        db_table = "wordcountercontact"
        
    def __str__(self):
        return self.email
        

class UserFeedback(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=13)
    email = models.EmailField(max_length=100)
    feedback = models.TextField(max_length=250, null=True)
    feedback_date = models.DateField(max_length=30, auto_now=False, auto_now_add=True)

    class Meta:
        db_table = "userfeedback"
        
    def __str__(self):
        return self.email
    
class TextContentHistory(models.Model):
    id = models.AutoField(primary_key=True)
    text = models.TextField(max_length=2500)
    contentsavedate = models.DateTimeField(max_length=30, auto_now=False, auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    class Meta:
        db_table = "textcontenthistory"
        
    def __str__(self):
        return self.text