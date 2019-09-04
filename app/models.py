from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class BlackList(models.Model):
    idx = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user
