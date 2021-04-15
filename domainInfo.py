# encoding=utf-8
# 2021/4/14
# 将txt文件中的url批量转变为主机IP地址

import urllib.request
import xlsxwriter
import time
import argparse




def getUrlIp(urlFile):	
	f = open(urlFile)
	lines = f.readlines()
	urls = []
	for i in lines:
		line = i.strip('\n')
		urls.append(line)
	opener = urllib.request.build_opener()
	opener.addheaders = [('User-agent',
                             'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36')]
	now = time.time()
	excle1 = xlsxwriter.Workbook("{0}.xlsx".format(now))
	worksheet = excle1.add_worksheet()
	worksheet.write("A1","目标URL")
	worksheet.write("B1","解析IP地址")
	for j in range(len(urls)):
		url = urls[j]
		response = opener.open("{}".format(url), timeout=5)
		ip_port = response.fp.raw._sock.getpeername()[0]		
		worksheet.write(j+1,0,urls[j])
		worksheet.write(j+1,1,ip_port)
	print("文件创建完成，请查看当前目录下新生成文件!")
	excle1.close()

		
if __name__ == '__main__':
	print("-------------------------------------------------------------------")
	print("-----by NineMeet")
	print("-------------------------------------------------------------------")
	try:
		parser = argparse.ArgumentParser()
		parser.add_argument("-f","--file", help="添加解析的url文件列表", type=str)
		parser.add_argument("-o","--output", help="输出到文件，保存形式暂时支持Excel", type=int,required = False)
		args = parser.parse_args()
		urlFile = args.file
		getUrlIp(urlFile)
	except Exception as e:
		print("你需要进行传参才能保证程序的运行！！！！")
