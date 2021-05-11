from django.test import TestCase
from django.urls import reverse

from playground.config import baker
from playground.posts.models import QuillPost


class QuillViewTest(TestCase):
    def test_generic_list_view(self):
        baker.make(QuillPost, _quantity=30)
        response = self.client.get(reverse("posts:quill-post-list"))
        self.assertEqual(response.status_code, 200)

    def test_generic_create_view(self):
        response = self.client.get(reverse("posts:quill-post-create"))
        self.assertEqual(response.status_code, 200)

    def test_generic_detail_view(self):
        quill_post = baker.make(QuillPost)
        response = self.client.get(
            reverse("posts:quill-post-detail", args=[quill_post.id])
        )
        self.assertEqual(response.status_code, 200)


class QuillAdminTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.posts = baker.make(QuillPost, _quantity=30)

    def setUp(self) -> None:
        self.client.login()

    def test_list(self):
        response = self.client.get(reverse("admin:posts_quillpost_changelist"))
        self.assertEqual(response.status_code, 200)

    def test_detail(self):
        response = self.client.get(
            reverse("admin:posts_quillpost_change", args=[self.posts[0].id])
        )
        self.assertEqual(response.status_code, 200)
