# Generated by Django 2.2.3 on 2019-07-20 06:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ticketing_system', '0002_auto_20190719_0706'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='username',
            field=models.CharField(default='username', max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='tickets_assigned',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='ticket_assigned_to',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='ticketing_system.Employee'),
        ),
    ]
