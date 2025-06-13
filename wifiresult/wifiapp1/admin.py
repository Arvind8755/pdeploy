from django.contrib import admin
from wifiapp1.models import Result, Admitcard, Answerkey, Job, Syllabus,Contact
from .forms import ResultAdminForm
# Register your models here.

admin.site.register(Admitcard)  
admin.site.register(Answerkey)
admin.site.register(Syllabus)
admin.site.register(Contact)


class ResultAdmin(admin.ModelAdmin):
  prepopulated_fields = {"slug": ("title",)}
  form = ResultAdminForm
admin.site.register(Result, ResultAdmin)

class JobAdmin(admin.ModelAdmin):
  prepopulated_fields = {"slug": ("title",)}
admin.site.register(Job, JobAdmin)
