from django.db import models
from django.core.validators import RegexValidator

phone_regex = RegexValidator(
    regex=r'^\+998\d{9}$',
    message="Phone number must be entered in the format: '+998xxxxxxxxx'. Up to 9 digits allowed."
)


class Users(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_joined = models.DateTimeField(auto_now_add=True)
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    phone_number = models.CharField(validators=[phone_regex], max_length=13, blank=True, null=True)
    is_businessman = models.BooleanField(default=False)

    def __str__(self):
        return self.first_name


class Businessmen(models.Model):
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    date_joined = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.user_id.is_businessman = True
        self.user_id.save()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.user_id.first_name + " - Biznesmen"