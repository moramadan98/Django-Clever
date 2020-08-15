# Generated by Django 3.1 on 2020-08-15 15:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('instructor', models.CharField(max_length=150)),
                ('duration', models.IntegerField(default=1)),
                ('leactures', models.IntegerField(default=1)),
                ('quizzes', models.IntegerField(default=0)),
                ('price', models.IntegerField(default=0)),
                ('description', models.TextField(max_length=200)),
                ('certification', models.CharField(choices=[('yes', 'yes'), ('no', 'no')], max_length=5)),
                ('image', models.ImageField(upload_to='course/')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.category')),
            ],
        ),
        migrations.CreateModel(
            name='Apply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.course')),
            ],
        ),
    ]