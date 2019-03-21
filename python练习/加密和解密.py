"""
对称加密 - DES/aES
非对称加密：RSA
PyCrypto
"""
import hashlib
from Crypto.Cipher import AES
from Crypto.PublicKey import RSA

from Crypto import Random
key = hashlib.md5('www'.encode()).hexdigest()
iv = Random.new().read(AES.block_size)
# print(iv)

def aes(message,key):
	cipher = AES.new(key, AES.MODE_CFB, iv)
	return cipher.decrypt(message)

def aes1(message,key):
	cipher = AES.new(key, AES.MODE_CFB, iv)
	return cipher.encrypt(message)

def main():
	ch1 = 'hellow'
	s1 = aes1(ch1,key)
	print('----------------------')
	print(s1)
	s2 = aes(s1,key)
	print(s2.decode('utf-8'))

def fj():
	key_p = RSA.generate(1024)
	p_k = RSA.importKey(key_p.publickey().exportKey())
	pr_k = RSA.importKey(key_p.exportKey())
	m = 'hellow'
	d = p_k.encrypt(m.encode(),None)
	print(d)
	j = pr_k.decrypt(d)
	print(j)
if __name__ == '__main__':

	fj()

