from django.shortcuts import render, get_object_or_404, HttpResponse, Http404
from django.template.defaulttags import register
from django.contrib.auth.decorators import login_required
from .models import Product, BatchNumber, Login


# Create your views here.
def index(request):
    return render(request, 'lifecare/index.html')


def results(request):
    if request.method == "POST":
        batch_number = request.POST['batch_number']

        # returns list of objects
        batch_number_query = BatchNumber.objects.filter(batch_no=batch_number)

        # returns list of dicts
        print(batch_number_query.values())

        product_container_list = []
        product_map = {}
        for dict in batch_number_query.values():
            product_container = {
                "batch_number": batch_number
            }
            product_name_query = Product.objects.filter(id=dict["product_id"])
            print(product_name_query[0].price)
            product_container["product_name"] = product_name_query[0].product_name
            product_container["mrp"] = product_name_query[0].price
            product_container_list.append(product_container)

        # returns list of tuples
        company_tuple_list = Login.objects.values_list('manufacturer_name')
        company_list = []
        for i in company_tuple_list:
            company_list.append(i[0])

        print(batch_number_query)
        print(company_list)
        print(product_map)
        context = {
            "batch_number": batch_number,
            "product_list": product_container_list,
            "company_list": company_list,
        }

        return render(request, 'lifecare/result.html', context)
    else:
        return Http404


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

        # if product_query_set:

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
