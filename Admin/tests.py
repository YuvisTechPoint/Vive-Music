from django.test import TestCase
from django.contrib.auth.models import User
from django.db.models.signals import post_save

from Admin.realtime.signals import user_created_signal



class AdminLoginTests(TestCase):
	def setUp(self):
		post_save.disconnect(user_created_signal, sender=User)
		self.addCleanup(post_save.connect, user_created_signal, sender=User, weak=False)

		self.admin_user = User.objects.create_user(
			username='admin',
			email='admin@example.com',
			password='secure-pass-123',
		)
		self.admin_user.is_staff = True
		self.admin_user.is_superuser = True
		self.admin_user.save()

	def test_admin_login_with_username_stores_username(self):
		response = self.client.post(
			'/admin/accounts/login/',
			{'username': 'admin', 'password': 'secure-pass-123'},
		)

		self.assertRedirects(response, '/admin/')
		self.assertEqual(self.client.session['adminuser'], 'admin')

	def test_admin_login_with_email_stores_username(self):
		response = self.client.post(
			'/admin/accounts/login/',
			{'username': 'admin@example.com', 'password': 'secure-pass-123'},
		)

		self.assertRedirects(response, '/admin/')
		self.assertEqual(self.client.session['adminuser'], 'admin')
