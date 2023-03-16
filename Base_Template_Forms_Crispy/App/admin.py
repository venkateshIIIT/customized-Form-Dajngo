from django.contrib import admin
from .models import Candidate
from django.utils.html import format_html
# Register your models here.

class CandidateAdmin(admin.ModelAdmin):
    list_filter = ['Situation']
    list_display=['firstname','lastname','email','Age','job','created_at','status']
    search_fields=['firstname','lastname','email','Situation']
    list_per_page =10

    #Function to change the icons

    #Function to color the text
    def status(self,obj):
        if(obj.Situation == "Approved"):
            color ="#28a745"
        elif(obj.Situation == "Pending"):
            color="#fea95e"
        else:
            color='red'
        return format_html('<strong><p style="color : {}">{}</p></strong>'.format(color,obj.Situation))
    status.allow_tags = True

admin.site.register(Candidate,CandidateAdmin)
