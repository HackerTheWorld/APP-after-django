
from common.sendjson import Sendjson
from user.models import *
from django.forms.models import model_to_dict


def getuserinfor(request):
    sendjson = Sendjson()
    user_id = request.POST["user_id"]
    try:
        userinfor = user_info.objects.get(user_id=user_id)
        user_dic = model_to_dict(userinfor)
        return_param ={
                "user_info":user_dic
        }
        sendjson.set_resNode("success")
        sendjson.set_resParam(return_param)
    except Exception as e:
            sendjson.set_resNode(e)
    return sendjson.get_json()

def insertuserinfor(request):
    sendjson = Sendjson()
    loginid = request.POST["loginid"]
    truename = request.POST["truename"]
    carnumber = request.POST["carnumber"]
    phone = request.POST["phone"]
    name = request.POST["name"]
    address = request.POST["address"]
    try:
        obj = user_info(truename=truename,carnumber=carnumber,phone=phone,address=address,name=name)
        obj.save()
        login.objects.filter(login_ID=loginid).update(user_id=obj.user_id)
        sendjson.set_resNode("success")
    except:
        sendjson.set_resNode("wrong")
    return sendjson.get_json()