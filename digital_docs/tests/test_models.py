from django.test import TestCase
from digital_docs.models import Topic, Folder, Document


class TestModels(TestCase):

    def setUp(self):
        self.topic1 = Topic.objects.create(
            id=1,
            topic_name='SpekiLove!'
        )

        self.folder1 = Folder.objects.create(
            id=1,
            folder_name='Customer Feedback',
            topic_id=1
        )

        self.document1 = Document.objects.create(
            document_name='positive_feedbacks',
            folder_id=1,
            topic_id=1
        )
           
    def test_models_fields(self):
        """To test if models have information fields"""

        self.assertIsInstance(self.topic1.topic_name, str)
        self.assertIsInstance(self.folder1.folder_name, str)
        self.assertIsInstance(self.document1.document_name, str)

    def test_exceeding_max_length_of_fields(self):
        """To check DB error if name field exceeded 'max_length' of character field"""

        db_error = "value too long for type character varying(50)\n"

        try:
            self.document2 = Document.objects.create(
                document_name='A very long name that should have more than fifty characters to generate DB error',
                folder_id=1,
                topic_id=1
            )
        except Exception as e:
            self.assertEqual(e.args[0], db_error)

    def test_model_one_to_many_realtionship(self):
        """To test the relationships among models"""

        self.assertEqual(self.document1.folder_id, 1)
        self.assertNotEqual(self.document1.folder_id, 112)
        self.assertEqual(self.document1.topic_id, 1)

        self.assertEqual(self.folder1.topic_id, 1)
        self.assertNotEqual(self.folder1.topic_id, 101)
        