from django.test import TestCase
from django.urls import reverse

from config import baker
from posts.models import UEPost


class UEViewTest(TestCase):
    def test_generic_list_view(self):
        baker.make(UEPost, _quantity=30)
        response = self.client.get(reverse("posts:ueditor-post-list"))
        self.assertEqual(response.status_code, 200)

    def test_generic_create_view(self):
        response = self.client.get(reverse("posts:ueditor-post-create"))
        self.assertEqual(response.status_code, 200)

    def test_generic_detail_view(self):
        ueditor_post = baker.make(UEPost)
        response = self.client.get(
            reverse("posts:ueditor-post-detail", args=[ueditor_post.id])
        )
        self.assertEqual(response.status_code, 200)


class UEAdminTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.posts = baker.make(UEPost, _quantity=30)

    def setUp(self) -> None:
        self.client.login()

    def test_list(self):
        response = self.client.get(reverse("admin:posts_ueditorpost_changelist"))
        self.assertEqual(response.status_code, 200)

    def test_detail(self):
        response = self.client.get(
            reverse("admin:posts_ueditorpost_change", args=[self.posts[0].id])
        )
        self.assertEqual(response.status_code, 200)
