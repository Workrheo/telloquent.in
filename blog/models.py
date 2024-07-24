from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone
from accounts.models import User


# Create your models here.



class Post(models.Model):
	title = models.CharField(max_length=100)
	short_content = models.TextField()
	content = models.TextField()
	main_content = models.TextField()
	quote = models.CharField(max_length = 1000 , null=True , blank = True)

	image = models.ImageField(upload_to='blog/', blank=True, null=True)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	category = models.ForeignKey('Category', null=True,  on_delete=models.SET_NULL)
	created = models.DateTimeField(default=timezone.now)


	def __str__(self):
		return self.title




class Category(models.Model):
	category_name = models.CharField(max_length=50)



	class Meta:
		verbose_name = 'category'
		verbose_name_plural = 'categories'


	def __str__(self):
		return self.category_name



class Comment(models.Model):
	User = models.ForeignKey(User , on_delete=models.CASCADE)
	post = models.ForeignKey(Post , on_delete=models.CASCADE)
	content = models.TextField()
	created = models.DateTimeField(default=timezone.now)
