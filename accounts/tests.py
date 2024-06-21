from django.contrib.auth import get_user_model
from django.test import TestCase


class CustomUserTests(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username="sasha", email="sasha@email.com", password="qwerty123"
        )
        self.assertEqual(user.username, "sasha")
        self.assertEqual(user.email, "sasha@email.com")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            username="supersasha", email="supersasha@email.com", password="qwerty123"
        )
        self.assertEqual(admin_user.username, "supersasha")
        self.assertEqual(admin_user.email, "supersasha@email.com")
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
