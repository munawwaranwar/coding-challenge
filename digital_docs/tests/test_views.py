from django.urls import reverse
from digital_docs.models import Topic, Folder, Document
from rest_framework.test import APITestCase
from rest_framework import status


class TestViews(APITestCase):

    def test_topic_POST(self):
        """To test the POST API by inserting new topic"""

        url = reverse('topics-list')

        data = {"id": 1, "topic_name": "careers"}

        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Topic.objects.count(), 1)
        self.assertEqual(Topic.objects.get().topic_name, 'careers')

    def test_topic_list_GET(self):
        """To test the GET API where we check the list of Topics"""

        self.topic1 = Topic.objects.create(
            id=1,
            topic_name='SpekiLove!'
        )

        self.topic2 = Topic.objects.create(
            id=2,
            topic_name='About Us!'
        )

        url = reverse('topics-list')

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_topic_detail_GET(self):
        """To test the GET API where we check the details of single Topic"""

        self.topic1 = Topic.objects.create(
            id=1,
            topic_name='Products'
        )

        self.topic2 = Topic.objects.create(
            id=2,
            topic_name='Careers'
        )

        url_1 = "/topics/1/"
        url_2 = "/topics/2/"

        res_1 = self.client.get(url_1)
        res_2 = self.client.get(url_2)

        self.assertEqual(res_1.status_code, status.HTTP_200_OK)
        self.assertEqual(res_2.status_code, status.HTTP_200_OK)
        self.assertEqual(res_1.data, {'id': 1, 'topic_name': 'Products'})
        self.assertEqual(res_2.data, {'id': 2, 'topic_name': 'Careers'})

    def test_document_API_CRUD(self):
        """
        To test the CRUD operations by using GET, POST, PUT & DELETE APIs of document URL
        """

        self.topic1 = Topic.objects.create(
            id=1,
            topic_name='SpekiLove!'
        )
        self.folder1 = Folder.objects.create(
            id=1,
            folder_name='Customer Feedback',
            topic_id=1
        )

        url = reverse('documents-list')

        data = {"id": 1, 
                "document_name": "positive_feedbacks", 
                "folder": 1, 
                "topic": 1
        }

        response = self.client.post(url, data, format='json')

        # Checking POST API
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Document.objects.count(), 1)
        self.assertEqual(Document.objects.get().document_name, 'positive_feedbacks')

        # Checking GET-LIST API
        url = reverse('documents-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Checking GET-Detail API
        self.document1 = Document.objects.create(
            id=2,
            document_name='negative_feedbacks',
            folder_id=1,
            topic_id=1
        )
        
        url = "/documents/2/"
        res = self.client.get(url)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, {'id': 2, 'document_name': 'negative_feedbacks', 'folder': 1, 'topic': 1})
    
        # Checking PUT API
        data = {'id': 2, 'document_name': 'remarks', 'folder': 1, 'topic': 1}

        response = self.client.put(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['document_name'], 'remarks')

        # Checking DELETE API
        data = {'id': 2}

        response = self.client.delete(url, data, format='json')

        doc = Document.objects.filter(id=2).first()

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(doc, None)

    def test_get_queryset_method(self):
        self.topic1 = Topic.objects.create(
            id=1,
            topic_name='SpekiLove!'
        )
        self.topic2 = Topic.objects.create(
            id=2,
            topic_name='Marketing'
        )

        self.folder1 = Folder.objects.create(
            id=1,
            folder_name='Customer Feedback',
            topic_id=1
        )
        self.folder2 = Folder.objects.create(
            id=2,
            folder_name='Campaigns',
            topic_id=2
        )

        self.document1 = Document.objects.create(
            id=1,
            document_name='positive_feedbacks',
            folder_id=1,
            topic_id=1
        )
        self.document2 = Document.objects.create(
            id=2,
            document_name='negative_feedbacks',
            folder_id=1,
            topic_id=1
        )
        self.document3 = Document.objects.create(
            id=3,
            document_name='online campaigns',
            folder_id=2,
            topic_id=1
        )
        self.document4 = Document.objects.create(
            id=4,
            document_name='Seminars',
            folder_id=2,
            topic_id=2
        )

        # Fetching All Documents when no query_param is provide
        url_1 = reverse('documents-list')
        res_1 = self.client.get(url_1)
        
        self.assertEqual(res_1.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res_1.data), 4)

        # Fetching Documents when only 'topic' is provided
        url_2 = "/documents/?topic=Marketing"
        res_2 = self.client.get(url_2)

        self.assertEqual(res_2.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res_2.data), 1)
        
        for doc in res_2.data:
            doc_name = dict(doc)['document_name']
            self.assertIn(doc_name, ['Seminars'])

        # Fetching Documents when only 'folder' is provided
        url_3 = "/documents/?folder=Campaigns"
        res_3 = self.client.get(url_3)

        self.assertEqual(res_3.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res_3.data), 2)

        for doc in res_3.data:
            doc_name = dict(doc)['document_name']
            self.assertIn(doc_name, ['online campaigns', 'Seminars'])


        # Fetching Documents when both 'folder' & 'topic' is provided

        url_4 = "/documents/?folder=Customer%20Feedback&topic==SpekiLove!"
        res_4 = self.client.get(url_4)

        self.assertEqual(res_4.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res_4.data), 2)

        for doc in res_4.data:
            doc_name = dict(doc)['document_name']
            self.assertIn(doc_name, ['positive_feedbacks', 'negative_feedbacks'])
