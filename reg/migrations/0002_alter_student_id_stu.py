# Generated by Django 3.2.15 on 2022-09-11 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reg', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='id_stu',
            field=models.CharField(max_length=10, primary_key=True, serialize=False),
        ),
    ]