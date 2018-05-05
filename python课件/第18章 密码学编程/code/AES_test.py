import string
import random
from Crypto.Cipher import AES

def keyGenerater(length):
    '''生成指定长度的秘钥'''
    if length not in (16, 24, 32):
        return None
    x = string.ascii_letters+string.digits
    return ''.join([random.choice(x) for i in range(length)]) 

def encryptor_decryptor(key, mode):
    return AES.new(key, mode, b'0000000000000000')

#使用指定密钥和模式对给定信息进行加密
def AESencrypt(key, mode, text):
    encryptor = encryptor_decryptor(key, mode)
    return encryptor.encrypt(text)

#使用指定密钥和模式对给定信息进行解密
def AESdecrypt(key, mode, text):
    decryptor = encryptor_decryptor(key, mode)
    return decryptor.decrypt(text)

if __name__ == '__main__':
    text = '山东省烟台市 Python3.5 is excellent.'
    key = keyGenerater(16)
    #随机选择AES的模式
    mode = random.choice((AES.MODE_CBC, AES.MODE_CFB, AES.MODE_ECB, AES.MODE_OFB))
    if not key:
        print('Something is wrong.')
    else:
        print('key:', key)
        print('mode:', mode)
        print('Before encryption:', text)
        #明文必须以字节串形式，且长度为16的倍数
        text_encoded = text.encode()
        text_length = len(text_encoded)
        padding_length = 16 - text_length%16
        text_encoded = text_encoded + b'0'*padding_length
        
        text_encrypted = AESencrypt(key, mode, text_encoded)
        print('After encryption:', text_encrypted)
        text_decrypted =AESdecrypt(key, mode, text_encrypted)
        print('After decryption:', text_decrypted.decode()[:-padding_length])
