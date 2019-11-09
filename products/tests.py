from rest_framework.test import APITestCase
from .models import Category
from .api.v1.serializers import CategorySerializer
from django.urls import reverse
from rest_framework import status


class GetAllCategoriesTest(APITestCase):

    def setUp(self):
        Category.objects.create(
            title='test1',
            title_plural='test plural1',
            description='test1 description',
        )

        Category.objects.create(
            title='test2',
            title_plural='test plural2',
            description='test2 description',
        )

    def test_get_all_categories(self):
        response = self.client.get(reverse('products:category_list'))
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)