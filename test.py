#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys, json
from zbx_api import ZabbixAPI

# =============================
#  Configure here.

ZBX_USER = 'takeuchi_t'
ZBX_PASS = 'takeuchi_t'
ZBX_Server = 'http://10.152.64.7/zabbix' #zabbix server

cust_IP = sys.argv[1]
cust_NAME = sys.argv[2]
cust_DNS = sys.argv[3]
#cust_proxy = sys.argv[4]

# =========================================================================

# --- ZBX class --- 
class ZBX_class:
	
      def __init__(self,zapi):
          self.zapi = zapi

# --- get id method ---
      def get_hostID(self,hostip):
      	  # -- ip address was must be unique number --
          return self.zapi.host.get({"filter":{"ip":hostip}})[0]["hostid"]

      def get_hostgroupID(self,group_name):
          return self.zapi.hostgroup.get({"filter":{"name":group_name}})[0]["groupid"]

      def get_templateID(self,temp_name):
          return self.zapi.template.get({"filter":{"host":temp_name}})[0]["templateid"]

# --- mass add method ---
      def hostgroup_massadd(self,host_id,gropu_id):
          self.zapi.hostgroup.massadd({
                                      "groups": [{"groupid": gropu_id}],
                                      "hosts": [{"hostid": host_id}]})
                                      
      def hostname_massadd(self,host_id,host_name):
          self.zapi.host.massadd({
                                  "hosts": [{"hostid": host_id},
                                            {"name": host_name}],})

      def interface_massadd(self, host_id, host_ip, ip_port):
          pass


      def template_massadd(self,_temp):
          pass
          
          
#-- decide hostgroup name --
def hgroup_dict(_customer):
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


# -- select host group --
def HostGroup(localdns):
    
    if "cassandra" in localdns: 
           return ["Cassandra","HUE Cassandra Template"]
    elif  "cassandra1" in localdns:
           return ["Cassandra","HUE Cassandra Template"]

           
           
#------------------------------------------------------------

def main(ipaddress,customer,localdns):

# -- class --
    zapi = ZabbixAPI(ZBX_Server, use_digest_authenticate=True)
    zapi.login(ZBX_USER, ZBX_PASS)
    ZBX = ZBX_class(zapi)

# -- host id get --
    HostID = ZBX.get_hostID(ipaddress)

# -- check kind of instance --
    #ZBX.hostname_massadd(HostID,localdns)

# -- add host group
    #ZBX.hostgroup_massadd(HostID,HostGroup(localdns))

    print HostGroup(localdns)[0]


#-------------------------------------------------------------
if __name__ == '__main__':

   main(cust_IP,cust_NAME,cust_DNS)