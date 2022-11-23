from django.shortcuts import render


# Create your views here.
def upload(request):
    if request.method == "POST":
        uploaded_file = request.FILES['document']
    return render(request, 'upload.html')
        
        
        