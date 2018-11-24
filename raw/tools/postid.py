#!/usr/bin/env python
#-*-coding:utf-8-*-
# get your post id modules
# BlackEngineer By Deray
# Report bug on my other sosmed
# https://facebook.com/achmadluthfi.hadi.3
# https://instagram.com/reyy05_

from requests import get,post
import json
from raw.tools.autolike import *
from sys import exit as keluar
import cacheclean
cacheclean.cache()
class postid():
	def __init__(self,*args,**kwargs):
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
	def main(self):
		tokenjs={"token":open('token.txt').read().split('\n')[0]}
		try:
			self.me=json.loads(get('https://graph.facebook.com/v3.0/me?fields=feed.limit(9999999)&access_token='+tokenjs['token']).text)
		except Exception as f:
			print f
			cacheclean.cache()
			keluar()
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
					try:
						auto()
					except:
						cacheclean.cache()
						printf("\n[!] Keluar!")
						keluar()
		except Exception as f:
			cacheclean.cache()
			printf("salah/* ERROR: "+str(f))
			printf("[!] Keluar!")
			keluar()