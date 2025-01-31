from django.db import models


class Slider(models.Model):

    image = models.ImageField('Slider image', upload_to='slider')
    title = models.CharField('Slider title', max_length=60)
    text = models.TextField('Slider text')

    def __str__(self):
        return self.title

class About(models.Model):
    title = models.CharField(max_length=30)
    text1 = models.TextField()
    text2 = models.TextField()
    image = models.ImageField('About image', upload_to='about')
    button_name = models.CharField(max_length=20)

    def __str__(self):
        return self.title


class Team(models.Model):
    name = models.CharField(max_length=60)
    position = models.CharField(max_length=50)
    img = models.ImageField(upload_to='team')

    def __str__(self):
        return self.name

class Contact(models.Model):

    name = models.CharField('Contact name', max_length=60)
    email = models.EmailField('Contact email')
    text = models.TextField('Contact text')

    def __str__(self):
        return f'{self.name} - {self.email}'
    
class Info(models.Model):
    address = models.CharField(max_length=60)
    phone = models.CharField(max_length=60)
    email = models.EmailField()
    fb = models.URLField()
    ins = models.URLField()
    X = models.URLField()

    def __str__(self):
        return self.address