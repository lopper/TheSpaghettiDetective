# Generated by Django 2.1.7 on 2019-08-07 12:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_add_alert_overwrite_to_print'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserCredit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(default=0)),
                ('reason', models.CharField(choices=[('ALERT_OVERWRITE', 'ALERT_OVERWRITE')], max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('print', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Print')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
