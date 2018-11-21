import os
import unittest
 
from app import app
 
class TestApp(unittest.TestCase): 

    @classmethod
    def setUpClass(cls):
        pass 

    @classmethod
    def tearDownClass(cls):
        pass 

    def setUp(self):
        # cliente de pruebas
        self.app = app.test_client()
        
        self.app.testing = True 

    def tearDown(self):
        pass 

    #Asegurarse que flask funciona correctamente
    def test_home_status_code(self):

        resp = self.app.get('/') 

        self.assertEqual(resp.status_code, 200)

    #Asegurarse que el login funciona correctamente
    def test_correct_login(self):
        with self.app:
            response = self.app.post(
                '/login',
                data=dict(username="admin", password="admin"),
                follow_redirects=True
            )
            
            self.assertTrue(response.data, "admin")

 
if __name__ == "__main__":
    unittest.main()
