from django.db import models
from django.contrib.auth.hashers import make_password, check_password
# Create your models here.
class Member(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=255)  # Increased length for hashed password
    email = models.EmailField(max_length=100, unique=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    role = models.CharField(max_length=100, blank=True, null=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'members'
        ordering = ['-createdAt']

    def save(self, *args, **kwargs):
        if self._state.adding:
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)

    def __str__(self):
        return f"{self.username} ({self.email})"
