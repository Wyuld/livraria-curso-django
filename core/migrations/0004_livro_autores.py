# Generated by Django 3.2.8 on 2021-10-18 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20211018_1801'),
    ]

    operations = [
        migrations.AddField(
            model_name='livro',
            name='autores',
            field=models.ManyToManyField(related_name='livros', to='core.Autor'),
        ),
    ]