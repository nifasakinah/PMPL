from django.shortcuts import redirect, render
#from django.http import HttpResponse
from lists.models import Item, List
from django.core.exceptions import ValidationError

# Create your views here.
def home_page(request):
    #if request.method == 'POST':
    #    Item.objects.create(text=request.POST['item_text'])
    #    return redirect('/lists/the-only-list-in-the-world/')

    #items = Item.objects.all()
    #countsItem = Item.objects.count()
    #comment = 'yey, waktunya berlibur'

    return render(request, 'home.html')
    #return render(request, 'home.html', {'comment': comment})

def list_page(request):
    countsItem = Item.objects.count()
    comment = 'yey, waktunya berlibur'

    return render(request, 'base.html', {'comment': comment})
def view_list(request, list_id):
    list_ = List.objects.get(id=list_id)
    error = None
    if request.method == 'POST':
        try:
            item = Item(text=request.POST['item_text'], list=list_)
            item.full_clean()
            item.save()
            return redirect(list_)
        except ValidationError:
            error = "You can't have an empty list item"
    comment = ''
    if Item.objects.filter(list_id=list_.id).count() == 0 :
        comment = 'yey, waktunya berlibur'
    elif (Item.objects.filter(list_id=list_.id).count() > 0) and (Item.objects.filter(list_id=list_.id).count() < 5) :
        comment = 'sibuk tapi santai'
    else :
        comment = 'oh tidak'
        
    return render(request, 'list.html', {'list': list_, 'error': error, 'comment':comment})
    #items = Item.objects.filter(list=list_)
    #items = Item.objects.all()
    #return render(request, 'list.html', {'items': items})

def new_list(request):
    list_ = List.objects.create()
    item = Item(text=request.POST['item_text'], list=list_)
    try:
        item.full_clean()
        item.save()
    except ValidationError:
        list_.delete()
        error = "You can't have an empty list item"
        return render(request, 'home.html', {"error": error})
    return redirect(list_)

def add_item(request, list_id):
    #pass
    list_ = List.objects.get(id=list_id)
    Item.objects.create(text=request.POST['item_text'], list=list_)
    return redirect('/lists/%d/' % (list_.id,))


