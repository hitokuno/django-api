# Generated by Django 2.2.9 on 2019-12-25 01:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_attach'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='attach',
            field=models.FileField(blank=True, null=True, upload_to='uploads/%Y/%m/%d/', verbose_name='添付ファイル'),
        ),
    ]
