# Generated by Django 5.1.1 on 2024-10-02 13:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('outflows', '0002_alter_outflow_created_at_alter_outflow_description_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='outflow',
            options={'ordering': ['-created_at'], 'verbose_name': 'fluxo de saida', 'verbose_name_plural': 'fluxos de saida'},
        ),
    ]
