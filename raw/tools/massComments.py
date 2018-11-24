#!/usr/bin/env python
#-*-coding:utf-8-*-
# Module Mass Comments
# BlackEngineer By Deray
# Report bug on my other sosmed
# https://facebook.com/achmadluthfi.hadi.3
# https://instagram.com/reyy05_

from raw.printf import *
from sys import exit as keluar
import random
import cacheclean
from requests import get as ambil
from requests import post as put
from json import loads as beban
from time import sleep as tidur
cacheclean.cache()
class massComments():
	def __init__(self,*args):
		self.reqToken()
		self.reqID()
		self.reqPesan()
		self.main()
	def reqToken(self):
		self.token=raw_input('+ token list: ')
		try:
			self.openToken=open(self.token).readlines()
		except Exception as f:
			printf('salah/* '+str(f))
			self.reqToken()
	def reqPesan(self):
		try:
			printf('notice/* type <space> for new lines.')
			self.pesan=raw_input('+ message: ').replace('<space>','\n')
			printf('notice/* starting jobs ...')
			printf('notice/* press CTRL+C To stopping loop ...')
		except:
			raise self.reqPesan()
	def reqID(self):
		try:
			self.reqIDS=raw_input('+ post id: ')
		except:
			raise self.reqIDS()
	def main(self):
		for x in self.openToken:
			xx=x.split('\n')[0]
			payload = {'access_token' :xx, 'message' : self.pesan}
			rr=put("https://graph.facebook.com/"+self.reqIDS+"/comments",data=payload)
			if "error" in rr.text.lower():
				js=beban(rr.text)
				printf("red/*-white/* Error msg: "+js['error']['message'][0:20])
			else:
				printf("green/*++ white/*spammers send successfully.")
				tidur(00.01)
		self.main()