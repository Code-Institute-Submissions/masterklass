from django.db import models
from django.contrib.auth.models import User
from purchase.models import Plan
from PIL import Image


class UserProfile(models.Model):
    """
    User profiles are defined by this model. It extends the User model

    fields: user, plan, date_joined, name, profile_picture
    required: user, plan, date_joined 
    """
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    plan = models.ForeignKey(Plan, null=True, blank=True,
                             on_delete=models.SET_NULL, limit_choices_to={'active': True})
    date_joined = models.DateTimeField(auto_now=True, null=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    profile_picture = models.ImageField(
        default="default-profile-picture.jpg", upload_to='profile_img')

    def __str__(self):
        return self.user.username
