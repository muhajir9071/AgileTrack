from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class UserProfile(models.Model):
    User = models.OneToOneField(User, on_delete=models.CASCADE,null=True)
    Address = models.CharField(max_length=100)
    City = models.CharField(max_length=100)
    State = models.CharField(max_length=100)

 
class TaskDetails(models.Model):
    TASK_TITLE=models.CharField(max_length=100)
    TASK_CREATED=models.ForeignKey(User,related_name='tasks_created',on_delete=models.CASCADE,null=True)
    TASK_CLOSED=models.ForeignKey(User,related_name='tasks_closed',on_delete=models.CASCADE,null=True)
    TASK_CREATED_ON=models.DateField(auto_now_add=True,null=True)
    TASK_CLOSED_ON=models.DateField(null=True)
    TASK_DUE_DATE=models.DateField()
    TASK_REWARD=models.IntegerField()
    TASK_DESCRIPTION=models.CharField(max_length=300)
    TASK_HOLDER=models.CharField(max_length=100,null=True)
    Choice = [
        ('Open','Open'),
        ('Closed', 'Closed'),
        ('Reopen', 'Reopen'),
        ('Expired', 'Expired'),
        ('Resolved', 'Resolved'),
        ('Inprocess','Inprocess'),
    ]
    TASK_STATUS=models.CharField(max_length=100,choices=Choice,default='Open')
#mycart model
class Mycart(models.Model):
    user= models.ForeignKey(User,on_delete=models.CASCADE)
    task=models.ForeignKey(TaskDetails,on_delete=models.CASCADE)
    task_count=models.IntegerField(default=1)

#Account model
class Account(models.Model):
    ACCOUNT_HOLDER= models.OneToOneField(User,on_delete=models.CASCADE)
    ACCOUNT_BALANCE=models.IntegerField()

#Transaction  model
class Transaction(models.Model):
    sender=models.ForeignKey(User,related_name='sender',on_delete=models.CASCADE) 
    reciver=models.ForeignKey(User,related_name='reciver',on_delete=models.CASCADE)
    amount=models.IntegerField()
    timestamp=models.DateTimeField(auto_now_add=True,null=True)
