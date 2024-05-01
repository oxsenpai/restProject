from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Product, Category, Firm, Order, OrderItem
from .serializers import ProductSerializer

class StoreTests(APITestCase):
    def setUp(self) -> None:
        self.category = Category.objects.create(name = 'Тестовая категория')
        self.firm = Firm.objects.create(name = 'Тестовая фирма')
        self.product = Product.objects.create(category = self.category, firm = self.firm, name = 'Тестовый диван', price = '9999.00')
        self.order = Order.objects.create(country = 'Россия', first_name = 'Данил', last_name = 'Лаврентьев', company_name = 'Тест', email = 'test@mail.ru', phone = '+79240209216', address = 'Тестовый адрес', postal_code = '123', city = 'Чита', order_notes = 'Тест')
        self.orderitem = OrderItem.objects.create(order = self.order, product = self.product)
        self.user = User.objects.create_user('testUser', 'test@test.com')


    def test_anonymous_user_orders(self):
        response = self.client.get('/api/orders/', format = 'json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


    def test_get_products_list(self):
        self.client.force_login(self.user)
        response = self.client.get('/api/products/', format = 'json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        product_serializer = ProductSerializer(Product.objects.all(), many = True)
        self.assertListEqual(response.data, product_serializer.data)

    
    def test_post_orderitem(self):
        self.client.force_login(self.user)
        response = self.client.post('/api/orderitems/', {'order': self.order.id, 'product': self.product.id, 'price': '5000.00', 'quantity': 2}, format = 'json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    

    def test_post_categories(self):
        self.client.force_login(self.user)
        response = self.client.post('/api/categories/', {'name': self.category.name}, format = 'json')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)


from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import WebDriver


class MySeleniumTests(StaticLiveServerTestCase):
    fixtures = ['products.json']

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = WebDriver()
        cls.selenium.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def test_products_page(self):
        self.selenium.get(f"{self.live_server_url}/")
        elements = self.selenium.find_elements(By.XPATH, '//div')
        for element in elements:
            self.assertIn(element.text, list(map(lambda b: b.name, Category.objects.all())))
