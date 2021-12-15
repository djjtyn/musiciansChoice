# Generated by Django 2.1.15 on 2021-12-15 18:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('instruments', '0003_instrumentpicture_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='InstrumentCmment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=6000)),
                ('instrument', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='instruments.Instrument')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]