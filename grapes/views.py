from django.shortcuts import render

# Create your views here.
def pandu(request):
    fruits='fruits are good for Health'
    d={'data':fruits}
    return render(request,'pandu.html',context=d)
