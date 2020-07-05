from django.db import models

# Create your models here.


class User(models.Model):
    user_id = models.CharField(max_length=5)
    username = models.CharField(max_length=15)
    password = models.CharField(max_length=10)
    email = models.CharField(max_length=30)
    fname = models.CharField(max_length=15)
    mname = models.CharField(max_length=10)
    lname = models.CharField(max_length=15)
    mobno = models.IntegerField()  # data type and validation

    def __str__(self):
        return (self.username)


class Breed(models.Model):
    breed_id = models.CharField(max_length=5)
    breed = models.CharField(max_length=30)

    def __str__(self):
        return (self.breed)


class Pet_type(models.Model):
    type_id = models.CharField(max_length=3)  # pk
    pet_type = models.CharField(max_length=10)

    def __str__(self):
        return (self.pet_type)


class Pet(models.Model):
    pet_id = models.CharField(max_length=5)  # pk
    pet_type = models.ForeignKey(Pet_type, on_delete=models.CASCADE)  # fk
    pet_name = models.CharField(max_length=15)
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE)  # fk
    sex = models.CharField(max_length=6)
    colour = models.CharField(max_length=10)
    age = models.IntegerField()
    size = models.CharField(max_length=6)
    desc = models.CharField(max_length=300)
    #image = models.FileField(upload_to='p_image',blank=True)
    image = models.ImageField(upload_to='p_image', blank=True)

    def __str__(self):
        return (self.pet_name)


class Que(models.Model):
    que_id = models.CharField(max_length=3)  # pk
    question = models.CharField(max_length=100)

    def __str__(self):
        return (self.question)


class Answer(models.Model):
    ans_id = models.CharField(max_length=4)  # pk
    answer = models.CharField(max_length=50)  # assumed length
    que = models.ForeignKey(Que, on_delete=models.CASCADE)  # fk
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # fk


class Contact(models.Model):
    fname = models.CharField(max_length=15)
    lname = models.CharField(max_length=15)
    email = models.CharField(max_length=20)
    message = models.CharField(max_length=100)

    def __str__(self):
        return (self.fname)


class Feedback(models.Model):
    email = models.CharField(max_length=30)
    message = models.CharField(max_length=50)

    def __str__(self):
        return (self.email)
