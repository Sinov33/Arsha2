from django.contrib import admin
from myfiles.models import *
# Register your models here.

class AdminType(admin.ModelAdmin):
    list_display = ['id','nomi']

admin.site.register(Type,AdminType)



class AdminPort(admin.ModelAdmin):
    list_display = ['id','nomi','tur','company_name','rasm1','vaqt']

admin.site.register(Poryfolio,AdminPort)

class Adminmalumot(admin.ModelAdmin):
    list_display = ['id','matn']

admin.site.register(Malumot,Adminmalumot)

class AdminSer(admin.ModelAdmin):
    list_display = ['id','nomi','tur','rasm1','malumot']

admin.site.register(Service,AdminSer)

class AdminLavozm(admin.ModelAdmin):
    list_display = ['id','nomi']

admin.site.register(Lavozm,AdminLavozm)

class AdminTeam(admin.ModelAdmin):
    list_display = ['id','ism','familiya','rasm1','yosh','malumot','lavozm']


admin.site.register(Team,AdminTeam)



class AdminMurojaat(admin.ModelAdmin):
    list_display = ['id','ism','gmail','title','text','vaqt']


admin.site.register(Murojaj,AdminMurojaat)