from django.http import HttpResponse
from common.Chack import chack_requset_type
from common.sendjson import Sendjson
from ..models import *


#fen ye zhanshidingdan
def getorder(request):
    sendjson = Sendjson()
    if(chack_requset_type(request)):
         page = int(request.POST['page'])
         count = int(request.POST['count'])
         try:
            list =   market_user_pub.objects.exclude(is_valid=1)[(page-1)*count:page*count-1]
            return_param = {
                "param": sendjson.list_json(list)
            }
            sendjson.set_resNode("success")
            sendjson.set_resParam(return_param)
         except Exception as e:
             sendjson.set_resNode(e)
    else:
        sendjson.set_resNode("wrong request type")
    return HttpResponse(sendjson.get_json())

#jie dan
def inputorder(request):
    sendjson = Sendjson()
    if(chack_requset_type(request)):
        order_id = request.POST["order_id"]
        user_id = request.POST["user_id"]
        try:
            market_user_get.objects.create(order_id=order_id,user_id=user_id,company="person")
            sendjson.set_resNode("success")
        except:
            sendjson.set_resNode("failde")
    else:
        sendjson.set_resNode("wrong request type")
    return HttpResponse(sendjson.get_json())
