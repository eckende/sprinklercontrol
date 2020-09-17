# Generated by Django 3.1 on 2020-09-09 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sprinklercontrolapp', '0004_weeklyrepeatingtimer'),
    ]

    operations = [
        migrations.AddField(
            model_name='weeklyrepeatingtimer',
            name='sprinklers',
            field=models.ManyToManyField(to='sprinklercontrolapp.Sprinkler'),
        ),
        migrations.AlterField(
            model_name='weeklyrepeatingtimer',
            name='description',
            field=models.CharField(max_length=150, verbose_name='Beschreibung'),
        ),
    ]
