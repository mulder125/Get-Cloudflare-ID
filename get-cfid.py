import requests
import json

#讀取config(JSON格式)
with open('config.txt', 'r', encoding="utf-8") as rcfg:
    config_array = json.load(rcfg)

#讀出各參數
Email = config_array['Email']
G_Key = config_array['G_Key']
ctype = config_array['ctype']
Zone_id = config_array['Zone_id']
cfurl = config_array["url"]

#url部分
url = cfurl + Zone_id + '/dns_records'
#headers部分
headers = {
    'x-auth-email': Email,
    'x-auth-key': G_Key,
    'content-type': ctype,
}

#顯示參數 for debug
#print(config_array['Email'])
#print(config_array['G_Key'])
#print(config_array['ctype'])
#print(config_array['Zone_id'])
#print(url)
#print(headers)

#Get Record ID 主程式 (curl -X GET url+headers)
res=requests.get(url=url, headers=headers)

#結果存到data.json
with open("res.txt", "w", encoding="utf-8") as wjf:
    wjf.write(res.text)

#讀出data.json到data    
with open('res.txt', 'r', encoding="utf-8") as rjf:
    jdata = json.load(rjf)

#篩出result後方資料到clist   
clist=jdata["result"]

#將clist的Record ID+域名儲存到cf_id.txt
with open("cf_id.txt", "w", encoding="utf-8") as cdid:
    cdid.write("Gobal KEY : " + G_Key + "\n" )
    print("Gobal KEY : ", G_Key)    
    for lis in clist:
        cdid.write(lis["name"].ljust(25) + "ID : " + lis["id"].ljust(36) + "TYPE : " + lis["type"] + "\n")
        print(lis["name"].ljust(25), "ID : ", lis["id"].ljust(36), "TYPE : ", lis["type"].ljust(8) )