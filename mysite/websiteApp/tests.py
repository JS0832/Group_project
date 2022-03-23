from django.test import TestCase, Client

# Create your tests here.
class RegisterTest(TestCase):
    def setUp(self) -> None:
        self.client1 = Client()
        self.client2 = Client()

    def test_register(self):
        # Inital request should have logged_in be False
        response = self.client1.get('/register/')
        self.assertFalse(response.context['logged_in'], "Default state behaved unexpecedly")
        
        # When the passswords are different the context should reflect that
        response = self.client1.post('/register/', { "email": "abc@example.com"
                                                   , "username": "test_case"
                                                   , "password1": "abc"
                                                   , "password2": "123"})
        self.assertTrue(response.context['password_not_same'], "Non matching passwords accepted")

        # A user shouldn't be able to have no password. TODO: This is currently fails, should be addressed
        response = self.client1.post('/register/', { "email": "abc@example.com"
                                                   , "username": "test_case"
                                                   , "password1": ""
                                                   , "password2": ""})
        self.assertFalse(response.context['logged_in'], "Registered without a password")

        # Fail to login without an email
        response = self.client1.post('/register/', { "email": ""
                                                   , "username": "test_case"
                                                   , "password1": "abc"
                                                   , "password2": "abc"})
        self.assertFalse(response.context['logged_in'], "Registered without an email") 
        # Currently results in not_available with context maybe have a more specific keyword?

        # Fail to login without a username
        response = self.client1.post('/register/', { "email": "abc@example.com"
                                                   , "username": ""
                                                   , "password1": "abc"
                                                   , "password2": "abc"})
        self.assertFalse(response.context['logged_in'], "Registered without a username") 

        response = self.client1.post('/register/', { "email": "abc@example.com"
                                                   , "username": "test_case"
                                                   , "password1": "abc"
                                                   , "password2": "abc"})
        self.assertTrue(response.context['logged_in'], "Registration context not updated")
        self.assertEqual(self.client1.session['username'], "test_case", "Session username incorrect")
        self.assertTrue(self.client1.session['logged_in'], "Session login state incorrect")

        # Attempting to register with an existing username should fail
        response = self.client2.post('/register/', { "email": "abc@example.com"
                                                   , "username": "test_case"
                                                   , "password1": "abc"
                                                   , "password2": "abc"})
        self.assertTrue(response.context['not_available'], "Duplicate account allowed") 
        self.assertFalse(response.context['logged_in'])

class LoginTest(TestCase):
    def setUp(self) -> None:
        setup_client = Client()
        self.email = "abc@example.com"
        self.username = "test_case"
        self.password = "abc"
        setup_client.post('/register/', { "email": self.email
                                        , "username": self.username
                                        , "password1": self.password
                                        , "password2": self.password})
        self.client = Client();

    def test_login(self):
        # Default get request should report logged_in as false in the context
        response = self.client.get('/login/')
        self.assertFalse(response.context['logged_in'], "Incorrect context for default GET request")

        # Attempting to login with with an incorrect username or password should be reflected in the context
        response = self.client.post('/login/', { "username": self.username + "_incorrect"
                                               , "password": self.password})
        self.assertTrue(response.context['invalid_login'], "Incorrect username accepted")
        response = self.client.post('/login/', { "username": self.username
                                               , "password": self.password + "_incorrect"})
        self.assertTrue(response.context['invalid_login'], "Incorrect password accepted")

        # Attempting to login
        response = self.client.post('/login/', { "username": self.username
                                               , "password": self.password})
        self.assertTrue(response.context['logged_in'], "Registration context not updated")
        self.assertEqual(self.client.session['username'], self.username, "Session username incorrect")
        self.assertTrue(self.client.session['logged_in'], "Session login state incorrect")




