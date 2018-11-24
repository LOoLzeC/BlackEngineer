#!/usr/bin/env python
#-*-coding:utf-8-*-
# get your post id modules
# BlackEngineer By Deray
# Report bug on my other sosmed
# https://facebook.com/achmadluthfi.hadi.3
# https://instagram.com/reyy05_

from requests import get,post
import json
from BlackEngineer import *
from sys import exit as keluar
import cacheclean
from os import system as perintah
cacheclean.cache()
class posts():
	def __init__(self,*args,**kwargs):
		self.ids()
		self.statos=[]
		self.km=[]
		self.komet=[]
		self.memek=[]
		try:
			self.main()
		except Exception as f:
			print f
			cacheclean.cache()
			print('\n[!] keluar!')
			keluar()
	def ids(self):
		try:
			self.id=raw_input('+ id: ')
		except:
			raise self.ids()
		
	def main(self):
		tokenjs={"token":open('token.txt').read().split('\n')[0]}
		try:
			self.js = get("https://graph.facebook.com/v3.0/%s?fields=feed.limit(99999999)&access_token=%s"%(self.id,tokenjs['token']))
			self.nama= requests.get("https://graph.facebook.com/"+self.id+"?access_token="+tokenjs['token'])
			self.name=json.loads(self.nama.text)
			self.me=json.loads(self.js.text)
		except Exception as f:
			print "- Error in: "+str(f)
			cacheclean.cache()
			keluar()
		print "	++ \033[1;37m\033[31m"+self.name['name']+" \033[0m++\n"
		for xx in self.me['feed']['data']:
			self.memek.append(xx['id']) 
		self.stats=raw_input('+ mau ngambil berapa status? : ')
		if int(self.stats) > len(self.memek):
			printf("red/*+ white/*Gagal ngambil red/*"+str(self.stats)+"white/* id")
			printf("red/*+white/* total id terambil hanya red/*"+str(len(self.memek))+"white/*")
			self.memek=[]
			self.main()
		else:
			print
			self.meki()
	def meki(self):
		try:
			for x in self.me['feed']['data']:
				for xx in range(int(self.stats)):
						self.statos.append(x['id'])
						self.km.append(xx)
						if len(self.statos) == int(self.stats):
							break
				self.komet.append(x['id'])
				try:
					printf("green/*|ID| white/*"+x['id']+" green/*->white/* "+x['message'][0:15]+"...")
				except:
					try:
						printf("green/*|ID| white/*"+x['id']+" green/*->white/* "+x['story'][0:15]+"...")
					except:
						pass
				if len(self.komet) == int(self.stats):
					raw_input('*press enter to menu ...')
					perintah('clear')
					main()
					
		except Exception as f:
			cacheclean.cache()
			printf("salah/* ERROR: "+str(f))
			printf("[!] Keluar!")
			keluar()
