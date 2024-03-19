from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin

@admin.register(Author)
class AuthorAdmin(ImportExportModelAdmin):
	pass 


@admin.register(Book)
class BookAdmin(ImportExportModelAdmin):
	pass 


@admin.register(Category)
class CategoryAdmin(ImportExportModelAdmin):
	pass 
