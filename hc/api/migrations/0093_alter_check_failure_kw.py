# Generated by Django 4.0.6 on 2022-07-13 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0092_alter_check_success_kw'),
    ]

    operations = [
        migrations.AlterField(
            model_name='check',
            name='failure_kw',
            field=models.CharField(blank=True, default='', max_length=200),
            preserve_default=False,
        ),
    ]
