from django.shortcuts import redirect, render
#from django.http import HttpResponse
from lists.models import Item, List

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

    #if request.method == 'POST':

     #   Item.objects.create(text=request.POST['item_text'])
      #  return redirect('/lists/the-only-list-in-the-world/')

    items = Item.objects.all()
    #countsItem = Item.objects.count()
    comment = 'yey, waktunya berlibur'

    #if countsItem > 0:
     #   comment = 'sibuk tapi santai'
    #if countsItem >= 5:
     #   comment = 'oh tidak'
    return render(request, 'home.html', {'comment': comment})
    #return render(request, 'home.html')
        #new_item_text = request.POST['item_text']  #1
     
   #Item.objects.create(text=new_item_text)  #2
    #else:
     #   new_item_text = ''  #3

    #return render(request, 'home.html', {
    #    'new_item_text': new_item_text,
    #})
def view_list(request, list_id):
    list_ = List.objects.get(id=list_id)
    #return render(request, 'list.html', {'list': list_})
    comment = ''
    if Item.objects.filter(list_id=list_.id).count() == 0 :
        comment = 'yey, waktunya berlibur'
    elif (Item.objects.filter(list_id=list_.id).count() > 0) and (Item.objects.filter(list_id=list_.id).count() < 5) :
        comment = 'sibuk tapi santai'
    else :
        comment = 'oh tidak'

    return render(request, 'list.html', {'list': list_, 'comment':comment})
    #items = Item.objects.filter(list=list_)
    #items = Item.objects.all()
    #return render(request, 'list.html', {'items': items})

def new_list(request):
#    pass
    list_ = List.objects.create()
    Item.objects.create(text=request.POST['item_text'], list=list_)
    return redirect('/lists/%d/' % (list_.id,))
#    return redirect('/lists/the-only-list-in-the-world/')

def add_item(request, list_id):
    #pass
    list_ = List.objects.get(id=list_id)
    Item.objects.create(text=request.POST['item_text'], list=list_)
    return redirect('/lists/%d/' % (list_.id,))


