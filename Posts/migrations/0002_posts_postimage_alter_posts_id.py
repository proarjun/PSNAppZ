# Generated by Django 4.2.1 on 2023-05-29 11:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='postimage',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='Posts.postimage'),
        ),
        migrations.AlterField(
            model_name='posts',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
