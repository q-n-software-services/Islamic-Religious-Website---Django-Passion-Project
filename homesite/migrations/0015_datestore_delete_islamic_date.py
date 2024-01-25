# Generated by Django 4.1.3 on 2022-12-03 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homesite', '0014_islamic_date_delete_datestore'),
    ]

    operations = [
        migrations.CreateModel(
            name='dateStore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('startDate', models.IntegerField(default=0)),
                ('startMonth', models.IntegerField(default=0)),
                ('startYear', models.IntegerField(default=0)),
                ('IslamicMonth', models.IntegerField(default=0)),
                ('IslamicYear', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name_plural': 'IslamicMonth',
            },
        ),
        migrations.DeleteModel(
            name='islamic_date',
        ),
    ]