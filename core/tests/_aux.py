from collections import OrderedDict


MARK = OrderedDict(
            {
                'facebookId': 4, 'name': 'Mark Zuckerberg', 'gender': 'Not in facebook', 'email': 'Not in facebook',
                'links': {'self': 'http://localhost:8007/persons/4/'}
            }
       )


SARAH = OrderedDict(
         {"facebookId":1399,"name":"Sarah Ellison","gender":"Not in facebook","email":"Not in facebook",
          "links":{"self":"http://localhost:8007/persons/1399/"}}
)

HAYS = OrderedDict(

        {"facebookId":1299,"name":"Alexandra Hays","gender":"Not in facebook","email":"Not in facebook",
        "links":{"self":"http://localhost:8007/persons/1299/"}}
   )

EXISTS = {"facebookId":["Facebook Users com este Id já existe."]}
NOT_EXISTS = {"detail":"Não encontrado."}


__base_url = 'http://localhost:8007/persons/'
__base_cmd = 'curl --user admin:master.21'
__cmd = __base_cmd+' '+__base_url

def get_curl(cmd, prm=None):
    prm = str(prm)
    if cmd == 'post':
        return __base_cmd +' --data "facebookId='+prm+'" '+__base_url
    elif cmd == 'delete':
        return __base_cmd + ' -X DELETE '+__base_url+prm
    elif cmd == 'list':
        return __cmd
    elif cmd=='limit':
        return __cmd+'?limit='+prm


