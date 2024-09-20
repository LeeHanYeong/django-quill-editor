from django.core import management
from django.test import TestCase
from django.urls import reverse

from config.baker import baker
from django_quill.quill import Quill, QuillParseError
from posts.models import QuillPost, NonQuillPost


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
    def setUp(self) -> None:
        self.client.login()

    def test_list(self):
        baker.make(QuillPost, _quantity=13)
        url = reverse("admin:posts_quillpost_changelist")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_detail(self):
        post = baker.make(QuillPost)
        url = reverse("admin:posts_quillpost_change", args=[post.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)


class ConvertToQuillCommandTest(TestCase):
    def test_command(self):
        dummy_text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut nunc dolor, malesuada in pulvinar et, efficitur non massa. Sed at mi elit. Quisque a dapibus nibh. Nunc ac tristique mi. Nam consectetur lectus ac ipsum euismod ultrices. Interdum et malesuada fames ac ante ipsum primis in faucibus. Mauris condimentum, libero vitae rutrum tristique, nibh urna maximus felis, ac gravida enim velit id erat."
        post_char = baker.make(NonQuillPost, content_char=dummy_text)
        post_text = baker.make(NonQuillPost, content_text=dummy_text)
        with self.assertRaises(QuillParseError):
            Quill(post_char.content_char)
        with self.assertRaises(QuillParseError):
            Quill(post_text.content_text)

        management.call_command(
            "convert_to_quill", "posts", "NonQuillPost", "content_char"
        )
        post_char.refresh_from_db()
        quill = Quill(post_char.content_char)
        self.assertEqual(quill.html, dummy_text)
        with self.assertRaises(QuillParseError):
            Quill(post_text.content_text)

        management.call_command(
            "convert_to_quill", "posts", "NonQuillPost", "content_text"
        )
        post_text.refresh_from_db()
        quill = Quill(post_text.content_text)
        self.assertEqual(quill.html, dummy_text)
