# -*- coding:utf-8 -*- 
#加/解密的整合
import base64
import hashlib

def tob64(b64):									#筛选base64的base64解密					
	try:
		a=base64.b64decode(b64).decode()
		return(a)
	except:
		return('')

def tocas(Ciphertext):                          #只包含字母的凯撒加密
	Ciphertext = Ciphertext.strip()
	calist = []
	for i in range(1, 26):
		# print(chr(65 + i) + ":", end=" ")
		y = []
		for a in Ciphertext:
			x = ord(a)
			if (65 <= x <= 90):
				x = x + i
				if x > 90:
					x = x - 90 + 65 - 1
					y.append(chr(x))
				else:
					y.append(chr(x))
			elif (97 <= x <= 122):
				x = x + i
				if x > 122:
					x = x - 122 + 97 - 1
					y.append(chr(x))
				else:
					y.append(chr(x))
		end = ''.join(y)
		calist.append(end)
	return(calist)
	
def toca128(lstr):                                #全ASCII的凯撒加密
	ca128list=[]
	for p in range(127):  
		str1 = ''  
		for i in lstr:  
			temp = chr((ord(i)+p)%127)  
			if 32<ord(temp)<127 :  
				str1 = str1 + temp   
				feel = 1  
			else:  
				feel = 0  
				break  
		if feel == 1:  
			ca128list.append(str1)
	return(ca128list)
		
def tomd5(md5str):
	m = hashlib.md5()
	m.update(md5str.encode())
	return (m.hexdigest())