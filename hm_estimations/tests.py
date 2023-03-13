import datetime

from django.test import TestCase, Client
from django.conf import settings
from django.core.mail import send_mail

from .models import CommunicationRequest, Estimations, Images

class CommunicationRequestModelTests(TestCase):

    def test_model_creation_proper_values(self):
        communication_request = CommunicationRequest(
            datetime = datetime.datetime.now(),
            email = 'test@test.com',
            body = 'Here is a string of test'
        )

        self.assertIsInstance(communication_request, CommunicationRequest)
    
    def test_model_creation_proper_valuess(self):
        communication_request = CommunicationRequest(
            datetime = datetime.datetime.now(),
            email = 'test@test.com',
            body = 'Here is a string of test'
        )

        communication_request.save()
        pk = communication_request.pk
        communication_request = CommunicationRequest.objects.get(pk = pk)
        self.assertEquals(communication_request.pk, pk)

class EstimationModelTests(TestCase):
    def setUp(self):
        self.estimate = Estimations(
            estimator_id = 1111,
            first_name = 'Testie',
            last_name = 'McTesterson',
            email = 'test@test.com',
            claim_num = 4300,
            year = 2007,
            make = 'Mazda',
            model = 3,
            notes = 'This car broke, need to be fixed',
        )
    
    def test_adding_image_to_estimate(self):
        image = Images(
            estimate = self.estimate,
            notes = 'picture of broke',
            imagefile = '/test/test1.png',
        )

        self.estimate.save()
        image.save()
        pk = self.estimate.pk
        estimate = Estimations.objects.get(pk = pk)
        images = estimate.images_set.all()
        self.assertEquals(images[0].imagefile, '/test/test1.png')
    
    def test_get_child_image_function(self):
        image = Images(
            estimate = self.estimate,
            notes = 'picture of broke',
            imagefile = '/test/test1.png',
        )

        self.estimate.save()
        image.save()
        print(self.estimate.images())
        # self.assertEquals(images[0].imagefile, '/test/test1.png')
        
    

class ContactPageViewTests(TestCase):
    
    def setUp(self):
        self.client = Client()
    
    def test_contact_form_submission(self):
        self.client.post('/contact/', {'email': 'test_contact_form_submission@test.com', 'body': 'this is a test'})
        c = CommunicationRequest.objects.get(email='test_contact_form_submission@test.com')
        self.assertIsInstance(c, CommunicationRequest)

# class EmailTests(TestCase):
#         subject = 'welcome to GFG world'
#         message = f'Hi thank you for registering in geeksforgeeks.'
#         email_from = settings.EMAIL_HOST_USER
#         recipient_list = ['chris.saretzky@gmail.com', ]
#         v = send_mail( subject, message, email_from, recipient_list, fail_silently=False)
#         print(v)