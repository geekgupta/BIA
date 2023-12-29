from django.db import models

from django.contrib.auth import get_user_model
User = get_user_model()


# Create your models here.

## part of Task 3 
class Books(models.Model):
    Category = [   ## Add books catgories here 
        ("Comic", "Comic"),
        ("Mystery", "Mystery"),
        ("Fiction", "Fiction"),
        ("Horror", "Horror"),
    ]
    book_name = models.CharField(max_length = 100) ## Add max character constraints
    book_desc = models.CharField(max_length = 255) ## Add max character constraints
    category = models.CharField(choices = Category , max_length = 255) ## Map choies here 
    author = models.ForeignKey(User , on_delete=models.CASCADE, null=True, blank=True)  ## Link with built in user table provided by django 
    
    ### run python manage.py makemigrations 
    ### run python manage.py migrate 