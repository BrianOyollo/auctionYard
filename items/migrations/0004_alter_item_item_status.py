# Generated by Django 4.2.4 on 2023-09-09 09:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0003_alter_item_item_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='item_status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='item_status', to='items.itemstatus'),
        ),
    ]
