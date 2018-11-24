#!/usr/bin/env python
#-*-coding:utf-8-*-
# requirements modules
# BlackEngineer By Deray
# Report bug on my other sosmed
# https://facebook.com/achmadluthfi.hadi.3
# https://instagram.com/reyy05_

from raw.printf import *
from sys import exit as keluar
from os import system as perintah
import cacheclean
cacheclean.cache()
def penginstalan():
	printf("salah/* requests module is not installed!")
	ask=raw_input('\033[1;37m\033[31m[-]\033[0m install? [y/n]: ')
	if ask.lower() == "y":
		perintah('pip2 install requests;pip install requests')
		perintah('clear')
	else:
		keluar()