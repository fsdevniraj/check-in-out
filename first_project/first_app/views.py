from django.shortcuts import render
from django .http import HttpResponse
from first_app.models import Items
# Create your views here.

def index(request):
    item_list = Items.objects.all()
    my_dict = {'Itemss': item_list}
    return render(request,'first_app/index.html',context=my_dict)
