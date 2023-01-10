import datetime

from django.db.models import Q
from django.shortcuts import render
from myfiles.models import Poryfolio,Service,Team,Murojaj

# Create your views here.Q(tur__startswith=text)|\loyiha = Service.objects.filter(qidirish)
def home(malumot):
    if 'Qidiruv' in malumot.POST:
        soz = malumot.POST.get('Qidiruv')
        text = str(soz).strip()
        qidirish = Q(ism__startswith=text)|Q(familiya__startswith=text)|\
                   Q(yosh__startswith=text)|Q(malumot__startswith=text)|Q(lavozm__nomi__contains=text)
        loyiha1 = Team.objects.filter(qidirish)
        loyihalar = Poryfolio.objects.all()
        loyiha = Service.objects.all()
        return render(malumot, 'index.html', {'teem': loyiha1, 'works': loyihalar, 'work': loyiha})
    if 'Qidiruv' in malumot.POST:
        soz = malumot.POST.get('Qidiruv')
        text = str(soz).strip()
        qidirish = Q(nomi__startswith=text)|Q(malumot__matn__contains=text)
        loyiha = Service.objects.filter(qidirish)
        loyihalar = Poryfolio.objects.all()
        loyiha1 = Team.objects.all()
        return render(malumot, 'index.html', {'work': loyiha,'works': loyihalar, 'teem': loyiha1})
    elif 'Qidiruv' in malumot.POST:
        soz = malumot.POST.get('Qidiruv')
        text = str(soz).strip()
        qidirish = Q(nomi__startswith=text)|Q(company_name__startswith=text)|\
                   Q(tur__nomi__contains=text)|Q(vaqt__startswith=text)|Q(link__startswith=text)
        loyihalar = Poryfolio.objects.filter(qidirish)
        loyiha = Service.objects.all()
        loyiha1 = Team.objects.all()
        return render(malumot, 'index.html', {"works": loyihalar, 'work': loyiha, 'teem': loyiha1})
    elif malumot.method=='POST':
        ism = malumot.POST.get('name')
        gmail = malumot.POST.get('email')
        mavzu = malumot.POST.get('subject')
        matn = malumot.POST.get('message')
        vaqti = datetime.datetime.now()
        Murojaj(ism=ism,gmail=gmail,title=mavzu,text=matn,vaqt=vaqti).save()


    loyihalar = Poryfolio.objects.all()
    loyiha = Service.objects.all()
    loyiha1 = Team.objects.all()
    return render(malumot,'index.html',{"works":loyihalar,'work':loyiha,'teem':loyiha1})


def portifolio(malumot,id):
    loyiha = Poryfolio.objects.get(id=id)
    return render(malumot,'portfolio-details.html',{'work':loyiha})