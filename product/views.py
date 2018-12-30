from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import product
from django.utils import timezone

def home(request):
    prod = product.objects
    return render(request, 'products/home.html', {'Product': prod})


@login_required(login_url='/account/signup')
def create(request):
    if request.method == 'POST':
        if request.POST['title'] and request.POST['body'] and request.POST['url'] and request.FILES['icon'] and request.FILES['image']:
            prod = product()
            prod.title = request.POST['title']
            prod.body = request.POST['body']
            if request.POST['url'].startswith('http://') or request.POST['url'].startswith('https://'):
                prod.url = request.POST['url']
            else:
                prod.url = "https://" + request.POST['url']
            prod.icom = request.FILES['icon']
            prod.image = request.FILES['image']
            prod.pub_date = timezone.datetime.now()
            prod.user = request.user
            prod.save()
            return redirect('/product/' + str(prod.id))
        else:
            return render(request, 'products/create.html', {'error':'all field are required'})

    else:
        return render(request, 'products/create.html')



def detail(request, product_id):
    prod = get_object_or_404(product, pk=product_id)
    return render(request, 'products/detail.html', {'product':prod})


@login_required(login_url='/account/signup')
def upvote(request, product_id):
    if request.method == 'POST':
        prod = get_object_or_404(product, pk=product_id)
        prod.votes_total += 1
        prod.save()
        return redirect('/product/' + str(prod.id))
