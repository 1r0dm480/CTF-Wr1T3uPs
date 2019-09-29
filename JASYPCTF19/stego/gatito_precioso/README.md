## Description
* **Name:** [Gatito Precioso](https://ctf.interferencias.tech/challenges#Gatito%20precioso)
* **Points:** 100
* **Tag:** Stego

<p align="center">
<img src="gatito.jpg"/>
</p>

## Tools
* Firefox Version 60.7.0 https://www.mozilla.org/en-US/firefox/60.7.0/releasenotes/
* GNU strings 2.31.1

## Writeup
```bash
root@1v4n:~/CTF/JASYPCTF2019/stego/gatito# file gatito.jpg
gatito.jpg: JPEG image data, JFIF standard 1.01, aspect ratio, density 1x1, segment length 16, baseline, precision 8, 1280x720, components 3
root@1v4n:~/CTF/JASYPCTF2019/stego/gatito# exiftool gatito.jpg
ExifTool Version Number         : 11.55
File Name                       : gatito.jpg
Directory                       : .
File Size                       : 51 kB
File Modification Date/Time     : 2019:04:15 20:04:11+02:00
File Access Date/Time           :
File Inode Change Date/Time     : 2019:04:26 21:04:19+02:00
File Permissions                : rw-r--r--
File Type                       : JPEG
File Type Extension             : jpg
MIME Type                       : image/jpeg
JFIF Version                    : 1.01
Resolution Unit                 : None
X Resolution                    : 1
Y Resolution                    : 1
Image Width                     : 1280
Image Height                    : 720
Encoding Process                : Baseline DCT, Huffman coding
Bits Per Sample                 : 8
Color Components                : 3
Y Cb Cr Sub Sampling            : YCbCr4:2:0 (2 2)
Image Size                      : 1280x720
Megapixels                      : 0.922
root@1v4n:~/CTF/JASYPCTF2019/stego/gatito# strings gatito.jpg | grep "JASYP{.*"
JASYP{B09D08A607FBD08BC5C5B6A0E2A3E53E}
```
### Flag

`JASYP{B09D08A607FBD08BC5C5B6A0E2A3E53E}`
