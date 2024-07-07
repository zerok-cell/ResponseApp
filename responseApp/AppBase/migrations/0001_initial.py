# Generated by Django 5.0.6 on 2024-06-30 10:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tovar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=100, verbose_name='Название')),
                ('date_create', models.DateTimeField(auto_now_add=True, verbose_name='Описание')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
            },
        ),
        migrations.CreateModel(
            name='Response',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=100, verbose_name='Название')),
                ('date_create', models.DateTimeField(auto_now_add=True, verbose_name='Описание')),
                ('text', models.TextField(verbose_name='Содержимое')),
                ('tovar_rel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='responses', to='AppBase.tovar')),
            ],
            options={
                'verbose_name': 'Отзыв',
                'verbose_name_plural': 'Отзывы',
            },
        ),
    ]
