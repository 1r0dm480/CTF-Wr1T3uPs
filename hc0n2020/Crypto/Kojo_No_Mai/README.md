## Description
* **Name:** [Kojo_No_Mai](https://ctf.h-c0n.com/challenges#Kojo%20No%20Mai)
* **Points:** 200
* **Tag:** Crypto
* **Team:** [Gh0st in th3 Cloud H3ll](https://ctf.h-c0n.com/teams/46) Note: *Thanks to Sedekt (aka E4gl3) && lilivx*

<p align="center">
<img src="hc0n2020quals-Challenge-Crypto-Kojo_No_Mai.png"/>
</p>

## Tools
* Firefox 68.2.0esr https://www.mozilla.org/en-US/firefox/68.2.0/releasenotes/
* RSA attack tool https://github.com/Ganapati/RsaCtfTool
* OpenSSL https://github.com/openssl/openssl/releases/tag/OpenSSL_1_1_1d

## Writeup
Download the file called kokonamai.txt (xxx) with a ASCII text. We detect an encrypted text splitted into smaller pieces and then encrypted with weak RSA.[Hybryd Encryption](https://stackoverflow.com/questions/13356656/split-data-to-smaller-pieces-then-encrypt-with-rsa)
```bash
https://ctf.h-c0n.com/challenges#Kojo%20No%20Mai
oot@1v4n:~/CTF/hc0n2020/Crypto/Kojo_No_Mai# wget https://ctf.h-c0n.com/files/7f923f1c0fc504b79b0a41f91f590a49/kojonomai.txt?token=eyJ1c2VyX2lkIjoxMjEsInRlYW1faWQiOjQ2LCJmaWxlX2lkIjo1fQ.Xhl3Hg.z74IbdjUOPkNijCuSg81uEeS9as
--2020-01-11 08:21:32--  https://ctf.h-c0n.com/files/7f923f1c0fc504b79b0a41f91f590a49/kojonomai.txt?token=eyJ1c2VyX2lkIjoxMjEsInRlYW1faWQiOjQ2LCJmaWxlX2lkIjo1fQ.Xhl3Hg.z74IbdjUOPkNijCuSg81uEeS9as
Resolviendo ctf.h-c0n.com (ctf.h-c0n.com)... 82.98.177.116
Conectando con ctf.h-c0n.com (ctf.h-c0n.com)[82.98.177.116]:443... conectado.
Petición HTTP enviada, esperando respuesta... 200 OK
Longitud: 318 [text/plain]
Grabando a: “kojonomai.txt?token=eyJ1c2VyX2lkIjoxMjEsInRlYW1faWQiOjQ2LCJmaWxlX2lkIjo1fQ.Xhl3Hg.z74IbdjUOPkNijCuSg81uEeS9as”

kojonomai.txt?token 100%[===================>]     318  --.-KB/s    en 0s      

2020-01-11 08:21:33 (4,70 MB/s) - “kojonomai.txt?token=eyJ1c2VyX2lkIjoxMjEsInRlYW1faWQiOjQ2LCJmaWxlX2lkIjo1fQ.Xhl3Hg.z74IbdjUOPkNijCuSg81uEeS9as” guardado [318/318]

root@1v4n:~/CTF/hc0n2020/Crypto/Kojo_No_Mai# mv kojonomai.txt\?token\=eyJ1c2VyX2lkIjoxMjEsInRlYW1faWQiOjQ2LCJmaWxlX2lkIjo1fQ.Xhl3Hg.z74IbdjUOPkNijCuSg81uEeS9as  kokonamai.txt

root@1v4n:~/CTF/hc0n2020/Crypto/Kojo_No_Mai# file kokonamai.txt
kokonamai.txt: ASCII text
root@1v4n:~/CTF/hc0n2020/Crypto/Kojo_No_Mai# cat kokonamai.txt
-----BEGIN PUBLIC KEY-----
MCwwDQYJKoZIhvcNAQEBBQADGwAwGAIRAOSpZLB7VXE7iZA72YTS85UCAwEAAQ==
-----END PUBLIC KEY-----

XnZvSmNqZqz+N5LL+ec6XA==
k4TD9AHouSlxdn97PXfmOg==
FhHp7W1orCt78mlz5PNGBQ==
a5FPpzeDX29qOriH2kS64A==
XCWOYhWFC6v3wa3qM58v5g==
qlLYhsaMWbOvCXddqsQ/pA==
i1jClSfyTf8XLiT57Su6IQ==
DZbTy4vMKW0WqjrD7CspMg==
```
We verify that the public RSA public key is well formed. (https://security.stackexchange.com/questions/69192/how-to-check-a-public-rsa-key-file-is-well-formed)

```bash
root@1v4n:~/CTF/hc0n2020/Crypto/Kojo_No_Mai# openssl rsa -inform PEM -text -noout -pubin < key.pub
RSA Public-Key: (128 bit)
Modulus:
    00:e4:a9:64:b0:7b:55:71:3b:89:90:3b:d9:84:d2:
    f3:95
Exponent: 65537 (0x10001)
```
We start attacking the weak RSA encryption key, obtaining the private key.

```bash
root@1v4n:~/Crypto/RsaCtfTool# ./RsaCtfTool.py --publickey ~/CTF/hc0n2020/Crypto/Kojo_No_Mai/key.pub --verbose --private
[*] Performing hastads attack.
[*] Performing prime_n attack.
[*] Performing factordb attack.
-----BEGIN RSA PRIVATE KEY-----
MGQCAQACEQDkqWSwe1VxO4mQO9mE0vOVAgMBAAECEQDdv/jJvZHK0CDDfXs8vASB
AgkA6nTNPNoXOLkCCQD5rEi0wt8rvQIJANrmxP0MzuOZAgkAy4+dA8vyWt0CCA7U
J3WkWZCx
-----END RSA PRIVATE KEY-----
root@1v4n:~/CTF/hc0n2020/Crypto/Kojo_No_Mai# cat private.pem
-----BEGIN RSA PRIVATE KEY-----
MGQCAQACEQDkqWSwe1VxO4mQO9mE0vOVAgMBAAECEQDdv/jJvZHK0CDDfXs8vASB
AgkA6nTNPNoXOLkCCQD5rEi0wt8rvQIJANrmxP0MzuOZAgkAy4+dA8vyWt0CCA7U
J3WkWZCx
-----END RSA PRIVATE KEY-----
root@1v4n:~/CTF/hc0n2020/Crypto/Kojo_No_Mai# openssl rsa -inform PEM -text -noout < private.pem
RSA Private-Key: (128 bit, 2 primes)
modulus:
    00:e4:a9:64:b0:7b:55:71:3b:89:90:3b:d9:84:d2:
    f3:95
publicExponent: 65537 (0x10001)
privateExponent:
    00:dd:bf:f8:c9:bd:91:ca:d0:20:c3:7d:7b:3c:bc:
    04:81
prime1: 16894353763414259897 (0xea74cd3cda1738b9)
prime2: 17990834552639007677 (0xf9ac48b4c2df2bbd)
exponent1: 15773511336032396185 (0xdae6c4fd0ccee399)
exponent2: 14668115151001115357 (0xcb8f9d03cbf25add)
coefficient: 1068522397815640241 (0xed42775a45990b1)

```
We separate each line encrypted and coded in base64 into separate files. To decipher our splitted flag

```bash
root@1v4n:~/CTF/hc0n2020/Crypto/Kojo_No_Mai_GRANTED# cat kokonamai.txt | sed 1,4d >> cipher.enc
root@1v4n:~/CTF/hc0n2020/Crypto/Kojo_No_Mai_GRANTED# cat cipher.enc
XnZvSmNqZqz+N5LL+ec6XA==
k4TD9AHouSlxdn97PXfmOg==
FhHp7W1orCt78mlz5PNGBQ==
a5FPpzeDX29qOriH2kS64A==
XCWOYhWFC6v3wa3qM58v5g==
qlLYhsaMWbOvCXddqsQ/pA==
i1jClSfyTf8XLiT57Su6IQ==
DZbTy4vMKW0WqjrD7CspMg==
root@1v4n:~/CTF/hc0n2020/Crypto/Kojo_No_Mai_GRANTED# cat cipher.enc | base64 -d | xxd
00000000: 5e76 6f4a 636a 66ac fe37 92cb f9e7 3a5c  ^voJcjf..7....:\
00000010: 9384 c3f4 01e8 b929 7176 7f7b 3d77 e63a  .......)qv.{=w.:
00000020: 1611 e9ed 6d68 ac2b 7bf2 6973 e4f3 4605  ....mh.+{.is..F.
00000030: 6b91 4fa7 3783 5f6f 6a3a b887 da44 bae0  k.O.7._oj:...D..
00000040: 5c25 8e62 1585 0bab f7c1 adea 339f 2fe6  \%.b........3./.
00000050: aa52 d886 c68c 59b3 af09 775d aac4 3fa4  .R....Y...w]..?.
00000060: 8b58 c295 27f2 4dff 172e 24f9 ed2b ba21  .X..'.M...$..+.!
00000070: 0d96 d3cb 8bcc 296d 16aa 3ac3 ec2b 2932  ......)m..:..+)2
00000080: 5e76 6f4a 636a 66ac fe37 92cb f9e7 3a5c  ^voJcjf..7....:\
00000090: 9384 c3f4 01e8 b929 7176 7f7b 3d77 e63a  .......)qv.{=w.:
000000a0: 1611 e9ed 6d68 ac2b 7bf2 6973 e4f3 4605  ....mh.+{.is..F.
000000b0: 6b91 4fa7 3783 5f6f 6a3a b887 da44 bae0  k.O.7._oj:...D..
000000c0: 5c25 8e62 1585 0bab f7c1 adea 339f 2fe6  \%.b........3./.
000000d0: aa52 d886 c68c 59b3 af09 775d aac4 3fa4  .R....Y...w]..?.
000000e0: 8b58 c295 27f2 4dff 172e 24f9 ed2b ba21  .X..'.M...$..+.!
000000f0: 0d96 d3cb 8bcc 296d 16aa 3ac3 ec2b 2932  ......)m..:..+)2
root@1v4n:~/CTF/hc0n2020/Crypto/Kojo_No_Mai_GRANTED# grep "XnZ" cipher.enc | base64 -d > enc1.raw
root@1v4n:~/CTF/hc0n2020/Crypto/Kojo_No_Mai_GRANTED# grep "k4T" cipher.enc | base64 -d > enc2.raw
root@1v4n:~/CTF/hc0n2020/Crypto/Kojo_No_Mai_GRANTED# grep "FhH" cipher.enc | base64 -d > enc3.raw
root@1v4n:~/CTF/hc0n2020/Crypto/Kojo_No_Mai_GRANTED# grep "a5F" cipher.enc | base64 -d > enc4.raw
root@1v4n:~/CTF/hc0n2020/Crypto/Kojo_No_Mai_GRANTED# grep "XCW" cipher.enc | base64 -d > enc5.raw
root@1v4n:~/CTF/hc0n2020/Crypto/Kojo_No_Mai_GRANTED# grep "qlL" cipher.enc | base64 -d > enc6.raw
root@1v4n:~/CTF/hc0n2020/Crypto/Kojo_No_Mai_GRANTED# grep "i1j" cipher.enc | base64 -d > enc7.raw
root@1v4n:~/CTF/hc0n2020/Crypto/Kojo_No_Mai_GRANTED# grep "DZb" cipher.enc | base64 -d > enc8.raw
root@1v4n:~/CTF/hc0n2020/Crypto/Kojo_No_Mai# openssl rsautl -decrypt -inkey private.pem -in enc1.raw -hexdump
0000 - 48 2d 63 30 6e                                    H-c0n
root@1v4n:~/CTF/hc0n2020/Crypto/Kojo_No_Mai_GRANTED# openssl rsautl -decrypt -inkey private.pem -in enc3.raw -hexdump
0000 - 36 63 32 65 62                                    6c2eb
root@1v4n:~/CTF/hc0n2020/Crypto/Kojo_No_Mai_GRANTED# openssl rsautl -decrypt -inkey private.pem -in enc4.raw -hexdump
0000 - 34 39 61 32 66                                    49a2f
root@1v4n:~/CTF/hc0n2020/Crypto/Kojo_No_Mai_GRANTED# openssl rsautl -decrypt -inkey private.pem -in enc5.raw -hexdump
0000 - 34 32 37 65 35                                    427e5
root@1v4n:~/CTF/hc0n2020/Crypto/Kojo_No_Mai_GRANTED# openssl rsautl -decrypt -inkey private.pem -in enc6.raw -hexdump
0000 - 37 63 37 31 35                                    7c715
root@1v4n:~/CTF/hc0n2020/Crypto/Kojo_No_Mai_GRANTED# openssl rsautl -decrypt -inkey private.pem -in enc7.raw -hexdump
0000 - 62 64 61 38 33                                    bda83
root@1v4n:~/CTF/hc0n2020/Crypto/Kojo_No_Mai_GRANTED# openssl rsautl -decrypt -inkey private.pem -in enc8.raw -hexdump
0000 - 39 65 36 7d                                       9e6}
root@1v4n:~/CTF/hc0n2020/Crypto/Kojo_No_Mai_GRANTED# buster -s 1aa36c2eb49a2f427e57c715bda839e6
_  _ ____ ____ _  _    ___  _  _ ____ ___ ____ ____
|__| |__| [__  |__|    |__] |  | [__   |  |___ |__/
|  | |  | ___] |  |    |__] |__| ___]  |  |___ |  \  v3.0

[!] Hash function : MD5
pequenio

```

### Flag

`H-c0n{1aa36c2eb49a2f427e57c715bda839e6}`

<p align="center">
<img src="hc0n2020quals-Challenge-Crypto-Kojo_No_Mai.gif"/>
</p>
