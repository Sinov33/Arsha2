from django.db import models


# Create your models here.




class Type(models.Model):
    nomi = models.CharField(max_length=20)

    def __str__(self):
        return self.nomi


class Poryfolio(models.Model):
    nomi = models.CharField(max_length=30)
    company_name = models.CharField(max_length=30)
    rasm1 = models.ImageField(upload_to='media')
    rasm2 = models.ImageField(upload_to='media',null=True,blank=True)
    rasm3 = models.ImageField(upload_to='media',null=True,blank=True)
    tur = models.ForeignKey(Type,models.CASCADE)
    vaqt = models.DateField()
    link = models.CharField(max_length=100)

class Malumot(models.Model):
    matn = models.CharField(max_length=100)

    def __str__(self):
        return self.matn



class Service(models.Model):
    nomi = models.CharField(max_length=30)
    rasm1 = models.ImageField(upload_to='media')
    tur = models.ForeignKey(Type, models.CASCADE)
    malumot = models.ForeignKey(Malumot,models.CASCADE)


class Lavozm(models.Model):
    nomi = models.CharField(max_length=30)

    def __str__(self):
        return self.nomi


class Team(models.Model):
    ism = models.CharField(max_length=20)
    familiya = models.CharField(max_length=20)
    yosh = models.IntegerField()
    rasm1 = models.ImageField(upload_to='media')
    malumot = models.CharField(max_length=200)
    lavozm = models.ForeignKey(Lavozm, models.CASCADE)




class Murojaj(models.Model):
    ism = models.CharField(max_length=50)
    gmail = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    text = models.TextField()
    vaqt = models.DateField()



