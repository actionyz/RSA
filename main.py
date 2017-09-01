#!/usr/bin/python
# -*- coding: utf-8 -*-
# author:4ct10n
from  models.base  import *
# import argparse


# do some mode translate ,make every args into int include files
def same_mode(args):
	# try:
		# print args
		if args.n:
			if args.n[0][:2] == '0x':
				args.n = [int(i,16) for i in args.n]
			else:
				args.n = [int(i) for i in args.n]
		if args.e:
			if args.e[0][:2] == '0x':
				args.e = [int(i,16) for i in args.e]
			else:
				args.e = [int(i) for i in args.e]
		if args.c:
			
			if args.c[0][:2] == '0x':
				args.c = [int(i,16) for i in args.c]
			else:
				args.c = [int(i) for i in args.c]	
			# print args.c
		elif args.cipherlocation:
			args.c = []
			try:
				for i in args.cipherlocation:
					# print i
					f = open(i,'r')
					args.c.append(s2n(f.read()))
					f.close()
			except Exception as e:
				print "[-] filename have soming wrong~~~"
				exit()
		# print args.c
		if args.c==[]:
			args.c = [1]
		return args
	# except Exception as e:
	# 	print "[-] args have soming wrong~~~"
	# 	exit()

#glb = [n,q,p,e]
class RSA_attack:
	def __init__(self,args):
		self.glb = [-1,-1,-1,-1]
		self.glb[0] = args.n
		self.glb[3] = args.e
		self.c = args.c
		self.m = args.mode
		self.form = args.form
	#when n,e n is small enough
	def factordb(self,glb):
		#输入参数:n
		#通过factordb.com分解n
		if len(glb[0])==1 and len(glb[3])==1:
			try:
				from models import factordb
				# if self.args.verbose:
				#     print "[*] Running: factordb module"
			except ImportError:
				print "s"
				# if self.args.verbose:
				#     print "[*] Warning: factordb module missing ( attack_method/factordb.py )"
				# return (-1,-1,-1)
			return factordb.factordb(glb)
		else:
			print replace_red("[-] factordb attack failed") 
			return glb
		#print self.q,self.p
	#when n,e1,e2(sometimes they are same) ,c
	def common_attack(self,glb,c):
		# print c,glb
		if len(glb[0])==1 and len(glb[3])==2 and len(c)==2:
			try:
				from models import common
			except Exception as e:
				raise e
			return common.common(glb,c)
		else:
			print replace_red("[-] common model attack failed")
			return glb
	#when n1,n2 e1,e2 ,c they the same factor
	def common_gcd(self,glb):
		if len(glb[0])==2 and (len(glb[3]) == 2 or len(glb[3])==1):
			try:
				from models import ext_gcd
			except Exception as e:
				raise e
			return ext_gcd.ext_gcd(glb)
		else:
			print replace_red("[-] common ext_gcd attack failed")
			return glb

	# when e==3 ,n,c
	def small_e(self,glb,c):
		# print len(glb[0]),len(c),glb[3]
		if len(c)==1 and glb[3][0]==3 and len(glb[0])==1:
			try:
				from models import small_e_attack
			except Exception as e:
				pass
			return small_e_attack.small_e_attack(glb,c)
		else:
			print replace_red("[-] common ext_gcd attack failed")
			return glb
	# when n,e,c
	def wiener_attack(self,glb):
		if len(glb[0])==1 and len(glb[3])==1:
			try:
				from models import wiener_attack
			except Exception as e:
				pass
			# print 1
			return wiener_attack.wiener_attack(glb)
		else:
			print replace_red("[-] wiener attack had failed")
			return glb
	def hastads_extend(self,glb,c):
		if len(glb[0])==len(c)==3 and len(glb[3])==1:
			try:
				from models import hastads_extend
			except Exception as e:
				pass
			array = hastads_extend.hastads_extend(glb,c)
			glb[0][0]= array[1]
			return self.small_e(alb,array[0])
		else:
			print replace_red("[-] hastads extend attack had failed")
			return glb			

	def output(self,glb,c,form):
		# print glb
		if len(glb) ==5 or (glb[1]!=-1 and glb[2]!=-1 ):
			decrypt(glb,c,form)
			exit()
		else:
			print replace_red("[-] all method had failed")


	def start(self):
		# from models import factordb
		if self.m == '0':
			self.glb = self.factordb(self.glb)
			if self.glb[1] != -1:
				print replace_green("[+] factordb devide success ") 
				return 1
			self.glb = self.common_attack(self.glb,self.c)
			if len(self.glb) == 5:
				print replace_green("[+] common_attack success ") 
				return 1			
			self.glb = self.wiener_attack(self.glb)
			if self.glb[1] != -1:
				print replace_green("[+] wiener_attack success ") 	
				return 1		
			self.glb = self.hastads_extend(self.glb,self.c)
			if len(self.glb) == 5:
				print replace_green("[+] hastads_extend success ") 	
				return 1	
			self.glb = self.small_e(self.glb,self.c)
			if len(self.glb) == 5:
				print replace_green("[+] small_e success ") 	
				return 1		
		if self.m == 'wm':
			pass
		if self.m == 'pq':
			pass
		if self.m == 'rb':
			pass
		# print self.glb
		#self.glb = [-1,-1,-1,-1]

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Bendawang\'s RSA CTF Tool',formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('-m','--mode',default='0',required=True,choices=['0','brute','cma','wn'],help='''\n选择模式\n0     : 给定一定数量的n,e，程序自动爆破私钥\nbrute ：指定使用暴力分解n的方法(yafu,fermat,factordb)进行攻击\ncma   : 指定使用共模攻击(Common Modulus Attack)进行攻击，需要：n,e1,e2,c1,c2\nwn    : 指定使用低私钥指数攻击(Wiener\'s attack)进行攻击\n\n''')
    parser.add_argument('-v','--verbose', help='输出详细过程', action='store_true')
    parser.add_argument('-p','--private', help='设定此参数之后破解出的私钥将以openssl私钥文件形式输出', action='store_true')
    parser.add_argument('-n',required=True,nargs='*',help='输入公玥中n的十进制数值，与e数值一一对应，可以输入多个')
    parser.add_argument('-e',required=True,nargs='*',help='输入公玥中e的十进制数值，与n数值一一对应，可以输入多个')
    parser.add_argument('-c',nargs='*',help='输入密文十进制数值')
    parser.add_argument('-cl','--cipherlocation',nargs='*',help='被加密文件绝对路径，支持*和?')
    parser.add_argument('-htime','--hastads_timeout',help='设置hastads的爆破时间')
    parser.add_argument('-ftime','--fermat_timeout',help='设置fermat的爆破时间')
    parser.add_argument('-f','--form',default='str',help='设置解密输出格式int hex str')

    args = parser.parse_args()
    args = same_mode(args)#translate modes to the same
    atk = RSA_attack(args)
    atk.start()
    # print atk.glb
    atk.output(atk.glb,atk.c,atk.form)
    # print atk.c
    # print args.p
    #-m 0 -n 11 22 -e 22
    
    # 文件输入的密文转换成数值形式便于计算
