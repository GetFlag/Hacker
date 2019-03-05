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

from_station=stations[input("���������վ: \n")]
to_station=stations[input("�����뵽��վ: \n")]
train_date=input("�������������(��ʽxxxx-xx-xx): \n")
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

	print("����"+tmp_list[3]+"  ����ʱ��:"+tmp_list[8]+"  ����ʱ��:"+tmp_list[9]+"  ��ʱ:"+tmp_list[10]+"  ���ԣ�"+tmp_list[23]+"  ������"+tmp_list[26]+"  Ӳ�ԣ�"+tmp_list[28]+"  Ӳ����"+tmp_list[29])
print('�ó��δ��� %d ���г�' %row)