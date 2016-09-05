URL
https://mail.worksap.co.jp/webmail2

アドレス
takeuchi_t@worksap.co.jp

getinfo=zapi.host.get({"filter":{"name":"pc"}})[0]
print getinfo["host"],getinfo["name"],getinfo["hostid"]
