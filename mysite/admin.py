from django.contrib import admin
from .models import Company, Advertisement, CompanyImages


class PhotosCompanyInline(admin.TabularInline):
    model = CompanyImages
    fields = ('image', 'description')
    max_num = 5

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    inlines = [PhotosCompanyInline,]


admin.site.register(Advertisement)
