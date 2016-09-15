#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys, json
from zbx_api import ZabbixAPI

# =============================
#  Configure here.

ZBX_USER = ''
ZBX_PASS = ''
ZBX_Server = 'http://10.152.64.7/zabbix' #zabbix server

cust_IP = sys.argv[1]
cust_NAME = sys.argv[2]
cust_DNS = sys.argv[3]
#cust_proxy = sys.argv[4]

# =========================================================================

#-- decide hostgroup name --
def base_dict(_customer):
    _dict = {
            "Cassandra": _customer + " Cassandra",
            "Cloudera": _customer + " Cloudera",
            "Elasticsearch": _customer + " Elasticsearch",
            "HUE Core Others": _customer + " HUE Core Others",
            "HUE Front": _customer + " HUE Front",
            "Kafka": _customer + " Kafka",
            "Kubernetes": _customer + " Kubernetes",
            "Redis": _customer + " Redis",
            "Zookeeper": _customer + " Zookeeper",
            "Conversion-Dev": _customer + " Conversion-Dev"
            }
    return _dict

def get_hostid(zapi,_ip):

    gethostid = zapi.host.get({"filter":{"ip":_ip}})[0]
    _id = gethostid["hostid"]
    return _id



class hostgroup_id:
      def __init__(self,zapi):
          self.zapi = zapi

      def hostgroup_idget(self):
          _dict = {}
          for k in self.zapi.hostgroup.get({"output":"extend"}):
              _dict[k["name"]] = k["groupid"]
          return _dict

      def hostgroup_massadd(self,host_id):
          self.zapi.hostgroup.massadd({
                                      "groups": [{"groupid": "5"}],"hosts": [{"hostid": host_id}]
                                      })

class template_id:
      def __init__(self,zapi):
          self.zapi = zapi

      def template_idget(self):
          _dict = {}
          for k in self.zapi.template.get({"output":"extend"}):
              _dict[k["name"]] = k["templateid"]
          return _dict

      #def template_massadd(self):

#------------------------------------------------------------

def main(ipaddress,customer,localdns):

# -- class --
    zapi = ZabbixAPI(ZBX_Server, use_digest_authenticate=True)
    zapi.login(ZBX_USER, ZBX_PASS)

    do_templateid=template_id(zapi)
    do_group_id=hostgroup_id(zapi)

# -- host id get --
    host_id = get_hostid(zapi,ipaddress)

# -- check kind of instance --

    if "cassandra" in localdns:
      #print base_dict(customer)['Cassandra']
      zapi.hostgroup.create({"name":base_dict(customer)['Cassandra']})

    elif "cloudera" in localdns:
      zapi.hostgroup.create({"name":base_dict(customer)['Cloudera']})

    else:
      print "nothing"

#-------------------------------------------------------------
if __name__ == '__main__':

   main(cust_IP,cust_NAME,cust_DNS)
