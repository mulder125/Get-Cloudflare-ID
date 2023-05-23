import requests
import json

#讀取config(JSON格式)
with open('config.txt', 'r', encoding="utf-8") as rcfg:
    config_array = json.load(rcfg)

# Cloudflare API账户信息
email = config_array['Email']
api_key = config_array['G_Key']
zone_name = config_array['domain']  # 要获取 Zone ID 的域名

# 发起 API 请求获取 Zone ID
url = f"https://api.cloudflare.com/client/v4/zones?name={zone_name}"
headers = {
    "Content-Type": "application/json",
    "X-Auth-Email": email,
    "X-Auth-Key": api_key,
}
response = requests.get(url, headers=headers)
data = response.json()

#從data中抓出Zone ID 存到 zone_id
if response.status_code == 200 and data["success"]:
    zone_id = data["result"][0]["id"]
    print(f"Zone ID for '{zone_name}' is: {zone_id}")
else:
    print("Failed to get Zone ID:", data["errors"])

# 发起 API 请求获取所有 DNS 记录
url = f"https://api.cloudflare.com/client/v4/zones/{zone_id}/dns_records"
headers = {
    "Content-Type": "application/json",
    "X-Auth-Email": email,
    "X-Auth-Key": api_key,
}

res = requests.get(url, headers=headers)

#顯示參數 for debug
#print(config_array['Email'])
#print(config_array['G_Key'])
#print(config_array['ctype'])
#print(config_array['zone_id'])
#print(url)
#print(headers)

#結果存到res.txt (json格式)
#with open("res.txt", "w", encoding="utf-8") as wjf:
#    wjf.write(res.text)

#篩出result後方資料到clist   
data = res.json()
clist=data["result"]

#將clist的Record ID+域名儲存到cf_id.txt
with open("cf_id.txt", "w", encoding="utf-8") as cdid:
    cdid.write("Domain : " + zone_name + "\n" )    
    cdid.write("Zone ID : " + zone_id + "\n" ) 
#    print("Domain : ", zone_name) 
#    print("Zone ID : ", zone_id)         
    for lis in clist:
        cdid.write(lis["name"].ljust(32) + "ID : " + lis["id"].ljust(36) + "TYPE : " + lis["type"] + "\n")
        print(lis["name"].ljust(32), "ID : ", lis["id"].ljust(36), "TYPE : ", lis["type"].ljust(8) )