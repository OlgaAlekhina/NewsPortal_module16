# Generated by Django 4.0 on 2021-12-20 21:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('news', '0002_subscribers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscribers',
            name='subscriber',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
        ),
    ]
