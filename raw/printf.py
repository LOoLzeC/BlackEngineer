#!/usr/bin/env python
#-*-coding:utf-8-*-
# printf modules
# BlackEngineer By Deray
# Report bug on my other sosmed
# https://facebook.com/achmadluthfi.hadi.3
# https://instagram.com/reyy05_

import cacheclean
cacheclean.cache()
def printf(deray):
	warna={'green':'\033[1;32m','white':'\033[0m','notice':'\033[34m[*]\033[0m','salah':'\033[1;37m\033[31m[-]\033[0m','whitebold':'\033[1;37m','red':'\033[1;37m\033[31m','blue':'\033[34m','cyan':'\033[33m'}
	print deray.replace('notice/*',warna['notice']).replace('salah/*',warna['salah']).replace('green/*',warna['green']).replace('white/*',warna['white']).replace('whitebold/*',warna['whitebold']).replace('red/*',warna['red']).replace('blue/*',warna['blue']).replace('cyan/*',warna['cyan'])
