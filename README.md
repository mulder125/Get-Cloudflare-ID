# GET_CF_ID
Get CF ID
通過Cloudflare API V4 獲取 Zone ID & Record ID，並輸出到螢幕和文字檔(cf_id.txt)


請自行在根目錄建立config.txt，並填上Cloudflare的帳號資訊(Email, Gobal API KEY, Domain)
以下為範例

{
	"Email": "aaa@bbb.ccc",
	"G_Key": "xxxxxxxxxxxxxxxxxxxxxxx",
	"domain": "aaa.bbb"
}


運行方式: python get-cfid.py
