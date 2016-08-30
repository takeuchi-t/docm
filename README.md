※メモ

dict.fromkeys(['name'])

obj.get()

obj.keys()

json.dumps(obj)

getinfo=zapi.host.update({"hostid":"10105","templates":[{"templateid":"10047"}]})

getinfo=zapi.host.get({"filter":{"name":"pasca"}})[0]
print getinfo["host"],getinfo["name"],getinfo["hostid"]

------------------------------------------------------------------

#!/bin/sh

IPADD=$1

CMD(){

expect -c "

set timeout 3

spawn ssh vyos@${IPADD}

expect '(yes/no)?' ; send \"yes\n\"

expect 'password:' ; send \"vyos\n\"

expect '~$' ; send \"exit\n\"

#expect

#send

#expect

interact

"

}
