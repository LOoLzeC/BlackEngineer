#!/usr/bin/env python
#-*-coding:utf-8-*-
# auto like modules
# BlackEngineer By Deray
# Report bug on my other sosmed
# https://facebook.com/achmadluthfi.hadi.3
# https://instagram.com/reyy05_

from requests import get,post
from json import loads
from raw.printf import *
import re
import base64
from sys import exit as keluar
import cacheclean
cacheclean.cache()
class auto():
	def __init__(self,*args):
		self.id()
		self.tk()
	def tk(self):
		try:
			o=raw_input('token list : ')
			self.op=open(o).readlines()
			self.main()
			
		except Exception as f:
			printf("salah/* "+str(f))
			self.tk()
	def id(self):
		self.wall_id=raw_input('\npaste id here : ')
		self.tk()
	def main(self):
		printf("""
	red/*** white/*SELECT REACTION MENU red/***
  red/*1blue/*)white/* ANGRY
  red/*2blue/*)white/* LOVE
  red/*3blue/*)white/* SAD
  red/*4blue/*)white/* WOW
  red/*5blue/*)white/* HAHA
  red/*6blue/*)white/* LIKE
		""")
		tipe=raw_input('* select: ').replace('1','ANGRY').replace('2','LOVE').replace('3','SAD').replace('4','WOW').replace('5','HAHA').replace('6','LIKE')
		
		for tken in self.op:
			x=tken.split('\n')[0]
			sundul={'access_token':x,'type':tipe}
			rr=post("https://graph.facebook.com/"+self.wall_id+"/reactions",data=sundul)
			if "error" in rr.text.lower():
				rs=loads(rr.text)
				printf("salah/* Error msg:white/* "+rs['error']['message'][0:40]+" ..")
			else:
				printf("green/*++ Suksess liked ...white/*")
		printf("notice/* job finished.")
		cacheclean.cache()
		keluar()
