# import Http Response from django
import datetime
import uuid

from django.shortcuts import render
from .forms import CommunicationRequestForm, EstimateForm
from .models import CommunicationRequest, Estimations, Images
from django.core.files.storage import FileSystemStorage
  
def home_view(request):
    return render(request, "home.html")

def estimate_view(request):
    context = {}
    if request.method == 'POST' and request.FILES['images']:
        estimate = Estimations(
                estimator_id = request.POST['estimator_id'],
                first_name = request.POST['first_name'],
                last_name = request.POST['last_name'],
                email = request.POST['email'],
                claim_num = request.POST['claim_num'],
                year = request.POST['year'],
                make = request.POST['make'],
                model = request.POST['model'],
                notes = request.POST['notes'],
            )
        estimate.save()

        for img in request.FILES.getlist('images'):
            image = Images(
                estimate = estimate,
                notes = 'blank',
                imagefile = img,
            )
            print(image.imagefile)
            image.save()
        context['message'] = "Information Sent, We will follow up by email"
    context['form'] = EstimateForm()
    return render(request, "estimate.html", context)

def about_view(request):
    return render(request, "about.html")

def contact_view(request):
    context = {}

    if request.method == 'POST':
        form = CommunicationRequestForm(request.POST)
        if form.is_valid():
            context['message'] = "Message Sent!"
            CommunicationRequest(
                datetime = datetime.datetime.now(),
                email = request.POST['email'],
                body = request.POST['body']
            ).save()

    context['form'] = CommunicationRequestForm()
    return render(request, "contact.html", context)