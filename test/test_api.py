from unittest import TestCase
import requests
from api.model.Figurine import Figurine
from fastapi import status

class Test_Api(TestCase):

    def setUp(self):
        self.url = 'http://127.0.0.1:8000/'
        self.data = {
            "name": "Test1",
            "price": "555€"
        }
        self.dataUpdated = {
            "name": "Test2",
            "price": "666€"
        }

        self.reqCreated = requests.post(self.url, json=self.data)
        self.newFigurine = Figurine(**self.reqCreated.json())

        self.reqGetAll = requests.get(f'{self.url}/GetAll')
        self.figurines = [Figurine(**article) for article in self.reqGetAll.json()]

        self.reqGetbyId = requests.get(f'{self.url}/Figurine/{self.newArticle.id}')
        self.figurine = Figurine(**self.reqGetbyId.json())

        self.reqUpdated = requests.put(f'{self.url}/Figurine/{self.newArticle.id}', json=self.dataUpdated)
        self.reqGetAfterUpdate = requests.get(f'{self.url}/Figurine/{self.newArticle.id}')

        self.figurineAfterUpdate = Figurine(**self.reqGetAfterUpdate.json())

        self.reqDeleted = requests.delete(f'{self.url}/Figurine/{self.newArticle.id}')

        def test_GetAll(self):
            self.assertIsInstance(self.figurines, list)
            self.assertIsInstance(self.figurine, Figurine)
            self.assertEqual(self.reqGetAll.status_code, status.HTTP_200_OK)

        def test_ById(self):
            self.assertIsInstance(self.figurine, Figurine)
            self.assertEqual(self.reqGetById.status_code, status.HTTP_200_OK)

        def test_Post(self):
            self.assertEqual(self.reqCreate.status_code, status.HTTP_201_CREATED)
            self.assertEqual(self.newFigurine, Figurine)

        def test_Update(self):
            self.assertEqual(self.reqUpdate.status_code, status.HTTP_200_OK)
            self.assertEqual(self.figurineAfterUpdate, Figurine)

            self.assertEqual(self.figurineAfterUpdate.name, self.dataUpdated['name'])
            self.assertEqual(self.figurineAfterUpdate.price, self.dataUpdated['price'])

        def test_Deleted(self):
            self.assertEqual(self.reqUpdate.status_code, status.HTTP_200_OK)
