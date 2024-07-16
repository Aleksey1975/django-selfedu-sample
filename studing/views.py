from django.shortcuts import render
from .models import *
from .forms import UploadFileForm

def handle_uploaded_file(f):
    with open(f"uploads/{f.name}", "wb+") as destination:
        for chunk in f.chunks():
            destination.write(chunk)
def index(request):
    if request.method == "POST":
        # handle_uploaded_file(request.FILES['file_upload'])
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            # handle_uploaded_file(form.cleaned_data["file"])
            fp = UploadFiles(file=form.cleaned_data["file"])
            fp.save()
    else:
        form = UploadFileForm()

    context = {
        "form": form,
    }

    return render(request, 'studing/index.html', context)
