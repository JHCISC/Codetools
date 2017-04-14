# -*- coding:utf-8 -*- 
#用于处理txt逐行内容
from codeprocess import *
def l2line(intlink,code,outlink): 
	codetxt = open(intlink,encoding='utf-8') #utf格式打开记事本
	line = codetxt.readline()
	readtxt=[]
	while line:
		if code == 'md5':
			line = tomd5(line)
			readtxt.append(line)
		elif code == 'base64':
			line = tob64(line)
			readtxt.append(line)
		elif code == 'casear':
			readtxt = tocas(line)
		elif code == 'ca128':
			readtxt = toca128(line)
		line=codetxt.readline()
	stext = '\r'.join(readtxt)                  #从list里读取每行以回车分割
	wfile = open(outlink,'w',encoding='utf-8')  
	wfile.write(stext);  
	wfile.close()  
	codetxt.close()
	
#用于-u模式下的字符串到编码模式
def mcode(code,str):
	if code == 'md5':
		return(tomd5(str))
	elif code == 'casear':
		return(tocas(str))
	elif code == 'ca128':
		return(toca128(str))
	elif code == 'base64':
		if tob64(str) == '':
			return ('base64错误')
		else:
			return(tob64(str))

		
#用于对比字符串
def difstr(dol,dstr,dru):   #需要最终输出位置，对比字符串，和数据处理结果三个参数
	if dstr == '':
		return ''
	else:
		if dol =='':
			return (dstr in dru)
		else:
			matchlist = []										#读取记事本行到list
			matchtxt = open(dol,encoding='utf-8')
			matchline = matchtxt.readline()
			while matchline:
				matchlist.append(matchline)
				matchline = matchtxt.readline()
			print (matchlist)
			logic=False             
			i=0
			for matchlist[i] in matchlist:
				logic=(dstr in matchlist[i])or logic           #引用或运算，一个为真即为真
				i+1
			return logic
		

