from django.test import SimpleTestCase
from django.urls import reverse, resolve
from digital_docs.views import DocumentViewSet, FolderViewSet, TopicViewSet


class TestUrls(SimpleTestCase):
    
    def test_resolve_documents_router_url(self):
        """ To test whether router url for 'documents' are resolved propely"""

        url = reverse('documents-list')

        print(resolve(url).func)

        self.assertEquals(resolve(url).func.__name__, DocumentViewSet.__name__)

    def test_resolve_folders_router_url(self):
        """ To test whether router url for 'folders' are resolved propely"""

        url = reverse('folders-list')

        print(resolve(url).func)

        self.assertEquals(resolve(url).func.__name__, FolderViewSet.__name__)
    
    def test_resolve_topics_router_url(self):
        """ To test whether router url for 'topics' are resolved propely"""

        url = reverse('topics-list')

        print(resolve(url).func)

        self.assertEquals(resolve(url).func.__name__, TopicViewSet.__name__)
