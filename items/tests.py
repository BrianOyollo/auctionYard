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

        self.buyer = user.objects.create_user(
            username = 'john',
            email = 'johndoe@gmail.com',
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
            status = 'Available',
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

        self.comment = Comment.objects.create(
            item = self.item,
            user = self.buyer,
            comment = "Looks neat!",
            time = date_posted
        )

        self.bid  = Bid.objects.create(
            item = self.item,
            user = self.buyer,
            bid_amount = 30000,
            bid_time = date_posted
        )


    def test_itemCategories(self):
        self.assertEqual(f'{self.item_category.category}', 'Electronics')
        self.assertEqual(f'{self.item_category.description}', 'Electronic device controls the flow of electrons for performing a particular task')

    def test_reserveStatus(self):
        self.assertEqual(f'{self.reserve_status.status}', 'Reserve')
        self.assertEqual(f'{self.reserve_status.description}', 'An auction reserve is the minimum price the seller is willing to accept for an item')

    def test_itemStatus(self):
        self.assertEqual(f'{self.item_status.status}', 'Available')
        self.assertEqual(f'{self.item_status.description}', 'The item is available for bidding')

    def test_item(self):
        self.assertEqual(f'{self.item.title}', 'Lenovo ThinkPad T470s Core i7 16GB RAM 512GB SSD 7th gen')
        self.assertEqual(f'{self.item.description}', 'Lenovo ThinkPad T470s- has a screen-sized of 14 Inches . It has DDR4 type 16 GB RAM and 512GB SSD Internal storage')
        self.assertEqual(f"{self.item.item_category}",'Electronics')
        self.assertEqual(f'{self.item.reserve_status}',"Reserve")
        self.assertEqual(f'{self.item.item_status}',"Available")
        self.assertEqual(self.item.reserve_price,10000)
        self.assertEqual(self.item.seller.username,'brian' )
        self.assertAlmostEqual(self.item.date_posted,date_posted, delta=timedelta(seconds=4))
    
    def test_comments(self):
        self.assertEqual(self.comment.item.title, 'Lenovo ThinkPad T470s Core i7 16GB RAM 512GB SSD 7th gen')
        self.assertEqual(self.comment.user.username, 'john')
        self.assertEqual(self.comment.comment,'Looks neat!' )
        self.assertAlmostEqual(self.comment.time, date_posted, delta=timedelta(seconds=3))
        
    def test_bidding(self):
        self.assertEqual(self.bid.item.title, 'Lenovo ThinkPad T470s Core i7 16GB RAM 512GB SSD 7th gen')
        self.assertEqual(self.bid.user.username, 'john')
        self.assertEqual(self.bid.bid_amount, 30000)
        self.assertAlmostEqual(self.bid.bid_time, date_posted, delta=timedelta(seconds=3))