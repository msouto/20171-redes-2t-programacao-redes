import json
name = dict(first='bob', last='smith')
registro=dict(name=name,job=['dev','mgr'],idade=45)
print(registro)
f=open('datafile.json','w')
json.dump(registro,f,indent=4)
f.close()
