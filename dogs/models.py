from django.db import models
from django.contrib.auth.models import AbstractUser
class Dog(models.Model):
    name = models.CharField(max_length=100, verbose_name="Кличка")
    breed = models.ForeignKey("dogs.Breed", verbose_name="Порода собаки", related_name="dogs",
                              on_delete=models.SET_NULL, null=True)
    photo = models.ImageField(upload_to="dog_photo", verbose_name="Картинка", null=True, blank=True)
    date_born = models.DateField(verbose_name="Дата рождения", blank=True, null=True)

class Breed(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
class User(AbstractUser):
    username = None
    email = models.EmailField(
        verbose_name='Почта',
        unique=True
    )
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

