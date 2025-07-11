from django.db import models

# from django.contrib.auth.models import User
import uuid #generate unique

from django.conf import settings
#ROLE
from django.contrib.auth.models import AbstractUser

    
# USER ROLE
ROLES = (
    (1, 'Company'),
    (2, 'Investor'),
    (3, 'Admin'),
)

class User(AbstractUser):
    role = models.PositiveSmallIntegerField(choices=ROLES, default=1)
    category = models.CharField(max_length=255, blank=True, null=True)
    reputation = models.CharField(max_length=255, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    profile_bg = models.ImageField(upload_to='profile_bg/', blank=True, null=True)
    vision = models.TextField(blank=True, null=True)
    mission = models.TextField(blank=True, null=True)
    userDetail = models.TextField(blank=True, null=True)
    umkm_level = models.CharField(max_length=100, blank=True, null=True)
    investment_history = models.ManyToManyField('self', symmetrical=False, blank=True)

class ChartData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = title = models.CharField(max_length=100)
    labels = models.JSONField()
    values = models.JSONField()
    chart_type = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.user.username}"
    
class UserChartSelection(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    chart = models.ForeignKey(ChartData, on_delete=models.CASCADE)
    
    class Meta:
        unique_together = ('user', 'chart')


# class User(AbstractUser):
#     is_company = models.BooleanField('company', default=False)
#     is_investor = models.BooleanField('investor', default=False)
#     is_admin = models.BooleanField('admin', default=False)


#model for password reset -> make migrations after update
class PasswordReset(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    #id generated by default (unique id)
    reset_id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    created_when = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Password reset for {self.user.username} at {self.created_when}"

class CompanyActivity(models.Model):
    company = models.ForeignKey(User, on_delete=models.CASCADE, related_name='activities')
    title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to='activity_images/', blank=True, null=True)

    def __str__(self):
        return f"{self.company.username}'s activity: {self.title}"



# placeholder user profile
# class UserProfileModel(models.Model):
#     user = models.OneToOneField(to=User, on_delete=models.CASCADE)
#     name = models.CharField(blank=True, null=True, max_length=100)
#     online_status = models.BooleanField(default=False)

#     def __str__(self) -> str:
#         return self.user.username

# class ChatModel(models.Model):
#     sender = models.CharField(max_length=100, default=None)
#     message = models.TextField(null =True, blank=True)
#     thread_name = models.CharField(null=True, blank=True, max_length=50)
#     timestamp = models.DateTimeField(auto_now_add=True)

#     def __str__(self) -> str:
#         return self.message

# from django.contrib.auth.models import User

# class Message(models.Model):
#     sender = models.ForeignKey(User, on_delete=models.CASCADE)
#     content = models.TextField()
#     timestamp = models.DateTimeField(auto_now_add=True)
#     def __str__(self):
#         return f'{self.sender}: {self.content}'

#python manage.py makemigrations
#Migrations for 'base':
#   base\migrations\0001_initial.py
#     + Create model PasswordREset

#python manage.py migrate
# Operations to perform:
#   Apply all migrations: admin, auth, base, contenttypes, sessions
# Running migrations:
#   Applying base.0001_initial... OK