from django.http import HttpResponse

def HelloView(request):
	return HttpResponse("Holu")