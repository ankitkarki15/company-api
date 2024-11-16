from django.http import HttpResponse
# this is function based views
#to make views request is must

def home_page(request):
    print("home page requested")
    return HttpResponse("<h1>This is home page</h1>")