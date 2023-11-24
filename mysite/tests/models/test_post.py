import pytest

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
import django
django.setup()

from blog.factories import PostFactory


@pytest.fixture
def post_published():
    return PostFactory(title='pytest with factory')


@pytest.mark.django_db
def test_create_published_post(post_published):
    assert post_published.title == 'pytest with factory'