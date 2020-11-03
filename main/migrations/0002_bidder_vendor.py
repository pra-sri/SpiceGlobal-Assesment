# Generated by Django 3.1.3 on 2020-11-03 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bidder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_Name', models.CharField(max_length=20)),
                ('Last_Name', models.CharField(max_length=20)),
                ('Email_Address', models.EmailField(max_length=254)),
                ('Password', models.CharField(max_length=20)),
                ('Company_Name', models.CharField(max_length=20)),
                ('Mobile', models.IntegerField()),
                ('Telephone', models.IntegerField()),
                ('Address_Lane1', models.CharField(max_length=20)),
                ('Address_Lane2', models.CharField(max_length=20)),
                ('City', models.CharField(max_length=20)),
                ('Postal_Zip', models.IntegerField()),
                ('Country', models.CharField(choices=[('USA', 'America'), ('DEU', 'Germany'), ('AU', 'Australia'), ('FR', 'France')], default='--Country--', max_length=20)),
                ('State', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_Name', models.CharField(max_length=20)),
                ('Last_Name', models.CharField(max_length=20)),
                ('Email_Address', models.EmailField(max_length=254)),
                ('Password', models.CharField(max_length=20)),
                ('Company_Name', models.CharField(max_length=20)),
                ('Mobile', models.IntegerField()),
                ('Telephone', models.IntegerField()),
                ('Address_Lane1', models.CharField(max_length=20)),
                ('Address_Lane2', models.CharField(max_length=20)),
                ('City', models.CharField(max_length=20)),
                ('Postal_Zip', models.IntegerField()),
                ('Country', models.CharField(choices=[('USA', 'America'), ('DEU', 'Germany'), ('AU', 'Australia'), ('FR', 'France')], default='--Country--', max_length=20)),
                ('State', models.CharField(max_length=20)),
            ],
        ),
    ]
