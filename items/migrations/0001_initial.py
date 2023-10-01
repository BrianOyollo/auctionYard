# Generated by Django 4.2.4 on 2023-10-01 19:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=150, verbose_name='Title')),
                ('description', models.TextField(verbose_name='Item description')),
                ('reserve_price', models.FloatField(blank=True, default=0, null=True)),
                ('cover_photo', models.ImageField(default='no_picture.jpg', upload_to='cover_photos/')),
                ('date_posted', models.DateTimeField(auto_now_add=True, verbose_name='Date Posted')),
            ],
            options={
                'verbose_name_plural': 'Items',
            },
        ),
        migrations.CreateModel(
            name='ItemCategory',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('category', models.CharField(max_length=150, verbose_name='Category')),
                ('description', models.TextField(max_length=250, verbose_name='Category description')),
            ],
            options={
                'verbose_name_plural': 'Item Categories',
            },
        ),
        migrations.CreateModel(
            name='ItemStatus',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('status', models.CharField(choices=[('Available', 'Available'), ('Sold', 'Sold')], default='Available', max_length=150, verbose_name='Status')),
                ('description', models.TextField(max_length=250, verbose_name='Status description')),
            ],
            options={
                'verbose_name_plural': 'Item Status',
            },
        ),
        migrations.CreateModel(
            name='ReserveStatus',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('status', models.CharField(choices=[('Reserve', 'Reserve'), ('No Reserve', 'No Reserve')], max_length=150, verbose_name='Status')),
                ('description', models.TextField(max_length=250, verbose_name='Status description')),
            ],
            options={
                'verbose_name_plural': 'Reserve Status',
            },
        ),
        migrations.CreateModel(
            name='itemImages',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('image', models.ImageField(upload_to='item_images/')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='image_item', to='items.item')),
            ],
            options={
                'verbose_name_plural': 'Item Images',
            },
        ),
        migrations.AddField(
            model_name='item',
            name='item_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='item_category', to='items.itemcategory'),
        ),
        migrations.AddField(
            model_name='item',
            name='item_status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='item_status', to='items.itemstatus'),
        ),
        migrations.AddField(
            model_name='item',
            name='reserve_status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='item_reserve_status', to='items.reservestatus'),
        ),
        migrations.AddField(
            model_name='item',
            name='seller',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seller', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('comment', models.TextField(verbose_name='Comment')),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_item', to='items.item')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Comments',
            },
        ),
        migrations.CreateModel(
            name='Bid',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('bid_amount', models.FloatField(verbose_name='Bid Amount')),
                ('bid_time', models.DateTimeField(auto_now_add=True)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bid_item', to='items.item')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bidder', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Bids',
            },
        ),
    ]
