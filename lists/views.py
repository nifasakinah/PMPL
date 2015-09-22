from django.shortcuts import redirect, render
#from django.http import HttpResponse
from lists.models import Item

# Create your views here.
def home_page(request):
    #return render(request, 'home.html')
    #return HttpResponse('<html><title>PMPL</title><p>Hanifah Sakinah / 1206278196</p></html>')
    #if request.method == 'POST':
    #    return HttpResponse(request.POST['item_text'])
    #return render(request, 'home.html')
    #item = Item()
    #item.text = request.POST.get('item_text', '')
    #item.save()

    if request.method == 'POST':

        Item.objects.create(text=request.POST['item_text'])
        return redirect('/lists/the-only-list-in-the-world/')

    items = Item.objects.all()
    countsItem = Item.objects.count()
    comment = 'yey, waktunya berlibur'

    if countsItem > 0:
        comment = 'sibuk tapi santai'
    if countsItem >= 5:
        comment = 'oh tidak'
    return render(request, 'home.html', {'comment': comment})
    #return render(request, 'home.html')
        #new_item_text = request.POST['item_text']  #1
     
   #Item.objects.create(text=new_item_text)  #2
    #else:
     #   new_item_text = ''  #3

    #return render(request, 'home.html', {
    #    'new_item_text': new_item_text,
    #})
def view_list(request):
    items = Item.objects.all()
    return render(request, 'list.html', {'items': items})

