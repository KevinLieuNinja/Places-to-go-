from __future__ import unicode_literals
from django.db import models
import re 

class UserManager(models.Manager):
    def register(self, postData):
        #RegEx for email
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        #RegEx for Password
        PASSWORD_REGEX = re.compile(r'^(?=.*?\d)(?=.*?[A-Z])(?=.*?[a-z])[A-Za-z\d,!@#$%^&*+=]{5,}$')
        errors = {}

        if len (postData['email']) < 5:
            errors['email'] = "Your email Sucked!"
        if not EMAIL_REGEX.match(postData['email']):
            errors['email-invalid'] = 'Invalid Email, Loser!'

        if len(postData['password']) < 5:
            errors['password'] = "Weak-ass Password."
        if not PASSWORD_REGEX.match(postData['password']):
            errors['password-invalid'] = 'Even this password is invalid!'

        if len(postData['password_confirm']) < 5:
            errors['password_confirm'] = 'Comfirm this, Idiot!'
        if postData['password_confirm'] != postData['password']:
            errors['password_match'] = "Your passwords have to match, dhua!"

        return errors

    def login(self, postData):
        messages = []

        if len(postData['email']) < 1:
            messages.append('Wheres the email?!')

        if len(postData['password']) <2:
            messages.append('Wheres the password?!')

        return messages

class TripManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}

        if len(postData['destination']) < 2:
            errors['destination'] = "Give a better destination"

        # if len(postData['start']) < 2:
        #     errors['start'] = "Give a valid start"

        # if len(postData['end']) < 2:
        #     errors['end'] = "Not a valid year"

        if len(postData['plan']) < 10:
            errors['plan'] = "Not enough words to be shared"

        return errors

class User(models.Model):
    email = models.CharField(max_length = 50)
    password = models.CharField(max_length = 50)
    F_name = models.CharField(max_length = 50)
    L_name = models.CharField(max_length = 50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

class Trip(models.Model):
    destination = models.CharField(max_length = 50)
    start = models.DateField()
    end = models.DateField()
    plan = models.CharField(max_length= 225)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = TripManager()