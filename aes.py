#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from utils import *
import random

class AES:
    def __init__(self, keylen, key=None):
        '''
        Input:
        - `keylen`: int type, the key length, with value 128, 192 or 256.
        - `key`: int type, the `keylen`-bit cipher key, encoded in big-endian;
          or None, generate the key randomly (None by default).

        Store the `key`, which is a cipher key provided by the user, as an
        attribute. If `key` is None, generate the cipher key randomly according
        to the length `keylen` with `random.randrange()`.

        Raise `AESInputError` if and only if either
        - `keylen` is not an int, or is a value other than 128, 192 and 256, or
        - `key` is not an int, is negative, or cannot be represented by
          `keylen` bits.
        '''
        
        "*** YOUR CODE HERE ***"
        raise InterruptedError

    def enc(self, msg):
        '''
        Input: `msg`: int type, the 128-bit plaintext to be encrypted,
        encoded in big-endian.
        Output: int type, the 128-bit ciphertext encoded in big-endian.

        Encrypt the plaintext `msg` with AES algorithm, given the key provided
        or generated before. Return the ciphertext.

        Raise `AESInputError` if and only if `msg` is not an int, is negative,
        or cannot be represented by 128 bits.
        '''
        
        "*** YOUR CODE HERE ***"
        raise InterruptedError


    def dec(self, ciph):
        '''
        Input: `msg`: int type, the 128-bit ciphertext to be decrypted,
        encoded in big-endian.
        Output: int type, the 128-bit plaintext encoded in big-endian.

        Decrypt the plaintext `ciph` with AES algorithm, given the key provided
        or generated before. Return the plaintext.

        Raise `AESInputError` if and only if `ciph` is not an int, is negative,
        or cannot be represented by 128 bits.
        '''
        
        "*** YOUR CODE HERE ***"
        raise InterruptedError

    def getkey(self):
        ''' Output: int type, the cipher key encoded in big-endian. '''
        
        "*** YOUR CODE HERE ***"
        raise InterruptedError

class AESCBC(AES):
    def encfile(self, infile, outfile, iv=0, pad=True):
        '''
        Input:
        - `infile`: str type, the pathname of input file (plaintext).
        - `outfile`: str type, the pathname of output file (ciphertext).
        - `iv`: int type, the 128-bit initialization vector (IV) encoded in
          big-endian (0 by default).
        - `pad`: bool type, pad the file using PKCS#7 if True (True by
          default).

        Read the plaintext from file `infile`. Encrypt with AES-128/192/256-CBC
        and use `iv` as the initialization vector.
        If `pad` is True, pad the file using PKCS#7.
        If `pad` is False,
        - If the input is a multiple of 128 bits (16 bytes), don't pad.
        - Otherwise, raise `AESPaddingError`.
        Write the ciphertext to file `outfile`.
        It is NOT required to check the existence of `infile` or I/O errors.

        Raise `AESInputError` if and only if either
        - `infile` is not a str, or
        - `outfile` is not a str, or
        - `iv` is not an int, is negative, or cannot be represented by
          128 bits, or
        - `pad` is not a bool.

        Raise `AESPaddingError` if and only if `pad` is False, but the input is
        not a multiple of 128 bits (16 bytes).
        '''
        
        "*** YOUR CODE HERE ***"

        with open(infile, 'rb') as infi:
            inbytes = infi.read()

        "*** YOUR CODE HERE ***"

        with open(outfile, 'wb') as outfi:
            outfi.write(outbytes)
        
        raise InterruptedError

    def decfile(self, infile, outfile, iv=0, pad=True):
        '''
        - `infile`: str type, the pathname of input file (ciphertext).
        - `outfile`: str type, the pathname of output file (plaintext).
        - `iv`: int type, the 128-bit initialization vector (IV) encoded in
          big-endian (0 by default).
        - `pad`: bool type, remove the padding according to PKCS#7 if True
          (True by default).

        Read the ciphertext from file `infile`. Decrypt with AES-128/192/256-CBC
        and use `iv` as the initialization vector.
        If `pad` is True, remove the padding according to PKCS#7 before writing.
        Write the plaintext to file `outfile`.
        It is NOT required to check the existence of `infile` or I/O errors.

        Raise `AESInputError` if and only if either
        - `infile` is not a str, or
        - `outfile` is not a str, or
        - `iv` is not an int, is negative, or cannot be represented by
          128 bits, or
        - `pad` is not a bool.

        Raise `AESDataError` if and only if the input is not a multiple of
        128 bits.

        Raise `AESPaddingError` if and only if `pad` is True but the padding
        doesn't seem correct.
        '''

        "*** YOUR CODE HERE ***"

        with open(infile, 'rb') as infi:
            inbytes = infi.read()

        "*** YOUR CODE HERE ***"

        with open(outfile, 'wb') as outfi:
            outfi.write(outbytes)
        
        raise InterruptedError

def test():
    key = 0x2b7e151628aed2a6abf7158809cf4f3c
    msg = 0x3243f6a8885a308d313198a2e0370734
    ciph_ans = 0x3925841d02dc09fbdc118597196a0b32

    aes = AES(128, key)
    ciph = aes.enc(msg)
    assert ciph == ciph_ans
    msg2 = aes.dec(ciph)
    assert msg == msg2

def test2():
    key = 0x000102030405060708090a0b0c0d0e0f1011121314151617
    msg = 0x00112233445566778899aabbccddeeff
    ciph_ans = 0xdda97ca4864cdfe06eaf70a0ec0d7191

    aes = AES(192, key)
    ciph = aes.enc(msg)
    assert ciph == ciph_ans
    msg2 = aes.dec(ciph)
    assert msg == msg2

def test3():
    msg_file = 'file.m'
    ciph_file = 'file.c'
    msg2_file = 'file2.m'
    key = 0x2b7e151628aed2a6abf7158809cf4f3c
    msg = 0x3243f6a8885a308d313198a2e0370734face
    ciph_ans = 0x3925841d02dc09fbdc118597196a0b32f4a3358aa7c61ced508f3435fe67f854

    aes = AESCBC(128, key)
    with open(msg_file, 'wb') as f:
        f.write(msg.to_bytes(18, 'big'))

    aes.encfile(msg_file, ciph_file)
    with open(ciph_file, 'rb') as f:
        ciph = int.from_bytes(f.read(), 'big')
    assert ciph == ciph_ans

    aes.decfile(ciph_file, msg2_file)
    with open(msg2_file, 'rb') as f:
        msg2 = int.from_bytes(f.read(), 'big')
    assert msg == msg2

if __name__ == '__main__':
    test()
    test2()
    test3()