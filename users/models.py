from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractUser




#crate an custom user model which is inherite django AbstractUser model for us django built in user model functionality 
class User(AbstractUser):
    #CAMS has 3type of user, this role class is basicly for seting role of a user
    class Role(models.TextChoices):
        MANAGER = "MANAGER",'Manager'
        STUFF = "STUFF",'Stuff'
        EMPLOYEE = "EMPLOYEE",'Employee'
    
    #creating some extra field for user table
    base_role = Role.MANAGER
    role  =  models.CharField(max_length=50,choices=Role.choices)
    company_name = models.CharField(max_length=100)
    company_website = models.CharField(max_length=100)
    company_id = models.PositiveIntegerField(null=False,blank=False)
    

    
    def save(self,*args,**kwargs):
        if not self.pk:
            self.role = self.base_role
            return super().save(*args,**kwargs)

#devide the user with there model role
#to access data role based we create 3 

class ManagerManager(BaseUserManager):
    def get_queryset(self,*args,**kwargs):
        result =  super().get_queryset(*args,**kwargs)
        return result.filter(role=User.Role.MANAGER)


class Manager(User):
    base_role = User.Role.MANAGER
    manager = ManagerManager()
    class Meta:
        proxy = True

    def welcome(slef):
        return "Only for managers"

class StuffManager(BaseUserManager):
    def get_queryset(self,*args,**kwargs):
        result =  super().get_queryset(*args,**kwargs)
        return result.filter(role=User.Role.STUFF)


class Stuff(User):
    base_role = User.Role.STUFF
    stuff = StuffManager()
    class Meta:
        proxy = True

    def welcome(slef):
        return "Only for stuff"

class EmployeeManager(BaseUserManager):
    def get_queryset(self,*args,**kwargs):
        result =  super().get_queryset(*args,**kwargs)
        return result.filter(role=User.Role.EMPLOYEE)


class Employee(User):
    base_role = User.Role.EMPLOYEE
    employee = EmployeeManager()
    class Meta:
        proxy = True

    def welcome(slef):
        return "Only for employee"