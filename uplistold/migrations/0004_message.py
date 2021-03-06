# Generated by Django 3.2.3 on 2021-06-14 05:28

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('uplistold', '0003_alter_userprofile_profile_pic'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub', models.CharField(blank=True, max_length=200, null=True)),
                ('msg', models.CharField(blank=True, max_length=500, null=True)),
                ('posted_date', models.DateTimeField(default=datetime.datetime(2021, 6, 14, 10, 57, 58, 307721))),
                ('ad_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sender', to='uplistold.postad')),
                ('reciever', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reciever', to=settings.AUTH_USER_MODEL)),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
