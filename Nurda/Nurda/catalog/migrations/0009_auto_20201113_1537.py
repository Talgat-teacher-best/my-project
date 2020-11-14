# Generated by Django 3.1.1 on 2020-11-13 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0008_auto_20201112_2221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='language',
            field=models.CharField(choices=[('Russian', 'Russian'), ('English', 'O vy iz Ameriki?'), ('Kazakh', 'Aktau the best')], default='Russian', help_text='Select a language for this book', max_length=122112, verbose_name='Language'),
        ),
    ]
