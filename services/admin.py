from django.contrib import admin
from .models import CoWorkingSpace, Conference, Membership, Customer

# Register your models here.
admin.site.register(CoWorkingSpace)
admin.site.register(Conference)
admin.site.register(Membership)
admin.site.register(Customer)