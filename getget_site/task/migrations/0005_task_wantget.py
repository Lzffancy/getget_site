# Generated by Django 2.2.12 on 2021-03-02 09:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
        ('task', '0004_auto_20210302_1616'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task_wantget',
            fields=[
                ('task', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='task.Task')),
                ('wgeter', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user.User', verbose_name='学生们')),
            ],
        ),
    ]
