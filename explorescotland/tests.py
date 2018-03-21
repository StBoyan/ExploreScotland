from django.test import TestCase, RequestFactory
from django.core.urlresolvers import reverse
from explorescotland.models import *
from explorescotland.forms import *
from django.contrib.auth.models import User
from explorescotland import views
from django.test.client import Client

# Tests in this class test if pages are restricted to
# authenticated users (i.e. if unauthenticated, user
# gets redirected to another page)
class UnauthenticatedAccessViewRedirectTests(TestCase):
    def test_parent_area_inacessible_without_login(self):
        response = self.client.get(reverse('parent_area'))
        self.assertEqual(response.status_code, 302)

    def test_view_profile_inacessible_without_login(self):
        response = self.client.get(reverse('view_profile'))
        self.assertEqual(response.status_code, 302)

    def test_edit_profile_inacessible_without_login(self):
        response = self.client.get(reverse('edit_profile'))
        self.assertEqual(response.status_code, 302)

    def test_feedback_inacessible_without_login(self):
        response = self.client.get(reverse('feedback'))
        self.assertEqual(response.status_code, 302)

    def test_scot_inacessible_without_login(self):
        response = self.client.get(reverse('scot'))
        self.assertEqual(response.status_code, 302)

    def test_lily_inacessible_without_login(self):
        response = self.client.get(reverse('lily'))
        self.assertEqual(response.status_code, 302)

    def test_map_inacessible_without_login(self):
        response = self.client.get(reverse('googlemap'))
        self.assertEqual(response.status_code, 302)

    def test_children_area_inacessible_without_login(self):
        response = self.client.get(reverse('children_area'))
        self.assertEqual(response.status_code, 302)

# Tests in this class test if forms process information
# correctly and database works correctly
class FormsAndDatabaseTests(TestCase):
    # Provides a test user instance
    def setUp(self):
        self.user = User.objects.create_user(
                    username='John',
                    email='john@test.com',
                    password='test_password')

    def test_feedback_form(self):
        test_text = 'Your website is awesome!'
        form_data = {'message': test_text}
        test_feedback = Feedback(parent=self.user)
        form = FeedbackForm(data=form_data, instance=test_feedback)
        self.assertTrue(form.is_valid())

    def test_add_child_form(self):
        test_child = 'Bob'
        form_data = {'name': test_child}
        test_childprofile = ChildProfile(parent=self.user)
        form = ChildForm(data=form_data, instance=test_childprofile)
        self.assertTrue(form.is_valid())

    def test_children_start_at_level_one(self):
        child = ChildProfile(name='Dave', parent=self.user)
        child.save()
        self.assertEqual((child.level), 1)

    def test_parent_profile_is_created(self):
        parent_profile = ParentProfile.objects.get(user=self.user)
        self.assertIsNotNone(parent_profile)

# Tests in this class test if views are accessible for authenticated
# users and information is displayed correctly
class AuthenticatedViewTests(TestCase):
    # Provides a test user instance
    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()
        self.user = User.objects.create_user(
                            username='John',
                            email='john@test.com',
                            password='test_password')
        self.client.login(username='John', password='test_password')

    def test_view_children_with_no_children(self):
        response = self.client.get(reverse('view_children'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['children'], [])

    def test_feedback_is_accessible_for_loggedin_user(self):
        response = self.client.get(reverse('feedback'))
        self.assertEqual(response.status_code, 200)

    def test_view_profile_is_accessible_for_loggedin_user(self):
        response = self.client.get(reverse('view_profile'))
        self.assertEqual(response.status_code, 200)

    def test_edit_profile_is_accessible_for_loggedin_user(self):
        response = self.client.get(reverse('edit_profile'))
        self.assertEqual(response.status_code, 200)

    def test_manage_children_is_accessible_for_loggedin_user(self):
        response = self.client.get(reverse('manage_children'))
        self.assertEqual(response.status_code, 200)

    def test_parent_area_is_accessible_for_loggedin_user(self):
        response = self.client.get(reverse('parent_area'))
        self.assertEqual(response.status_code, 200)

    def test_lily_is_accessible_for_loggedin_user(self):
        response = self.client.get(reverse('lily'))
        self.assertEqual(response.status_code, 302)

    def test_scot_is_accessible_for_loggedin_user(self):
        response = self.client.get(reverse('scot'))
        self.assertEqual(response.status_code, 302)

    def test_googlemap_is_accessible_for_loggedin_user(self):
        response = self.client.get(reverse('googlemap'))
        self.assertEqual(response.status_code, 302)

    def test_children_area_is_accessible_for_loggedin_user(self):
        response = self.client.get(reverse('children_area'))
        self.assertEqual(response.status_code, 200)

# Tests in this class test whether the view content
# is displayed correctly
class ViewContentTests(TestCase):
    # Provides a test user instance
    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()
        self.user = User.objects.create_user(
                            username='John',
                            email='john@test.com',
                            password='test_password')
        self.client.login(username='John', password='test_password')

    def test_children_area_without_children(self):
        response = self.client.get(reverse('children_area'))
        self.assertContains(response, 'You havent registered any children yet!')
        self.assertQuerysetEqual(response.context['children'], [])

    def test_view_children_without_children(self):
        response = self.client.get(reverse('view_children'))
        self.assertContains(response, 'You havent registered any children yet!')
        self.assertQuerysetEqual(response.context['children'], [])

    def test_profile_page_displays_correct_data(self):
        response = self.client.get(reverse('view_profile'))
        self.assertEqual(response.context['user'], self.user)

    def test_children_area_with_children(self):
        add_child(self.user, 'Bobby')
        response = self.client.get(reverse('children_area'))
        self.assertTrue(response.context['children'] != [])

    def test_view_children_with_children(self):
        response = self.client.get(reverse('children_area'))
        self.assertTrue(response.context['children'] != [])

# Helper function to create child profile
def add_child(parent, name):
    child = ChildProfile.objects.get_or_create(parent=parent, name=name)[0]
    child.save()

    return child
