from functools import wraps
from time import sleep
from random import randint


def retry(*, times=3, max_wait=6,errors=(Exception,),handler=None):
	def decorate(func):

		@wraps(func)
		def wrapper(*args, **kwargs):
			for _ in range(times):
				try:
					return func(*args, **kwargs)
				except errors:
					sleep(randint(3,max_wait))
					if handler:
						handler(errors)

		return wrapper
	return decorate


import requests

s = requests.get('http://182.140.219.13/amobile.music.tc.qq.com/C400002cAc0m4JyZVd.m4a?guid=6105872536&vkey=10F8DAA4C86A14331447C65249F6F897CE6396DCD63C650AE179426AE11E525E46750EE2FE236EABEBD2887F9226008D433C124C8F0513ED&uin=0&fromtag=66')
con = (s.content)

with open('kk.mp3','wb') as f:
	f.write(con)