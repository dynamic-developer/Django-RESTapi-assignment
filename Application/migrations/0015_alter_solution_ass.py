# Generated by Django 3.2.5 on 2021-07-29 09:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Application', '0014_alter_solution_ass'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solution',
            name='ass',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Application.assigment'),
        ),
    ]
