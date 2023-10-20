from django.test import TestCase
from django.urls import reverse

from store.models import Category, Product
from users.models import UserBase


class TestCategoriesModel(TestCase):
    def setUp(self):
        self.data1 = Category.objects.create(name="django", slug="django")

    def test_category_model_entry(self):
        """
        Test Category model data insertion/types/field attributes
        """
        data = self.data1
        self.assertTrue(isinstance(data, Category))
        self.assertEqual(str(data), "django")

    def test_category_url(self):
        """
        Test category model slug and URL reverse
        """
        data = self.data1
        response = self.client.post(reverse("store:category_list", args=[data.slug]))
        self.assertEqual(response.status_code, 200)


class TestProductsModel(TestCase):
    def setUp(self):
        self.category1 = Category.objects.create(name="django", slug="django")
        self.category2 = Category.objects.create(name="javascript", slug="js")
        self.user1 = UserBase.objects.create(user_name="admin", email="admin@example.com")
        self.user2 = UserBase.objects.create(user_name="admin2", email="admin2@example.com")
        self.data11 = Product.objects.create(
            category=self.category1,
            title="django beginners",
            created_by=self.user1,
            slug="django-beginners",
            price="20.00",
            image="django",
        )
        self.data12 = Product.objects.create(
            category=self.category1,
            title="django advanced",
            created_by=self.user2,
            slug="django-advanced",
            price="20.00",
            image="django",
            is_active=False,
        )
        self.data13 = Product.objects.create(
            category=self.category1,
            title="django intermediate",
            created_by=self.user1,
            slug="django-intermediate",
            price="20.00",
            image="django",
            is_active=False,
        )
        self.data21 = Product.objects.create(
            category=self.category2,
            title="js beginners",
            created_by=self.user2,
            slug="js-beginners",
            price="20.00",
            image="js",
        )
        self.data21 = Product.objects.create(
            category=self.category2,
            title="js intermediate",
            created_by=self.user2,
            slug="js-intermediate",
            price="20.00",
            image="js",
            is_active=False,
        )
        self.data21 = Product.objects.create(
            category=self.category2,
            title="js advanced",
            created_by=self.user2,
            slug="js-advanced",
            price="20.00",
            image="js",
        )

    def test_products_model_entry(self):
        """
        Test product model data insertion/types/field attributes
        """
        data = self.data11
        self.assertTrue(isinstance(data, Product))
        self.assertEqual(str(data), "django beginners")

    def test_products_url(self):
        """
        Test product model slug and URL reverse
        """
        data = self.data11
        url = reverse("store:product_detail", args=[data.slug])
        self.assertEqual(url, "/item/django-beginners/")
        response = self.client.post(reverse("store:product_detail", args=[data.slug]))
        self.assertEqual(response.status_code, 200)

    def test_products_custom_manager_basic(self):
        """
        Test product model custom manager returns only active products
        """
        data = Product.objects.all().filter(is_active=True)
        self.assertEqual(data.count(), 3)

    def test_product_categories(self):
        """
        Test that each selecting products by category only returns products in that category
        """
        data = self.category1.product.all()
        self.assertEqual(data.count(), 3)

    def test_product_creator(self):
        """
        Test that selecting products by `created_by` only returns products created by that user
        """
        data = self.user1.product_creator.all()
        self.assertEqual(data.count(), 2)
