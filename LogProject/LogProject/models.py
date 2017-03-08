# Create your models here.
from django.db import models
from django.contrib.auth.models import User


class Registration(models.Model):
	username = models.CharField(max_length=30)	
	mob_no = models.CharField(max_length=30)
	email = models.EmailField(max_length=30)
	password = models.CharField(max_length=30)
	confirm_pwd = models.CharField(max_length=30)

	def __str__(self):
		return self.username


 