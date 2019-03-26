from django.shortcuts import render, get_object_or_404, HttpResponse
from django.template.defaulttags import register
from django.contrib.auth.decorators import login_required
from .models import Product, BatchNumber, Login


# Create your views here.
def index(request):
    return render(request, 'lifecare/index.html')


def results(request):
    return render(request, 'lifecare/result.html')


@login_required()
def upload_form(request):
    if request.method == 'POST':
        product_name = request.POST['product_name']
        mrp = request.POST['mrp']
        packing = request.POST['packing']
        expiry = request.POST['expiry']
        batch_numbers = request.POST.getlist('batch_number[]')
        print(batch_numbers)

        product = Product()

        user_query_set = Login.objects.filter(user=request.user)

        if user_query_set:
            l = list(user_query_set.values('manufacturer_name'))
            manf_name = l[0]['manufacturer_name']
            product.manufacturer = manf_name

        product.product_name = product_name
        product.price = str(mrp)
        product.packing = packing
        product.expiry = expiry
        product.save()

        for i in range(len(batch_numbers)):
            batch = BatchNumber()
            batch.product = product
            batch.batch_no = str(batch_numbers[i])
            batch.save()

    return render(request, 'lifecare/upload-form.html')


@login_required()
def upload_excel(request):
    return render(request, 'lifecare/upload-excel.html')
