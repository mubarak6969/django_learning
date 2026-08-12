from django.http import HttpResponse

def home(request):
    return HttpResponse("Assalamu Alaikum! My first Django view is working! 🎉")

def about(request):
    return HttpResponse("This is the About page! I am Mubarak, a Django developer!")