from django import forms



class RegistrationForm(forms.Form):
    First_Name  =   forms.CharField(max_length=20)
    Last_Name   =   forms.CharField(max_length=20)
    Email_Address   =   forms.EmailField( max_length=254)
    Password =   forms.CharField(max_length=20)

    Company_Name    =   forms.CharField(max_length=20)
    Mobile  =   forms.IntegerField()
    Telephone   =   forms.IntegerField()
    Address_Lane1   =   forms.CharField(max_length=20)
    Address_Lane2   =  forms.CharField(max_length=20)
    City    =   forms.CharField(max_length=20)
    Postal_Zip  =   forms.IntegerField()

    # countries =   [
    #     ('USA','America'),
    #     ('DEU','Germany'),
    #     ('AU','Australia'),
    #     ('FR','France')
    # ]

    # Country =   forms.CharField(
    #     max_length=20,
    #     choices=countries,
    #     default='--Country--'
    # )

    State   =   forms.CharField(max_length=20)
