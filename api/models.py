from django.db import models

# Create your models here.


class User(models.Model) :
    First_Name  =   models.CharField(max_length=20)
    Last_Name   =   models.CharField(max_length=20)
    Email_Address   =   models.EmailField( max_length=254)
    Password =   models.CharField(max_length=20)

    Company_Name    =   models.CharField(max_length=20)
    Mobile  =   models.IntegerField()
    Telephone   =   models.IntegerField()
    Address_Lane1   =   models.CharField(max_length=20)
    Address_Lane2   =   models.CharField(max_length=20)
    City    =   models.CharField(max_length=20)
    Postal_Zip  =   models.IntegerField()

    countries =   [
        ('USA','America'),
        ('DEU','Germany'),
        ('AU','Australia'),
        ('FR','France')
    ]

    Country =   models.CharField(
        max_length=20,
        choices=countries,
        default='--Country--'
    )

    State   =   models.CharField(max_length=20)

    def __str__(self):
        return self.First_Name
    