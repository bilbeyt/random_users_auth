from django.db import models
import uuid


class CustomUserManager(models.Manager):
    def generate_api_key(self):
        api_key = str(uuid.uuid4().hex)[:15]
        if CustomUser.objects.filter(api_key=api_key).exists():
            self.generate_api_key()
        return api_key
        
    def save_data(self, *args, **kwargs):
        user_list = kwargs.get("users")
        for user in user_list:
            setattr(user, "api_key", self.generate_api_key())
        CustomUser.objects.bulk_create(user_list, 1000)


class CustomUser(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    gender = models.CharField(max_length=6)
    email = models.EmailField()
    age = models.PositiveIntegerField()
    phone = models.CharField(max_length=25)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    api_key = models.CharField(max_length=15, unique=True)
    objects = CustomUserManager()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name + " " + self.surname

