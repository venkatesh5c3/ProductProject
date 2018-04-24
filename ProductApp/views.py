from django.shortcuts import render
from django.http import HttpResponse
from .models import Product,Menu,Item;
# Create your views here.

def index(request):
    return render(request,'index.html')

def addProduct(request):
    return render(request,'addProduct.html')

def saveProduct(request):
    pid=request.POST['pid']
    pname=request.POST['pname']
    pdate=request.POST['pdate']
    p=Product(pid,pname,pdate)
    p.save()
    return render(request,'index.html')

def displayProducts(request):
    records=Product.objects.all()
    return render(request,'display.html',{'recs':records})


def menuCreate(request):
    breafast=Menu(101,'Breakfast')
    item1=Item(901,'idli',20,menu=breafast)
    item2=Item(902,'soup',30,menu=breafast)
    cooldrinks=Menu(201,'cool drinks')
    item3=Item(801,'pepsy',menu=cooldrinks)
    item4=Item(802,'mazza',menu=cooldrinks)
    item5=Item(803,'sprite',menu=cooldrinks)
    icecreams=Menu(301,'Ice Creams')
    item6=Item(401,'venalaa',menu=icecreams)
    item7=Item(402,'choocklet',menu= icecreams)

    breafast.save();
    item1.save()
    item2.save()
    cooldrinks.save()
    item3.save()
    item4.save()
    item5.save()
    icecreams.save()
    item6.save()
    item7.save()

    return render(request,'display.html')


def menuDelete(request):
    return render(request,'display.html')