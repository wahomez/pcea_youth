from django.contrib import admin
from .models import *

# Register your models here.
class SermonAdmin(admin.ModelAdmin):
    list_display = ("Service","Preacher","Date")
    search_fields = ("Service", "Preacher","Date")

admin.site.register(Sermon, SermonAdmin)
admin.site.register(Activity)
admin.site.register(Family)
admin.site.register(Team)
admin.site.register(Week_Message)
admin.site.register(Payment)
admin.site.register(Schedule)
admin.site.register(Membership)
admin.site.register(Booking)
admin.site.register(Join_Team)
admin.site.register(Join_Family)
admin.site.register(Announcement)