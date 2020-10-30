# Generated by Django 3.1.1 on 2020-10-30 01:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0005_auto_20201029_2143'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jogos',
            name='plataforma',
        ),
        migrations.AlterField(
            model_name='generos',
            name='games',
            field=models.ManyToManyField(blank=True, related_name='generos', to='games.Jogos'),
        ),
        migrations.CreateModel(
            name='Plataformas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plataforma', models.CharField(max_length=64)),
                ('games', models.ManyToManyField(blank=True, related_name='plataformas', to='games.Jogos')),
            ],
        ),
    ]
