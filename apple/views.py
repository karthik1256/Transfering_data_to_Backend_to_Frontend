from django.shortcuts import render

# Create your views here.
def karthik(request):
    fruits='fruits are good for Health'
    d={'data':fruits}
    return render(request,'karthik.html',context=d)
