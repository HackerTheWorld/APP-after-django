from django.http import HttpResponse
from ..common.Chack import chack_method

def failter(request):

    if(request.method =="POST"):
        meth = request.POST["meth"]
        switcher = chack_method(meth)
        if (switcher != ""):
           switcher.set_request(switcher,request)
           return HttpResponse(switcher.dopost(switcher))
        else:
           return HttpResponse("don't have method")
    else:
        return HttpResponse("wrong requset type")


