from distutils.command.upload import upload
from email.mime import image
import profile
from tabnanny import verbose
from turtle import update
from unicodedata import name
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.core.validators import RegexValidator
import os
from uuid import uuid4
from django.utils.deconstruct import deconstructible

# Home Section.


class Bio(models.Model):
    name = models.CharField(max_length=20)
    title = models.CharField(max_length=40)
    description_2 = models.TextField(blank=False)
    age = models.PositiveIntegerField(null=True, blank=True)
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(
        validators=[phone_regex], max_length=17, blank=True)  # Validators should be a list
    birthday = models.DateField()
    profile_img = models.ImageField(upload_to='profile/')
    degree = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    city = models.CharField(max_length=255, blank=True)
    link = models.URLField(max_length=200)
    updated = models.DateTimeField(auto_now=True)
    available = (
        ('av', 'available'),
        ('nv', 'not available')
        # .. etc
    )
    freelance = models.CharField(max_length=5, choices=available, blank=True)

    class Meta:
        db_table = "briefcase_bio"
        ordering = ['name']

    def __str__(self):
        return self.name


class Skill(models.Model):
    skill_name = models.CharField(max_length=30)
    skill_strength = models.PositiveIntegerField(
        default=10, validators=[MinValueValidator(1), MaxValueValidator(100)])

    def __str__(self):
        return self.skill_name


class Portfolio(models.Model):
    image = models.ImageField(upload_to='portfolio/')
    link = models.URLField(max_length=200)

    def __str__(self):
        return f'Portfolio {self.id}'


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    image = models.ImageField(
        upload_to="static\assets\img", null=True, blank=True)

    def __str__(self):
        return self.title
