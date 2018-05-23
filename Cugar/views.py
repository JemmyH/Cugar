from django.shortcuts import render


def home(request):
    return render(request, "index.html")


def intro(request):
    return render(request, "introduce.html")


def static(request):
	def file_iterator(file_name, chun_size=512):
	    with open(file_name) as f:
	        while True:
	            c = f.read(chun_size)
	            if c:
	                yield c
	            else:
	                break
	file_name = "qq_android.apk"
	response = StreamingHttpResponse(file_iterator(file_name))
	response['Content-Type'] = 'application/octer-stream'
	response['Content-Disposition'] = 'attachment;file_name="{0}"'.format(file_name)
	return response