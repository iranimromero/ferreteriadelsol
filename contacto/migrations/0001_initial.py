# Generated by Django 4.0.3 on 2022-05-25 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('asunto', models.CharField(max_length=50)),
                ('mail', models.EmailField(max_length=254)),
                ('mensaje', models.TextField()),
            ],
        ),
    ]
