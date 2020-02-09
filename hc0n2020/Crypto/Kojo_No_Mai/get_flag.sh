#!/bin/bash
# Script
cat kokonamai.txt

echo "-----BEGIN PUBLIC KEY-----
MCwwDQYJKoZIhvcNAQEBBQADGwAwGAIRAOSpZLB7VXE7iZA72YTS85UCAwEAAQ==
-----END PUBLIC KEY-----" > pub.key
openssl rsa -inform PEM -text -noout -pubin < key.pub
git clone https://github.com/Ganapati/RsaCtfTool.git

cd RSACtfTool
./RsaCtfTool.py --publickey ~/CTF/hc0n2020/Crypto/Kojo_No_Mai/key.pub --verbose --private

echo "-----BEGIN RSA PRIVATE KEY-----
MGQCAQACEQDkqWSwe1VxO4mQO9mE0vOVAgMBAAECEQDdv/jJvZHK0CDDfXs8vASB
AgkA6nTNPNoXOLkCCQD5rEi0wt8rvQIJANrmxP0MzuOZAgkAy4+dA8vyWt0CCA7U
J3WkWZCx
-----END RSA PRIVATE KEY-----" > private.pem
openssl rsa -inform PEM -text -noout < private.pem

echo "XnZvSmNqZqz+N5LL+ec6XA==" > cipher1.enc
echo "k4TD9AHouSlxdn97PXfmOg==" > cipher2.enc
echo "FhHp7W1orCt78mlz5PNGBQ==" > cipher3.enc
echo "a5FPpzeDX29qOriH2kS64A==" > cipher4.enc
echo "XCWOYhWFC6v3wa3qM58v5g==" > cipher5.enc
echo "qlLYhsaMWbOvCXddqsQ/pA==" > cipher6.enc
echo "i1jClSfyTf8XLiT57Su6IQ==" > cipher7.enc
echo "DZbTy4vMKW0WqjrD7CspMg==" > cipher8.enc

cat cipher.enc | base64 -d | xxd
cat cipher1.enc |base64 -d > enc1.raw
cat cipher2.enc |base64 -d > enc2.raw
cat cipher3.enc |base64 -d > enc3.raw
cat cipher4.enc |base64 -d > enc4.raw
cat cipher5.enc |base64 -d > enc5.raw
cat cipher6.enc |base64 -d > enc6.raw
cat cipher7.enc |base64 -d > enc7.raw
cat cipher8.enc |base64 -d > enc8.raw

openssl rsautl -decrypt -inkey private.pem -in enc1.raw -hexdump
openssl rsautl -decrypt -inkey private.pem -in enc2.raw -hexdump
openssl rsautl -decrypt -inkey private.pem -in enc3.raw -hexdump
openssl rsautl -decrypt -inkey private.pem -in enc4.raw -hexdump
openssl rsautl -decrypt -inkey private.pem -in enc5.raw -hexdump
openssl rsautl -decrypt -inkey private.pem -in enc6.raw -hexdump
openssl rsautl -decrypt -inkey private.pem -in enc7.raw -hexdump
openssl rsautl -decrypt -inkey private.pem -in enc8.raw -hexdump

buster -s 1aa36c2eb49a2f427e57c715bda839e6

printf 'The flag is >_ H-c0n{1aa36c2eb49a2f427e57c715bda839e6}'
