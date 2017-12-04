from django.contrib.sessions.models import Session
from user.models import *

def chack_requset_type(request):
    if(request.method == "GET"):
        print("Get")
        return False
    elif(request.method == "POST"):
         sessionid = request.POST["token"]
         print(request.POST["method"])
         try:
            print(sessionid)
	    #免密登录
            aslog = login.objects.get(token=sessionid)
            print(aslog.login_ID)
            return aslog
         except:
             return False
