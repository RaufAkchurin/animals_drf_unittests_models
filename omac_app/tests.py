from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_204_NO_CONTENT
from rest_framework.test import APITestCase
from rest_framework.reverse import reverse

from omac_app.models import Animal, Breed, AnimalType


class AnimalListTestCase(APITestCase):
    def setUp(self):
        self.url = reverse("v1:animal")
        # prepare date without Factories
        self.type1 = AnimalType.objects.create(
            name='name'
        )

        self.breed1 = Breed.objects.create(
            name="first",
            type=self.type1
        )

        self.animal1 = Animal.objects.create(
            inventory_num=11223,
            sex="F",
            nickname="aqaqaq",
            arrival_date="2023-07-12",
            arrival_age=22,
            breed=self.breed1
        )

    def test_url(self):
        self.assertEqual(self.url, "/v1/omac/animal")

    def test_list_count(self):
        self.assertEqual(Animal.objects.all().count(), 1)
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_retrieve(self):
        retrieve_url = f"{self.url}/{self.animal1.id}/"
        response = self.client.get(retrieve_url)
        self.assertEqual(response.status_code, HTTP_200_OK)

        self.assertEqual(response.data["id"], 1)
        self.assertEqual(response.data["sex"], "F")
        self.assertEqual(response.data["nickname"], "aqaqaq")
        self.assertEqual(response.data["arrival_date"], "2023-07-12")
        self.assertEqual(response.data["arrival_age"], 22)
        self.assertEqual(response.data["breed"], self.breed1.id)
        self.assertEqual(len(response.data), 8)

    def test_create(self):
        response = self.client.post(self.url, data={
            "inventory_num": 112232,
            "sex": "F",
            "nickname": "aqaqaq",
            "arrival_date": "2023-07-12",
            "arrival_age": 22,
            "breed": self.breed1.id
        })

        self.assertEqual(response.status_code, HTTP_201_CREATED, response.data)
        self.assertEqual(Animal.objects.all().count(), 2)

        # test_number_validation
        response = self.client.post(self.url, data={
            "inventory_num": 112232,
            "sex": "F",
            "nickname": "aqaqaq",
            "arrival_date": "2023-07-12",
            "arrival_age": 22,
            "breed": self.breed1.id
        })

        self.assertEqual(response.status_code, HTTP_400_BAD_REQUEST, response.data)
        self.assertEqual(response.data["inventory_num"][0],
                         'animal with this inventory num already exists.')

    def test_delete(self):
        self.assertEqual(Animal.objects.all().count(), 1)
        delete_url = f"{self.url}/{self.animal1.id}/"
        response = self.client.delete(delete_url)
        self.assertEqual(response.status_code, HTTP_204_NO_CONTENT)
        self.assertEqual(Animal.objects.all().count(), 0)
