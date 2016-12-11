from django.test import TestCase
from dashboard.models import Word

# Create your tests here.
class NewListTest(TestCase):
    def test_saving_a_POST_request(self):
        Word.objects.create(english="en", polish="pl")

        self.client.post(
            '/dashboard/add_word/',
            data={'en_word': 'english', 'pl_word': 'polish'}
        )

        self.assertEqual(Word.objects.count(), 4)
        new_item = Word.objects.filter(english='english')
        self.assertEqual(new_item.english, 'english')

    # def test_redirects_after_POST(self):
    #     response = self.client.post(
    #         '/lists/new',
    #         data={'item_text': 'Nowy element listy'}
    #     )
    #
    #     new_list = List.objects.first()
    #     self.assertRedirects(response, '/lists/%d/' % (new_list.id,))