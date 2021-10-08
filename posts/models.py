from django.db import models
from django.contrib.auth.models import User
from profiles.models import Profile
#from users.models import CustomUser

# Create your models here.
class Post(models.Model):
	picture = models.ImageField(upload_to='images', blank=True)
	body = models.TextField()
	author = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
	updated = models.DateTimeField(auto_now=True)
	created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return str(self.pk)