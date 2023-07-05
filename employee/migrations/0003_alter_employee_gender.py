# Generated by Django 4.2.2 on 2023-07-05 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("employee", "0002_alter_employee_table"),
    ]

    operations = [
        migrations.AlterField(
            model_name="employee",
            name="gender",
            field=models.CharField(
                choices=[("M", "Male"), ("F", "Female")],
                default="M",
                max_length=1,
                null=True,
            ),
        ),
    ]
