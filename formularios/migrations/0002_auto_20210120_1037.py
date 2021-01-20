# Generated by Django 3.1.5 on 2021-01-20 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formularios', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='musico',
            name='banda',
        ),
        migrations.CreateModel(
            name='Banda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('fecha_formacion', models.DateField()),
                ('musicos', models.ManyToManyField(to='formularios.Musico')),
            ],
        ),
    ]