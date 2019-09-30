from django.db import models
import re
import bcrypt

#Managers
class UserManager(models.Manager):
    def registration_validate(self,postData):
        errors = {}
        EMAILREGEX = re.compile(r'^[a-zA-Z0-9.+-]+@[a-zA-Z0-9._-]+.[a-zA-Z]+$')
        form_email = postData['email']
        taken_email = User.objects.filter(email = form_email)
        if len(taken_email) > 0:
            errors['takenemail'] = "Error: That email is already taken!"
        if len(postData['name']) < 2:
            errors['name'] = "Error: Name should be between 8-45 characters!"
        if not EMAILREGEX.match(postData['email']):
            errors['emailpattern'] = "Invalid email address!"
        if len(postData['password']) < 8:
            errors['password'] = "Error: Password should be between 8-45 characters!"
        if postData['password'] != postData['confirm']:
            errors['confirm'] = "Error: Passwords do not match!"
        return errors
    
    def login_validate(self,postData):
        errors = {}
        emailSubmitted = postData['email']
        email_pass = User.objects.filter(email = emailSubmitted)
        if len(email_pass) > 0:
            submittedPass = postData['password']
            email_pass = email_pass[0]
            passwordMatch = bcrypt.checkpw(submittedPass.encode(), email_pass.password.encode())
            if passwordMatch == False:
                errors['wrongpass'] = "Error: Password is incorrect!"
        else:
            errors['nonuser'] = "Error: This email is not registered!"
        return errors
class QuoteManager(models.Manager):
    def quote_validate(self,postData):
        errors = {}
        if len(postData['source']) < 2:
            errors['source'] = "Error: Source must be at least 2 characters long!"
        if len(postData['content']) < 10:
            errors['content'] = "Error: Content must be at least 10 characters long!"
        return errors


    def edit_validate(self,postData):
        errors = {}
        if len(postData['source']) < 2:
            errors['source'] = "Error: Source must be at least 2 characters long!"
        if len(postData['content']) < 10:
            errors['content'] = "Error: Content must be at least 10 characters long!"
        return errors






class User(models.Model):
    name = models.CharField(max_length = 45)
    email = models.CharField(max_length = 45)
    password = models.CharField(max_length = 45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class Quote(models.Model):
    source = models.CharField(max_length = 45)
    content = models.CharField(max_length = 255)
    poster = models.ForeignKey(User,related_name="quotes",on_delete=models.CASCADE,null=True, blank=True)
    favorited = models.ManyToManyField(User, related_name="favorite_quotes")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = QuoteManager()