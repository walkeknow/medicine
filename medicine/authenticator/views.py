from django.shortcuts import render, get_object_or_404, HttpResponse, Http404
from django.template.defaulttags import register
from django.contrib.auth.decorators import login_required
from .models import Product, BatchNumber, Login
import xlrd
import os
from datetime import datetime


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

# def floatHourToTime(fh):
#     h, r = divmod(fh, 1)
#     m, r = divmod(r*60, 1)
#     return (
#         int(h),
#         int(m),
#         int(r*60),
#     )
#
# @login_required()
# def upload_excel(request):
#     module_dir = os.path.dirname(__file__)
#     file_path = os.path.join(module_dir, 'data.xlsx')
#     loc = file_path
#     wb = xlrd.open_workbook(loc)
#     sheet = wb.sheet_by_index(0)
#     sheet.cell_value(0,0)
#
#     for i in range(1, sheet.nrows):
#         row = [str(x).strip() for x in sheet.row_values(i)]
#         product_name = row[0]
#         packing = row[1]
#         batch_numbers = row[2]
#         mrp = row[3]
#         expiry = row[4]
#         excel_date = float(expiry)
#         dt = datetime.fromordinal(datetime(1900, 1, 1).toordinal() + int(excel_date) - 2)
#         hour, minute, second = floatHourToTime(excel_date % 1)
#         expiry_with_time = dt.replace(hour=hour, minute=minute, second=second)
#         expiry = expiry_with_time.date()
#
#         product = Product()
#
#         user_query_set = Login.objects.filter(user=request.user)
#
#         if user_query_set:
#             l = list(user_query_set.values('manufacturer_name'))
#             manf_name = l[0]['manufacturer_name']
#             product.manufacturer = manf_name
#
#         # if product_query_set:
#
#         product.product_name = product_name
#         product.price = str(mrp)
#         product.packing = packing
#         product.expiry = expiry
#         product.save()
#
#         for i in range(len(batch_numbers)):
#             batch = BatchNumber()
#             batch.product = product
#             batch.batch_no = str(batch_numbers[i])
#             batch.save()
#
#     return render(request, 'lifecare/upload-excel.html')
