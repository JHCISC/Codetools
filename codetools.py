# -*- coding:utf-8 -*- 
import sys
from codeprocess import *
from textprocess import *
def getpar():             #获取参数
	function=['-base64','-md5','-casear','-ca128','-u','-o','-match'] #参数菜单
	codelist=['-base64','-md5','-casear','-ca128']
	intlink = ''
	seccode = ''
	matstr = ''
	cmd = sys.argv[1:]    #获得命令行输入参数
	#print(cmd)
	#print(function.index(cmd[0])) #拿到第一段命令
	if  '-u' in cmd:
		intlink = cmd[cmd.index('-u')+1] #捕捉输入字符
		outlink = ''          #-u输入情况下不存在输出路径
		if cmd[1] in codelist:
			seccode = cmd[1]
		
	else:
		if cmd[1] in function: #是否为两次加密获得输入路径
			intlink = cmd[2]
			seccode = cmd[1]       #这是二次加密的类型
		else:
			intlink = cmd[1]
		#print(intlink)
		if '-o' in cmd: #是否指定输出路径
			outlink = cmd[cmd.index('-o')+1] #捕捉输出路径
		else:
			outlink = cmd[0][1:] + seccode[1:] + intlink 	
	if	'-match' in cmd: #对比功能
		matstr = cmd[cmd.index('-match')+1]      #拿到匹配对象
	return(intlink,cmd[0][1:],seccode[1:],outlink,matstr) #输入路径，编码类型1，编码类型2，输出路径,对比字符串
version = '1.0.0_Alpha'
helpword='''
CODETOOLS 帮助-显示CODETOOLS的使用
命令范例: 
$ python codetools.py -ca128 -base64 expinput.txt -o expoutput.txt -match test
  本次模式为:('expinput.txt', 'ca128', 'base64', 'expoutput.txt', 'test')
  结果保存为:expoutput.txt
  匹配结果为False
说明:
对expinput.txt的内容先进行全ASCII字符的凯撒解密爆破，然后对127个结果进行base64解密，将正确的结果保存在expoutput.txt中，并检查结果是否包含‘test’

其他范例：
$python codetools.py -base64 -base64 -u abcdef
$python codetools.py -md5 a.txt -match 'c4ca4238a0b923820dcc509a6f75849b'
$python codetools.py -base64 -u MQ== match 1


加解密指令:		(最多支持一行命令中加解密2次)
-base64			base64解密(对无法解码的字符返回空值)
-md5			md5加密
-casear			不区分大小写26位英文字母的凯撒加密
-ca128			128位ASCII的凯撒加密
...

选择加解密对象指令：
-u			表示加解密对象是下一个字符串,-u情况下暂不支持输出到指定文件
			没有-u情况下的下一个字符串为对象文件名称
-o			表示加解密对象的结果文件指定为 （如有同名文件则覆盖）
			没有-o情况下程序自动命名 （如有同名文件则覆盖）
				
其他功能：
-match			表示判断下一个字符串是否被加解密结果包含
-help  			显示帮助
-version 		显示版本


'''

if len(sys.argv[1:])>=1:  #判断是否有参数输入
	if ('-help' in (sys.argv[1:]))and(len(sys.argv[1:])==1):
		print(helpword)
	elif ('-version' in (sys.argv[1:]))and(len(sys.argv[1:])==1):
		print(version)
	else:
		intlink,fircode,seccode,outlink,matstr= getpar()
		print('本次模式为:'+str(getpar()))
		result = ''
		if  outlink != '':           
			l2line(intlink,fircode,outlink)
			if seccode != '':
				l2line(outlink,seccode,outlink)
			print('结果保存为:'+outlink)
		
		else:                                           #-u模式则直接输出
			if seccode == '':
				result = mcode(fircode,intlink)
			else:
				result = mcode(seccode,mcode(fircode,intlink))
			print('结果为:'+str(result))
		if matstr != '':
			print('匹配结果为'+str(difstr(outlink,matstr,result)))
	
else:
	print('''CODETOOLS
-help查看帮助''')
	