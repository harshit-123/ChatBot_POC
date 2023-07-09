from django.shortcuts import render
from core.models import UploadPDF
from django.contrib import messages
from django.http import HttpResponse

# Create your views here.
def index(request):
    css = 'css/style.css'
    success_res = False
    reload = False
    if request.method == "POST":
        user_pdfs = request.FILES.getlist('pdf')
        try:
            for f in user_pdfs:
                pdf_uplaod = UploadPDF(pdf = f)
                pdf_uplaod.save()
            success_res = True
            reload = True
            return render(request, "index.html", {"css": css, "success_res": success_res, "reload": reload})
        except Exception as e:
            pass
    return render(request, "index.html", {"css": css, "success_res": success_res})


