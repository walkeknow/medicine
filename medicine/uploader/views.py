from django.shortcuts import render
from .models import UploadForm, Upload
from django.http import HttpResponseRedirect
from django.urls import reverse
import xlrd
import os
from datetime import datetime
from django.contrib.auth.decorators import login_required
from authenticator.models import Product, BatchNumber, Login


def floatHourToTime(fh):
    h, r = divmod(fh, 1)
    m, r = divmod(r * 60, 1)
    return (
        int(h),
        int(m),
        int(r * 60),
    )


# # Create your views here.
# def home(request):
#     if request.method == "POST":
#         file = UploadForm(request.POST, request.FILES)
#         if file.is_valid():
#             file.save()
#             return HttpResponseRedirect(reverse('imageupload'))
#     else:
#         img = UploadForm()
#     images = Upload.objects.all().order_by('-upload_date')
#     return render(request, 'home.html', {'form': img, 'images': images})
#

@login_required()
def upload_excel(request):
    if request.method == "POST":
        input_excel = request.POST.get('file0')
        
        #input_excel = request.FILES['file']
        print(input_excel)
        # file.save()
        # saved_file_query = Upload.objects.all().order_by('-id')[0]
        # print(saved_file_query.file)
        # saved_file = saved_file_query.file
        # module_dir = os.path.dirname(__file__)
        # file_path = os.path.join(module_dir, input_excel)
        # loc = file_path
        wb = xlrd.open_workbook(file_contents=input_excel.read())
        sheet = wb.sheet_by_index(0)
        sheet.cell_value(0, 0)

        for i in range(1, sheet.nrows):
            row = [str(x).strip() for x in sheet.row_values(i)]
            product_name = row[0]
            packing = row[1]
            batch_number = row[2]
            mrp = row[3]
            expiry = row[4]
            excel_date = float(expiry)
            dt = datetime.fromordinal(datetime(1900, 1, 1).toordinal() + int(excel_date) - 2)
            hour, minute, second = floatHourToTime(excel_date % 1)
            expiry_with_time = dt.replace(hour=hour, minute=minute, second=second)
            expiry = expiry_with_time.date()

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

            batch = BatchNumber()
            batch.product = product
            batch.batch_no = batch_number
            batch.save()
        return HttpResponseRedirect(reverse('upload-excel'))
    else:
        print("not enter")
        file = UploadForm()
        files = Upload.objects.all().order_by('-upload_date')
        return render(request, 'lifecare/upload-excel.html', {'form': file, 'images': files})
