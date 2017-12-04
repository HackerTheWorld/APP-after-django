import json

class Sendjson():

    def __init__(self):
        self.res = {}

    def set_resNode(self,str):
        self.res["resNode"]=str

    def set_resParam(self,str):
        self.res["resParam"]=str

    def set_reSession_ID(self,str):
        self.res["session_id"] = str.strip('-')
    def get_json(self):
        context =  json.dumps(self.res,ensure_ascii=False)
        print(context)
        return context

    def list_json(self,str):
        jsonarray =[]
        for i in range(len(str)):
              jsonarray.append(str[i].__dict__)
              jsonarray[i].pop('_state')
              for k in jsonarray[i].keys():
                  try:
                      jsonarray[i][k] = jsonarray[i][k].strftime('%Y-%m-%d %H:%S:%M')
                  except :
                      continue
        return jsonarray

