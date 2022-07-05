from django.db import models
class UserAccount(models.Model):
    user_id = models.CharField(max_length=20)
    nick = models.CharField(max_length=20)
    password = models.BinaryField(max_length=64)
    salt = models.BinaryField(max_length=64)
    signup_date = models.DateField()