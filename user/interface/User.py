from django.shortcuts import *

from common.sendjson import Sendjson
from user.models import *
import uuid

def log(request):
        sendjson = Sendjson()
        in_username = request.POST["username"]
        in_password = request.POST["password"]
        try:
            userlogin = login.objects.get(username=in_username, password=in_password)
            if(userlogin.user_id == None):
                sendjson.set_resNode("improve")
                return_param = {
                    "userlogin":userlogin.login_ID
                }
                sendjson.set_resParam(return_param)
            else:
                sendjson.set_resNode("success")
                token = str(uuid.uuid1())
                userlogin.token = token
                userlogin.save()
                return_param = {
                    "userlogin": userlogin.login_ID,
                    "user_id":userlogin.user_id
                }
                sendjson.set_resParam(return_param)
                sendjson.set_reSession_ID(token)
        except Exception as e:
            sendjson.set_resNode("password wrong")
        return sendjson.get_json()

def aslog(query):
        sendjson = Sendjson()
        sendjson.set_resNode("success")
        params = {
            "userlogin":query.login_ID,
            "user_id":query.user_id
        }
        sendjson.set_resParam(params)
        return sendjson.get_json()

def checkpassword(request):
        sendjson = Sendjson()
        loginid = request.POST["loginid"]
        password = request.POST["password"]
        try:
            login.objects.get(login_ID=loginid,password=password)
            sendjson.set_resNode("success")
        except:
            sendjson.set_resNode("wrong password")
        return sendjson.get_json()

def changpassword(request):
        sendjson = Sendjson()
        loginid = request.POST["loginid"]
        password = request.POST["password"]
        try:
            changlog = login.objects.get(login_ID=loginid)
            changlog.password = password
            changlog.save()
            sendjson.set_resNode("success")
        except:
            sendjson.set_resNode("false")
        return sendjson.get_json()

def listview(request):
        sendjson = Sendjson()
        user_id = request.POST["user_id"]
        try:
            list = order.objects.get(user_id=user_id)
            return_param = {
                "param": sendjson.list_json(list)
            }
            sendjson.set_resNode("success")
            sendjson.set_resParam(return_param)
        except:
            sendjson.set_resNode("error")


def register(request):
        sendjson = Sendjson()
        reg_username = request.POST["username"]
        reg_password = request.POST["password"]
        getlog = login.objects.get_or_create(username=reg_username,password=reg_password)
        if(getlog[1]):
            login_ID = login.objects.get(username=reg_username, password=reg_password).login_ID
            request.session['log_id'] = login_ID
            sendjson.set_resNode("success")
        else:
            sendjson.set_resNode("this name is been used")
        return sendjson.get_json()
