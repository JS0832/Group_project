from django.test import TestCase, Client

# Create your tests here.
class AccountTest(TestCase):
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


