import requests
import json

# 读取config(JSON格式)
with open('cfg.txt', 'r', encoding="utf-8") as rcfg:
    config_array = json.load(rcfg)

# Cloudflare API账户信息
email = config_array['Email']
api_key = config_array['G_Key']
domains = config_array['domains']  # 多个域名列表

def get_zone_id(domain):
    url = f"https://api.cloudflare.com/client/v4/zones?name={domain}"
    headers = {
        "Content-Type": "application/json",
        "X-Auth-Email": email,
        "X-Auth-Key": api_key,
    }
    response = requests.get(url, headers=headers)
    data = response.json()
    if response.status_code == 200 and data["success"]:
        return data["result"][0]["id"]
    else:
        print(f"Failed to get Zone ID for {domain}: {data['errors']}")
        return None

def get_dns_records(zone_id):
    url = f"https://api.cloudflare.com/client/v4/zones/{zone_id}/dns_records"
    headers = {
        "Content-Type": "application/json",
        "X-Auth-Email": email,
        "X-Auth-Key": api_key,
    }
    res = requests.get(url, headers=headers)
    return res.json()["result"]

# 遍历每个域名
for domain in domains:
    zone_id = get_zone_id(domain)
    if zone_id:
        dns_records = get_dns_records(zone_id)

        # 输出到文件
        with open(f"{domain}_dns_records.txt", "w", encoding="utf-8") as f:
            f.write("Domain : " + domain + "\n")
            f.write("Zone ID : " + zone_id + "\n\n")
            for record in dns_records:
                f.write(f"{record['name'].ljust(32)} ID : {record['id'].ljust(36)} TYPE : {record['type']}\n")

        # 打印到控制台 (可自定义输出格式)
        print(f"For domain {domain}:")
        for record in dns_records:
            print(f"  {record['name'].ljust(32)} ID : {record['id'].ljust(36)} TYPE : {record['type']}")
