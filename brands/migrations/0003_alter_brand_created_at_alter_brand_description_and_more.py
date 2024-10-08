# Generated by Django 5.1 on 2024-08-12 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brands', '0002_rename_brands_brand'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='criado em'),
        ),
        migrations.AlterField(
            model_name='brand',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='descrição'),
        ),
        migrations.AlterField(
            model_name='brand',
            name='name',
            field=models.CharField(max_length=100, verbose_name='nome'),
        ),
        migrations.AlterField(
            model_name='brand',
            name='slug',
            field=models.SlugField(verbose_name='slug'),
        ),
        migrations.AlterField(
            model_name='brand',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='atualizado em'),
        ),
    ]
