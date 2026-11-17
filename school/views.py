from django.shortcuts import render

# Create your views here.
def index(request): 
    return render(request, "baringo/index.html")

def terms(request): 
    return render(request, "baringo/terms.html")

def about(request): 
    return render(request, "baringo/about.html")

def services(request):
    return render(request, "baringo/services.html")

def admissions(request):
    return render(request, "baringo/admissions.html")

def academics(request):
    return render(request, "baringo/academics.html")

def facilities(request):
    return render(request, "baringo/facilities.html")

def gallery(request):
    return render(request, "baringo/gallery.html")

def blog(request):
    return render(request, "baringo/blog.html")

def contact(request):
    return render(request, "baringo/contact.html")

def principal(request):
    return render(request, "baringo/principal.html")

def student_life(request):
    return render(request, "baringo/student_life.html")

def cbe(request):
    return render(request, "baringo/cbe.html")

def departments(request):
    return render(request, "baringo/departments.html")