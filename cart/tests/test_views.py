from django.test import TestCase
from django.urls import reverse

from store.models import Category, Product
from users.models import UserBase


class TestCartView(TestCase):
    def setUp(self):
        self.user1 = UserBase.objects.create(user_name="admin", email="a@a.com")
        self.user2 = UserBase.objects.create(user_name="admin2", email="b@b.com")
        self.category1 = Category.objects.create(name="django", slug="django")
        data1 = Product.objects.create(
            category=self.category1,
            title="django beginners",
            created_by=self.user1,
            slug="django-beginners",
            price="20.00",
            image="django",
        )
        data2 = Product.objects.create(
            category=self.category1,
            title="django intermediate",
            created_by=self.user1,
            slug="django-beginners",
            price="20.00",
            image="django",
        )
        data3 = Product.objects.create(
            category=self.category1,
            title="django advanced",
            created_by=self.user1,
            slug="django-beginners",
            price="20.00",
            image="django",
        )
        self.client.post(reverse("cart:cart_add"), {"productid": 1, "productqty": 1, "action": "post"}, xhr=True)
        self.client.post(reverse("cart:cart_add"), {"productid": 2, "productqty": 2, "action": "post"}, xhr=True)

    def test_basket_url(self):
        """
        Test homepage response status
        """
        response = self.client.get(reverse("cart:cart_summary"))
        self.assertEqual(response.status_code, 200)

    def test_cart_add(self):
        """
        Test adding items to the cart
        """
        response = self.client.post(reverse("cart:cart_add"), {"productid": 3, "productqty": 1, "action": "post"}, xhr=True)
        self.assertEqual(response.json(), {"qty": 4})
        response = self.client.post(reverse("cart:cart_add"), {"productid": 2, "productqty": 1, "action": "post"}, xhr=True)
        self.assertEqual(response.json(), {"qty": 3})

    def test_cart_remove(self):
        """
        Test removing items from the cart
        """
        response = self.client.post(
            reverse('cart:cart_remove'), {"productid": 2, "action": "post"}, xhr=True)
        self.assertEqual(response.json(), {'qty': 1, 'subtotal': '31.50'})

    def test_cart_update(self):
        """
        Test updating items from the cart
        """
        response = self.client.post(
            reverse('cart:cart_update'), {"productid": 2, "productqty": 1, "action": "post"}, xhr=True)
        self.assertEqual(response.json(), {'qty': 2, 'subtotal': '51.50'})
