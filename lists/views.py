from django.shortcuts import render
#from django.shortcuts import HttpResponse

# Create your views here.
def home_page(request):
    return render(request, 'home.html')
    #return HttpResponse('<html><title>PMPL</title><p>Hanifah Sakinah / 1206278196</p></html>')
