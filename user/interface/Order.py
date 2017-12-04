from django.forms import model_to_dict

from common.sendjson import Sendjson
from ..models import order,voyage

def getorder(request):
    sendjson = Sendjson()
    type = request.POST["type"]
    user_id = request.POST["userid"]

    if (type != "2"):
        list = order.objects.filter(type=type, take_user_id=user_id)
    else:
        list = order.objects.filter(take_user_id=user_id)
    return_param = {
        "param": sendjson.list_json(list)
    }
    sendjson.set_resNode("success")
    sendjson.set_resParam(return_param)

    return sendjson.get_json()

def getvoyage(request):
    sendjson = Sendjson()
    voyage_id = request.POST["voyage_id"]
    user_id = request.POST["userid"]
    try:
            voyagemod = voyage.objects.get(voyage_id=voyage_id,take_user_id=user_id)
            voyagemod_dic = model_to_dict(voyagemod)
            return_param = {
                "param": voyagemod_dic
            }
            sendjson.set_resNode("success")
            sendjson.set_resParam(return_param)
    except Exception as e:
         sendjson.set_resNode(e)
    return sendjson.get_json()

def getvoyagelist(request):
    sendjson = Sendjson()
    voyage_id = request.POST["voyage_id"]
    user_id = request.POST["userid"]

    voyagelist = order.objects.filter(voyage_id=voyage_id,take_user_id=user_id)
    voyagemod = voyage.objects.values("voyage_id","voyage_num","voyage_models","get_box_address",
                                      "in_return_box","take_user_id").get(voyage_id=voyage_id, take_user_id=user_id)
    #voyagemod_dic = model_to_dict(voyagemod)
    return_param={
            "param":sendjson.list_json(voyagelist),
            "object":voyagemod
        }
    sendjson.set_resNode("success")
    sendjson.set_resParam(return_param)

    return sendjson.get_json()

def getpicurl(request):
    sendjson = Sendjson()
    voyage_id = request.POST["voyage_id"]

    imgurl = voyage.objects.get(voyage_id=voyage_id).imgname
    imgurl = "/mystatic/equipment/"+str(imgurl)
    sendjson.set_resNode("success")
    return_param={
            "imgurl":imgurl
    }

    sendjson.set_resParam(return_param)

    return sendjson.get_json()