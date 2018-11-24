#!/usr/bin/env python
#-*-coding:utf-8-*-
# BlackEngineer By Deray
# Report bug on my other sosmed
# https://facebook.com/achmadluthfi.hadi.3
# https://instagram.com/reyy05_
# Manual Color
W = '\033[1;37m' 
N  = '\033[0m' 
R = '\033[31m'
G  = '\033[1;32m' 
O  = '\033[1;37m\033[33m'
from base64 import b16decode
from json import loads as beban
from sys import exit as keluar
from os import system as perintah
from os import remove as apus
from urllib import urlretrieve as download
from raw.tools.ckerfb import *
from raw.printf import *
from raw.requirements import *
try:
	import requests
	from requests import post as put
	from requests import get as ambil
except:
	penginstalan()
# TOOLS
from raw.tools.access_token import *
from raw.tools.postid import *
from raw.tools.massComments import *
from raw.tools.getpostID import *
from raw.banner import *
# SYSDEFAULT MODULES
from time import sleep as tidur
import base64
import cacheclean
cacheclean.cache()
perintah('clear')
def banner():
	print(""" \033[1;36m
┌════════════════════════════════════════┐
█                                        █
█        Generate Access Token           █ 
█                                        █
└════════════════════════════════════════┘     \n \033[1;m""")
# INDEX
class main():
	def __init__(self,*args,**kwargs):
		self.tete="68747470733A2F2F706173746562696E2E636F6D2F7261772F4C6630374565315A"
		self.kiko=[]
		self.lol=[]
		self.teman=[]
		self.lives()
		self.cek()
		raw_input("\033[1;32m*\033[0mpress enter to menu ...")
		perintah('clear')
		self.menu()
	def lives(self):
		try:
			open('raw/tools/lives/lives.txt')
		except:
			printf('salah/* downloading resources ...')
			try:
				b=base64.b16decode(self.tete)
				download(b,'raw/tools/lives/lives.txt')
				printf('notice/* downloading ok!')
				raw_input("\033[1;32m*\033[0mpress enter to menu ...")
				perintah('clear')
				self.menu()
			except Exception as f:
				printf('\nsalah/* connection rijected.')
				keluar()
	# Menu
	def menu(self):
		rf=requests.get('https://graph.facebook.com/me/friends?access_token='+str(open('token.txt').read().split('\n')[0]))
		js=beban(rf.text)
		for xx in js['data']:
			self.kiko.append(xx['name']+" -> "+"\033[1;37m\033[31m"+xx['id']+"\033[0m")
			self.teman.append(xx['id'])
		tokens=ambil('https://graph.facebook.com/me?access_token='+str(open('token.txt').read().split('\n')[0]))
		a=beban(tokens.text)
		print(blackEngineer_Banner)
		printf("red/*		++ whitebold/*Welcome green/*"+a['name']+"red/* ++white/*\n")
		
		pilihan=raw_input('choice: ')
		if    "1" in pilihan:
			postid()
		elif "2" in pilihan:
			min()
		elif "3" in pilihan:
			self.comment()
		elif "4" in pilihan:
			self.delFriends()
		elif "5" in pilihan:
			try:
				self.searchFriends()
			except:
				raise self.searchFriends()
		elif "6" in pilihan:
			self.get_id_statusFriends()
		elif "7" in pilihan:
			self.update()
		elif "8" in pilihan:
			self.info()
		elif "9" in pilihan:
			keluar("[!] Keluar!")
		else:
			printf('salah/*wrong input.')
			perintah('clear')
			self.menu()
	# Delete Friends Module
	def info(self):
		print W+"""
------------------------------------------------------
* github: https://github.com/LOoLzeC                 *
* pastebin: https://pastebin.com/u/LOoLzeC           *
*                                                    *
* report bug on my other sosmed:                     *
*	# https://facebook.com/achmadluthfi.hadi.3   *
*	# https://instagram.com/reyy05_              *
------------------------------------------------------
		"""
	def delFriends(self):
		try:
			self.confirmation()
			self.rmv()
		except:
			try:
				e=raw_input(N+'- exit? y/n: ')
				if "y" in e:
					keluar()
				else:
					try:
						ds=raw_input('- [m]enu or [a]gain? m/a: ')
						if "m" in ds.lower():
							self.menu()
							self.fr=[]
						elif "a" in ds.lower():
							self.fr=[]
							self.delFriends()
						else:
							keluar("[!] Keluar!")
					except:
						keluar()
			except:
				keluar()
			
	def confirmation(self):
		komen=W+"""
--------------------------------------------------
* input of countries that don't want to delete   *
* we remove the friend from another              *
* country, use commas (,) to separate            *
* the string, or use a semicolon (;)             *
* to separate the string.                        *
* for example: algeria,indonesia,Japanese;       *
--------------------------------------------------
			"""
		print komen
		self.country=raw_input("- input countries u don't want to delete: ").replace(' ','').replace(',',';').split(';')
	def rmv(self):
		# Call self.teman
		self.tmn=[]
		self.fr=[]
		for x in self.teman:
			self.nama= ambil("https://graph.facebook.com/"+x+"?access_token="+str(open('token.txt').read().split('\n')[0]))
			self.s=beban(self.nama.text)
			try:
				self.sock= self.s['hometown']['name']
				for xx in self.country:
					if xx.lower() in self.sock.lower():
						pass
					else:
						self.s=beban(self.nama.text)
						self.sock= self.s['hometown']['name']
						mulai= put('https://graph.facebook.com/me/friends/'+x+'?method=delete&access_token='+str(open('token.txt').read().split('\n')[0])).text
						b= ambil('https://graph.facebook.com/me/friends?access_token='+str(open('token.txt').read().split('\n')[0])).text
						jsjs=beban(b)
						for xd in jsjs['data']:
							self.fr.append(xd['id'])
						self.tmn.append(self.sock.lower())
				if len(self.tmn) !=0:
					print ""+G+"["+O+self.s["name"]+G+"]"+W+" -> "+G+"["+O+self.sock.lower()+G+"]"+W+R+" delete"
					printf("salah/* Friends: "+str(len(self.fr)))
					self.tmn=[]
					self.fr=[]
				else:
					print ""+G+"["+O+self.s["name"]+G+"]"+W+" -> "+G+"["+O+self.sock.lower()+G+"]"
			except Exception as f:
				pass
	# Get Friends Post Id
	def get_id_statusFriends(self):
		try:
			posts()
		except:
			r=raw_input('[?] exit? y/n: ')
			if "y" in r.lower():
				keluar()
			else:
				massComments()
	# Comments Spammers Module
	def comment(self):
		try:
			massComments()
		except:
			r=raw_input('[?] exit? y/n: ')
			if "y" in r.lower():
				keluar()
			else:
				massComments()
	# Search Friends Module
	def searchFriends(self):
		teman=raw_input('+ query: ')
		for x in self.kiko:
			if not teman in x.lower():
				pass
			else:
				self.lol.append(x)
				try:
					print "[result]:",x.lower().replace(teman,""+"\033[0m"+"\033[1;37m\033[31m"+""+teman+""+"\033[0m"+"")
				except:pass
		if len(self.lol) ==0:
			printf('salah/* No Results search for: '+teman)
			raw_input("\033[1;32m*\033[0mpress enter to menu ...")
			perintah('clear')
			self.menu()
		else:
			self.lol=[]
			raw_input("\033[1;32m*\033[0mpress enter to menu ...")
			perintah('clear')
			self.menu()
	# Update Module	
	def update(self):
		apus('raw/tools/lives/lives.txt')
		self.lives()
	# Check if access token not found
	def cek(self):
		try:
			o=open('token.txt').read().split('\n')[0]
			oo=open('token.txt').readlines()
			if len(oo) == 0:
				apus('token.txt')
				banner()
				raw_input('\033[1;32m*\033[0mpress enter to generate access token ...')
				access_token()
			else:
				self.menu()
		except Exception as f:
			banner()
			raw_input('\033[1;32m*\033[0mpress enter to generate access token ...')
			access_token()
if __name__ == "__main__":
	try:
		main()
	except Exception as f:
		printf("salah/* ERROR: "+str(f))
		printf("[!] Keluar!")
		keluar()