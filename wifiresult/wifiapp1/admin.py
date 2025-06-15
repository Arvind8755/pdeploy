from django.contrib import admin
from wifiapp1.models import Result, Admitcard, Answerkey,Syllabus,Job,Admission,Contact
from .forms import ResultAdminForm
# Register your models here.


admin.site.register(Contact)


class ResultAdmin(admin.ModelAdmin):
  prepopulated_fields = {"slug": ("title",)}
  form = ResultAdminForm
  list_display = ('title', 'status', 'updated_at')
  list_filter = ('status',)
admin.site.register(Result, ResultAdmin)

class AdmitcardAdmin(admin.ModelAdmin):
  prepopulated_fields = {"slug": ("title",)}
  list_display = ('title', 'status', 'updated_at')
  list_filter = ('status',)
admin.site.register(Admitcard, AdmitcardAdmin)

class SyllabusAdmin(admin.ModelAdmin):
  prepopulated_fields = {"slug": ("title",)}
  list_display = ('title', 'status', 'updated_at')
  list_filter = ('status',)
admin.site.register(Syllabus, SyllabusAdmin)

class AnswerkeyAdmin(admin.ModelAdmin):
  prepopulated_fields = {"slug": ("title",)}
  list_display = ('title', 'status', 'updated_at')
  list_filter = ('status',)
admin.site.register(Answerkey, AnswerkeyAdmin)

class JobAdmin(admin.ModelAdmin):
  prepopulated_fields = {"slug": ("title",)}
  list_display = ('title', 'status', 'updated_at')
  list_filter = ('status',)
admin.site.register(Job, JobAdmin)

class AdmissionAdmin(admin.ModelAdmin):
  prepopulated_fields = {"slug": ("title",)}
  list_display = ('title', 'status', 'updated_at')
  list_filter = ('status',)
admin.site.register(Admission, AdmissionAdmin)
