from django.db import models

# Create your models here.

class Person(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=20)
    avatar = models.CharField(max_length=300)
    

class Card(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=20)
    text = models.CharField(max_length=200)
    img = models.CharField(max_length=200)


class Collection(models.Model):
    id = models.BigAutoField(primary_key=True)
    person_id = models.ForeignKey('Person', on_delete=models.CASCADE)
    card_id = models.ForeignKey('Card', on_delete=models.CASCADE)


class Manga(models.Model):
    id = models.BigAutoField(primary_key=True)
    manga_id = models.ForeignKey('Card', on_delete=models.CASCADE)
    file_name = models.CharField(max_length=300)