# Generated by Django 4.2.4 on 2023-09-09 09:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bid',
            options={'verbose_name_plural': 'Bids'},
        ),
        migrations.AlterModelOptions(
            name='itemcategory',
            options={'verbose_name_plural': 'Item Categories'},
        ),
        migrations.AlterModelOptions(
            name='itemstatus',
            options={'verbose_name_plural': 'Item Status'},
        ),
        migrations.AlterModelOptions(
            name='reservestatus',
            options={'verbose_name_plural': 'Reserve Status'},
        ),
        migrations.AlterField(
            model_name='item',
            name='item_status',
            field=models.ForeignKey(choices=[('available', 'Available'), ('sold', 'Sold')], default='available', max_length=150, on_delete=django.db.models.deletion.CASCADE, related_name='item_status', to='items.itemstatus'),
        ),
        migrations.AlterField(
            model_name='itemstatus',
            name='status',
            field=models.CharField(choices=[('available', 'Available'), ('sold', 'Sold')], max_length=150, verbose_name='Status'),
        ),
    ]