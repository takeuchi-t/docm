※
#!/bin/sh

Insta_id="i-0c18d1c73ba7a2794"

get_int_id() {
         insta_id=$1
         getid=`aws ec2 \
         describe-network-interfaces \
         --filters Name=attachment.instance-id,Values=${insta_id} \
         --output json | jq -r '.NetworkInterfaces[].NetworkInterfaceId'`
         return getid
}

get_sg_id() {
         insta_id=$1
         getsgid=`aws ec2 \
         describe-network-interfaces \
         --filters Name=attachment.instance-id,Values=${insta_id} \
         --output json | jq -r '.NetworkInterfaces[].Groups[].GroupId'`
         return getsgid
}

sg_create=`aws ec2 \
           create-security-group --group-name hms-operation \
           --description "hms-operation" \
           --vpc-id vpc-4ef1ef2b`

#if [ 0 = $?]; then

sg_adapt=`aws ec2 \
          modify-network-interface-attribute \
"AWS_getinfo.sh" 40L, 972C                                                                                                               1,1          先頭
#!/bin/sh

Insta_id="i-0c18d1c73ba7a2794"

get_int_id() {
         insta_id=$1
         getid=`aws ec2 \
         describe-network-interfaces \
         --filters Name=attachment.instance-id,Values=${insta_id} \
         --output json | jq -r '.NetworkInterfaces[].NetworkInterfaceId'`
         return getid
}

get_sg_id() {
         insta_id=$1
         getsgid=`aws ec2 \
         describe-network-interfaces \
         --filters Name=attachment.instance-id,Values=${insta_id} \
         --output json | jq -r '.NetworkInterfaces[].Groups[].GroupId'`
         return getsgid
}

sg_create=`aws ec2 \
           create-security-group --group-name hms-operation \
           --description "hms-operation" \
           --vpc-id vpc-4ef1ef2b`

#if [ 0 = $?]; then

sg_adapt=`aws ec2 \
          modify-network-interface-attribute \
          --network-interface-id get_int_id($Insta_id) \
          --groups get_sg_id($Insta_id)`

#  echo "OK"

#else

#  echo "NG"
#fi
