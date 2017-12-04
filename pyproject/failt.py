from user.interface.Order import *
from user.interface.User import *
from user.interface.Userinfor import *
from common.Chack import chack_requset_type
from user.interface.uploadfile import upload


def fail(req):
    method = req.POST["method"]
    res = ""
    if(method =="log"):
        res = log(req)
        return HttpResponse(res)
    elif(method == "register"):
        res = register(req)
        return HttpResponse(res)
    elif (method == "insertuserinfor"):
        res = insertuserinfor(req)
        return HttpResponse(res)
    elif(chack_requset_type(req)!=False):
        if(method == "aslog"):
            res = aslog(chack_requset_type(req))
            return HttpResponse(res)
        elif(method == "checkpassword"):
            res = checkpassword(req)
            return HttpResponse(res)
        elif(method == "changepassword"):
            res = changpassword(req)
            return HttpResponse(res)
        elif(method == "listview"):
            res = listview(req)
            return HttpResponse(res)
        elif(method == "insertuserinfor"):
            res = insertuserinfor(req)
            return HttpResponse(res)
        elif(method == "uploadhead"):
            res = upload(req)
            return HttpResponse(res)
        elif(method == "getorder"):
            res = getorder(req)
            return HttpResponse(res)
        elif(method == "getvoyage"):
            res = getvoyage(req)
            return HttpResponse(res)
        elif(method == "getvoyagelist"):
            res = getvoyagelist(req)
            return HttpResponse(res)
        elif(method == "getpicurl"):
            res = getpicurl(req)
            return HttpResponse(res)

    else:
        return HttpResponse("faile")