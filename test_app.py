import unittest
from app import app

class TestApp(unittest.TestCase):

    def setUp(self):
        # Создаем клиент Flask для отправки запросов
        self.app = app.test_client()
        self.app.testing = True

    def test_upload_csv(self):
        # Тест загрузки CSV-файла
        response = self.app.post('/upload', data={'file': open('test.csv', 'rb')})
        data = response.get_json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['message'], 'CSV file uploaded successfully')

    def test_get_file_list(self):
        # Тест получения списка файлов
        response = self.app.get('/files')
        data = response.get_json()

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(data['files'], list)

    def test_get_data(self):
        # Тест получения данных из файла
        response = self.app.get('/data/test.csv')
        data = response.get_json()

        self.assertEqual(response.status_code, 200)

    

    
    

if __name__ == '__main__':
    unittest.main()
