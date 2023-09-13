from django.test import TestCase
from .models import ItemCategory, ReserveStatus, ItemStatus, Item, Comment, Bid
from django.contrib.auth import get_user_model
from django.utils import timezone
from datetime import timedelta

date_posted = timezone.now()

# Create your tests here.
class ItemTests(TestCase):

    def setUp(self):

        user = get_user_model()

        self.seller = user.objects.create_user(
            username = 'brian',
            email = 'bo@gmail.com',
            password = 'testpass123'
        )

        self.item_category = ItemCategory.objects.create(
            category = 'Electronics',
            description = 'Electronic device controls the flow of electrons for performing a particular task'
        )

        self.reserve_status = ReserveStatus.objects.create(
            status = 'Reserve',
            description = 'An auction reserve is the minimum price the seller is willing to accept for an item'
        )

        self.item_status = ItemStatus.objects.create(
            status = 'available',
            description = 'The item is available for bidding'
        )

        self.item = Item.objects.create(
            title = 'Lenovo ThinkPad T470s Core i7 16GB RAM 512GB SSD 7th gen',
            description = 'Lenovo ThinkPad T470s- has a screen-sized of 14 Inches . It has DDR4 type 16 GB RAM and 512GB SSD Internal storage',
            item_category = self.item_category,
            reserve_status = self.reserve_status,
            item_status = self.item_status,
            reserve_price = 10000,
            seller = self.seller,
            date_posted = date_posted

        )

    def test_itemCategories(self):
        self.assertEqual(f'{self.item_category.category}', 'Electronics')
        self.assertEqual(f'{self.item_category.description}', 'Electronic device controls the flow of electrons for performing a particular task')

    def test_reserveStatus(self):
        self.assertEqual(f'{self.reserve_status.status}', 'Reserve')
        self.assertEqual(f'{self.reserve_status.description}', 'An auction reserve is the minimum price the seller is willing to accept for an item')

    def test_itemStatus(self):
        self.assertEqual(f'{self.item_status.status}', 'available')
        self.assertEqual(f'{self.item_status.description}', 'The item is available for bidding')

    def test_item(self):
        self.assertEqual(f'{self.item.title}', 'Lenovo ThinkPad T470s Core i7 16GB RAM 512GB SSD 7th gen')
        self.assertEqual(f'{self.item.description}', 'Lenovo ThinkPad T470s- has a screen-sized of 14 Inches . It has DDR4 type 16 GB RAM and 512GB SSD Internal storage')
        self.assertEqual(f'{self.item.item_category}',self.item_category.category)
        self.assertEqual(f'{self.item.reserve_status}',self.reserve_status.status)
        self.assertEqual(f'{self.item.item_status}',self.item_status.status)
        self.assertEqual(self.item.reserve_price,10000)
        self.assertEqual(self.item.seller,self.seller )
        self.assertAlmostEqual(self.item.date_posted,date_posted, delta=timedelta(seconds=2))
