import unittest

from SW5.dummyjson_requests.posts import PostsRequests


class TestPostsRequests(unittest.TestCase):

    def setUp(self):
        self.posts_req = PostsRequests()

    def test_get_all_posts(self):
        response = self.posts_req.get_all_posts()
        response_msg = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_msg["total"], 150)
