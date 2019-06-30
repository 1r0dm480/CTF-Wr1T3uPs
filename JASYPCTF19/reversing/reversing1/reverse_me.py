#!/usr/bin/env python

import sys
import base64

print3 = str(sys.argv[1])
print5 = "3033324534443730453344304237367d" 
print1 = "4a415359507b43453646333639463543304635364333"
print2 = "Password incorrecta"
print10 = "qwerty"

def a():
	d = 3
	if len(print3)%d==2:
		return base64.b64decode(print3[::-1])

def b():
	d = 3
	e = 5
	if len(print3)%d!=0:
		return (len(print3)%e)*12


print1 = print1+str(b())

print6 = print1+print5

print4 = print6.decode("hex")

if a() == print10:
	print(print4)
else:
	print(print2)
