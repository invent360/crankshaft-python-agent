"""
    Swagger Dummy Posts

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import unittest

import openapi_client
from openapi_client.api.posts_api import PostsApi  # noqa: E501


class TestPostsApi(unittest.TestCase):
    """PostsApi unit test stubs"""

    def setUp(self):
        self.api = PostsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_posts(self):
        """Test case for create_posts

        Create a post  # noqa: E501
        """
        pass

    def test_fetch_posts(self):
        """Test case for fetch_posts

        List all posts  # noqa: E501
        """
        pass

    def test_get_post_by_id(self):
        """Test case for get_post_by_id

        Info for a specific post  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
