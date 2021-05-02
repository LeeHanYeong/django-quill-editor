from django.test import TestCase, Client
from django.urls import reverse
from testproject.baker import baker
from django.contrib.auth import get_user_model

# from django.contrib.auth.models import User

from .models import QuillPost, QuillMaster, QuillDetail


class QuillViewTest(TestCase):
    def test_generic_list_view(self):
        baker.make(QuillPost, _quantity=30)
        response = self.client.get(reverse('posts:quill-post-list'))
        self.assertEqual(response.status_code, 200)

    def test_generic_create_view(self):
        response = self.client.get(reverse('posts:quill-post-create'))
        self.assertEqual(response.status_code, 200)

    def test_generic_detail_view(self):
        quill_post = baker.make(QuillPost)
        response = self.client.get(reverse('posts:quill-post-detail', args=[quill_post.id]))
        self.assertEqual(response.status_code, 200)


class QuillAdminTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.posts = baker.make(QuillPost, _quantity=30)
        cls.posts_detail = baker.make(QuillDetail, _quantity=30)

    def setUp(self) -> None:
        User = get_user_model()

        test_user = User(username='admin', is_staff=True)
        test_user.is_superuser = True
        test_user.save()

        self.client.force_login(test_user, backend=None)

    def test_list(self):
        response = self.client.get(reverse('admin:post_quillpost_changelist'))
        self.assertEqual(response.status_code, 200)

    def test_master_list(self):
        response = self.client.get(reverse('admin:post_quillmaster_changelist'))
        self.assertEqual(response.status_code, 200)

    def test_detail(self):
        response = self.client.get(reverse('admin:post_quillpost_change', args=[self.posts[0].id]))
        self.assertEqual(response.status_code, 200)

    def test_master_detail(self):
        response = self.client.get(reverse('admin:post_quillmaster_change', args=[self.posts_detail[0].id]))
        self.assertEqual(response.status_code, 200)