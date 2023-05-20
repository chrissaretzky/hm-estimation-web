from django.db import models
from azureproject.custom_azure import AzureMediaStorage

class CommunicationRequest(models.Model):
    
    datetime = models.DateTimeField()
    email = models.EmailField()
    body = models.TextField()

class Estimations(models.Model):

    estimator_id = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    claim_num = models.CharField(max_length=50)
    year = models.CharField(max_length=4)
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    notes = models.TextField()

    def images(self):
        return Images.objects.get(estimate=self.pk)


class Images(models.Model):

    estimate = models.ForeignKey(Estimations, on_delete=models.CASCADE)
    notes = models.TextField()
    imagefile = models.ImageField(upload_to='images')