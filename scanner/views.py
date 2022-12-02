import json
from django.shortcuts import HttpResponse, HttpResponseRedirect, render
from django.urls import reverse

import qrcode
from scanner.forms import HouseForm
from scanner.models import HouseDetails

# Create your views here.
def create(request):
    """
    create
    :param request:
    :param pk:
    :return:
    """
    if request.method == 'POST':

        # if instance go to edit
        form = HouseForm(request.POST)
        
        if form.is_valid():
            data = form.save(commit=False)
            data.save()

            response_data = {
                "status": "true",
                "title": "Successfully Created",
                "message": "created successfully.",
                'redirect': 'true',
            }

        else:
            message = ""
            response_data = {
                "status": "false",
                "title": "Failed",
                "message": message,
            }

        return HttpResponse(json.dumps(response_data), content_type='application/javascript')

    else:
        form = HouseForm()

        context = {
        "form" : form,
    }
    return render(request, 'create.html',context)

