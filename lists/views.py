from django.shortcuts import HttpResponse

# Create your views here.
def home_page(request):
    return HttpResponse('<html><title>PMPL</title><p>Hanifah Sakinah / 1206278196</p></html>')
