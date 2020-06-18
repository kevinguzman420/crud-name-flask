# app/test/test_blog_client

from app.models import UserName
from . import BaseTestClass

class UserIndexTestCase(BaseTestClass):

    def test_index_with_no_users(self):
        res = self.client.get("/") # Path to test
        self.assertEqual(200, res.status_code)
        self.assertIn(b'There are no users', res.data)

    # PENDIENTE DE REALIZAR UN TEST, PARA VERIFICAR SI EL INGRESAR UN USUARIO, SE MUESTRA EL MENSAJE DE "EXITO"
    # def test_create_user_show_message(self):
    #     with self.app.app_context():
    #         user = UserName(name="ExampleName", email="exampleemail@xyz.com", phone="3393993")
    #         user.save()
    #     res = self.client.get("/")
    #     # self.assertEqual(200, res.status_code)
    #     self.assertEqual('User has been saved successfully.', res.data)

