# Generated by Django 2.0.7 on 2018-07-06 09:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kamp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('start_date', models.DateTimeField(verbose_name='Pocetak kampa')),
                ('end_date', models.DateTimeField(verbose_name='Kraj kampa')),
            ],
            options={
                'verbose_name_plural': 'Kampovi',
            },
        ),
        migrations.CreateModel(
            name='Radionica',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('leader_name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('kamp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mgmt.Kamp')),
            ],
            options={
                'verbose_name_plural': 'Radionice',
            },
        ),
    ]
