from django.http import HttpResponse


def index(request):
    return HttpResponse("this is the music app hompage")
	
def detail(request, album_id):
    return HttpResponse("<h2>Details for ALbum id: " + str(album_id) + "</h2>")
	
	
	
