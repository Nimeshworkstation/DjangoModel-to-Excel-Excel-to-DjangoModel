from django.shortcuts import render
from app.models import *
from django.http import HttpResponse
from .resources import BookResource
from tablib import Dataset

def home(request):
	return render(request,'app/home.html')





def export(request):
    book_resource = BookResource()
    dataset = book_resource.export()
    print("***********************************")
    response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="persons.xls"'
    return response




def upload(request):
    if request.method == 'POST':
        book_resource = BookResource()
        dataset = Dataset()
        new_books = request.FILES['myfile']

        imported_data = dataset.load(new_books.read())
        result = book_resource.import_data(dataset, dry_run=True)  # Test the data import

        if not result.has_errors():
            book_resource.import_data(dataset, dry_run=False)  # Actually import now
            

    return render(request, 'app/home.html')
