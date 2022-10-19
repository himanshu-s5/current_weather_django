from django.db import models


class UserModel(models.Model):
    username = models.CharField(max_length=20, unique=True)
    First_name = models.CharField(max_length=25)
    Last_name = models.CharField(max_length=25)
    Email = models.EmailField(unique=True)
    password = models.CharField(max_length=50)
    confirm_password = models.CharField(max_length=50)


class ImageModel(models.Model):
    image = models.ImageField(upload_to='images/')
    text = models.TextField(max_length=300)


class ContactModel(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.TextField(max_length=256)
