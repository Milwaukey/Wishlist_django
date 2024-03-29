from django.db import models
from django.contrib.auth.models import User
from secrets import token_urlsafe

# Create your models here.
class PasswordResetRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=43, default=token_urlsafe)
    created_timestamp = models.DateTimeField(auto_now_add=True)
    updated_timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user} - CREATED: {self.created_timestamp} - UPDATED: {self.updated_timestamp} - {self.token}'