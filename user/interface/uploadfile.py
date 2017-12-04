import os
from django import forms

from common.sendjson import Sendjson
from pyproject import settings
from user.models import user_info

class uploadfile(forms.Form):
    token = forms.CharField()
    method = forms.CharField()
    userid = forms.CharField()
    imgtype = forms.CharField()
    photo = forms.FileField()


def upload(request):
    sendjson = Sendjson()
    uf = uploadfile(request.POST, request.FILES)
    print("wait")
    if uf.is_valid():
        print("success")
        user_id = uf.cleaned_data["userid"]
        imgtype = uf.cleaned_data["imgtype"]
        img = uf.cleaned_data["photo"]

        if(imgtype == "car_id"):
            path = "static/uploadcar/";
            handle_uploaded_file(img, user_id,path)
            user_info.objects.filter(user_id=user_id).update(car_id=img)

        elif(imgtype == "driver_id"):
            path = "static/uploaddriver/";
            handle_uploaded_file(img, user_id,path)
            user_info.objects.filter(user_id=user_id).update(driver_id=img)
        param = {
            "car_path": path + user_id + "_" + img.name
        }
        sendjson.set_resParam(param)
        sendjson.set_resNode("success")
    else:
        uf = uploadfile()
        print("false")
        sendjson.set_resNode("fales")
    return sendjson.get_json()

def handle_uploaded_file(f,user_id,path):
    with open(path+user_id+'_'+f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)