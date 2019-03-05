#coding=gbk
import re
import requests

#url=https://kyfw.12306.cn/otn/leftTicket/queryA?leftTicketDTO.train_date=2018-10-01&leftTicketDTO.from_station=BJP&leftTicketDTO.to_station=CDW&purpose_codes=ADULT

url="https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9069"
req=requests.get(url,verify=False)
reg="([\u4e00-\u9fa5]+)\|([A-Z]+)"
result_addr=re.findall(reg,req.text)
stations=dict(result_addr)
#print(stations)

from_station=stations[input("请输入出发站: \n")]
to_station=stations[input("请输入到达站: \n")]
train_date=input("请输入出发日期(格式xxxx-xx-xx): \n")
url1="https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date="+str(train_date)+"&leftTicketDTO.from_station="+str(from_station)+"&leftTicketDTO.to_station="+str(to_station)+"&purpose_codes=ADULT"
#print(url1)
r = requests.get(url1, verify=False)
#print(r.text)
res = r.json()['data']['result']
#res = r.json()
print(res)
row = len(res)
for i in res:
	tmp_list=i.split("|")

	print("车次"+tmp_list[3]+"  发车时间:"+tmp_list[8]+"  到达时间:"+tmp_list[9]+"  历时:"+tmp_list[10]+"  软卧："+tmp_list[23]+"  无座："+tmp_list[26]+"  硬卧："+tmp_list[28]+"  硬座："+tmp_list[29])
print('该车次存在 %d 次列车' %row)