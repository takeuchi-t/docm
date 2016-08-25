#メモ

http://www.cloudera.co.jp/doc/cm/introduction/primer.html

http://perezvon.hatenablog.com/entry/20091026/1256552181

http://dev.classmethod.jp/cloud/aws-cli-params-from-json/

https://github.com/gescheit/scripts/blob/master/zabbix/examples/zabbix_item_add_example.py

------------------------------------------------

#!/usr/bin/python
# coding: UTF-8

'''
Created on 01.10.2010
@author: gescheit
'''
from zbx_api import ZabbixAPI

server="http://127.0.0.1/zabbix"
username="admin"
password="zabizabi"
zapi = ZabbixAPI(server=server, path="", log_level=6)
zapi.login(username, password)


##ホスト確認
hostid=zapi.host.get({"filter":{"host":"ABCD"}})[0]

##テンプレート確認
hostid=zapi.template.get({"filter":{"name":"Template ICMP Ping"}})[0]

##ホストグループ確認
#hostid=zapi.hostgroup.get({"filter":{"groups":"zabbix server"}})[0]

##ホスト登録
hostid=zapi.host.create({"host":"test005", \
"interfaces":[{"type":1,"main":1,"useip":1,"dns":"","ip":"172.16.1.20","port":"10050"}], \
"groups":[{"groupid":"2"}],"templates":[{"templateid":"10104"},{"templateid":"10047"}]})[0]

print hostid

