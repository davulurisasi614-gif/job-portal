from django.contrib import admin
from .models import Job, Application

# 👇 ADD THESE LINES
admin.site.site_header = "Sasi's Job Portal Administration"
admin.site.site_title = "Job Portal Admin"
admin.site.index_title = "Welcome to Job Portal Admin"

admin.site.register(Job)
admin.site.register(Application)
