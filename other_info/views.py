from django.shortcuts import render,get_object_or_404
from other_info import models
# Create your views here.
def infos(request):
    info=models.Info.objects.order_by('-date')
    return render(request,'info.html',{'info':info})

def each_info(request,info_id):
    info=get_object_or_404(models.Info,pk=info_id)
    return render(request,'each_info.html',{'info':info})
