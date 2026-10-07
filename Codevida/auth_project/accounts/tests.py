from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.core import mail
from django.test import TestCase, override_settings
from django.urls import reverse


class AuthenticationTests(TestCase):
    def test_registration_hashes_password_and_assigns_regular_role(self):
        response = self.client.post(
            reverse('accounts:register'),
            {
                'username': 'newuser',
                'email': 'newuser@example.com',
                'password1': 'A-strong-test-password-53!',
                'password2': 'A-strong-test-password-53!',
            },
        )

        self.assertRedirects(response, reverse('accounts:dashboard'))
        user = get_user_model().objects.get(username='newuser')
        self.assertTrue(user.check_password('A-strong-test-password-53!'))
        self.assertNotEqual(user.password, 'A-strong-test-password-53!')
        self.assertFalse(user.is_staff)
        self.assertIn(Group.objects.get(name='Regular user'), user.groups.all())

    def test_login_and_post_logout(self):
        user = get_user_model().objects.create_user(
            username='member', password='A-strong-test-password-53!'
        )

        response = self.client.post(
            reverse('accounts:login'),
            {'username': user.username, 'password': 'A-strong-test-password-53!'},
        )
        self.assertRedirects(response, reverse('accounts:dashboard'))
        self.assertEqual(self.client.get(reverse('accounts:dashboard')).status_code, 200)

        response = self.client.post(reverse('accounts:logout'))
        self.assertRedirects(response, reverse('accounts:login'))
        self.assertRedirects(
            self.client.get(reverse('accounts:dashboard')),
            f"{reverse('accounts:login')}?next={reverse('accounts:dashboard')}",
        )

    def test_only_staff_users_can_access_admin(self):
        regular_user = get_user_model().objects.create_user(
            username='member', password='A-strong-test-password-53!'
        )
        self.client.force_login(regular_user)
        self.assertEqual(self.client.get(reverse('admin:index')).status_code, 302)

        administrator = get_user_model().objects.create_user(
            username='administrator',
            password='A-strong-test-password-53!',
            is_staff=True,
        )
        self.client.force_login(administrator)
        self.assertEqual(self.client.get(reverse('admin:index')).status_code, 200)

    @override_settings(EMAIL_BACKEND='django.core.mail.backends.locmem.EmailBackend')
    def test_password_reset_sends_email(self):
        get_user_model().objects.create_user(
            username='member',
            email='member@example.com',
            password='A-strong-test-password-53!',
        )

        response = self.client.post(
            reverse('accounts:password_reset'), {'email': 'member@example.com'}
        )

        self.assertRedirects(response, reverse('accounts:password_reset_done'))
        self.assertEqual(len(mail.outbox), 1)
        self.assertIn('password-reset/confirm/', mail.outbox[0].body)