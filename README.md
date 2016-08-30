※メモ

dict.fromkeys(['name'])

obj.get()

obj.keys()

json.dumps(obj)

getinfo=zapi.host.update({"hostid":"10105","templates":[{"templateid":"10047"}]})

getinfo=zapi.host.get({"filter":{"name":"pasca.luna.ddns.vc"}})[0]
print getinfo["host"],getinfo["name"],getinfo["hostid"]
