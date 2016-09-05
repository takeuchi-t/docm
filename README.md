URL
https://mail.worksap.co.jp/webmail2

アドレス
takeuchi_t@worksap.co.jp

getinfo=zapi.host.get({"filter":{"name":"pc"}})[0]
print getinfo["host"],getinfo["name"],getinfo["hostid"]


#!/usr/bin/python
# coding: utf8
import boto,boto.ec2
from boto.ec2.connection import EC2Connection

AWS_ACCESS_KEY = 'AKIAJZBPOOQGSDMPNIWA'
AWS_SECRET_ACCESS_KEY = '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'

def main():
    conn = EC2Connection(aws_access_key_id=AWS_ACCESS_KEY ,aws_secret_access_key=AWS_SECRET_ACCESS_KEY)

    region = conn.get_all_regions()
    asia_conn = region[6].connect(aws_access_key_id=AWS_ACCESS_KEY ,aws_secret_access_key=AWS_SECRET_ACCESS_KEY)

    rsv = asia_conn.get_all_instances(instance_ids="i-0c18d1c73ba7a2794")
    print rsv

if __name__ == '__main__':
    main()

