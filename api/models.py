from django.db import models

# Create your models here.

# User model to store user information
class User(models.Model):
    userid=models.AutoField(primary_key=True) # Primary key, auto-incrementing field
    name=models.CharField(max_length=100) # User's name
    email=models.EmailField(unique=True) # User's email, must be unique
    password=models.CharField(max_length=10) # User's password, limited to 10 characters
    points=models.IntegerField() # Points accumulated by the user
    def __str__(self) -> str:
        return self.email # Display the user's email in admin and other interfaces
    
    
# AppDetails model to store details about each app
class AppDetails(models.Model):
    appid=models.AutoField(primary_key=True) # Primary key, auto-incrementing field
    appName=models.CharField(max_length=100) # Name of the app
    appLink=models.CharField(max_length=100) # Link to the app
    appCat=models.CharField(max_length=50) # Category of the app
    appSubCat=models.CharField(max_length=50) # Subcategory of the app
    appIcon=models.ImageField(upload_to='icon/') # Path to the app's icon image
    points=models.IntegerField() # Points associated with the app
    def __str__(self) -> str:
        return self.appName # Display the app's name in admin and other interfaces
   
   
# TaskDetail model to store details about each task 
class TaskDetail(models.Model):
    taskid=models.AutoField(primary_key=True) # Primary key, auto-incrementing field
    appid=models.IntegerField() # Foreign key to the AppDetails model
    userid=models.IntegerField() # Foreign key to the User model
    taskname=models.CharField(max_length=100) # Name of the task
    appIcon=models.ImageField(upload_to='images/') # Path to the task's associated image
    def __str__(self) -> str:
        return self.taskname # Display the task's name in admin and other interfaces

    
    