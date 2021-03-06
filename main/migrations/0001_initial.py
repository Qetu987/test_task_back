# Generated by Django 4.0 on 2021-12-20 11:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Servis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Subservice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=15)),
                ('date', models.DateTimeField(auto_now=True)),
                ('servises_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.servis')),
            ],
        ),
    ]
