## Description
* **Name:** [Rev03](http://ctf.securityhighschool.es/challenges?category=reversing)
* **Tag:** Reversing
<p align="center">
<img src="shs2k19ctf.png"/>
</p>

## Tools
* Firefox Version 60.8.0 https://www.mozilla.org/en-US/firefox/60.8.0/releasenotes/
* GNU strings 2.31.1
* ltrace version 0.7.3. https://gitlab.com/cespedes/ltrace

## Writeup
We find a [ELF](https://en.wikipedia.org/wiki/Executable_and_Linkable_Format) (692fe3db80f4e24b64c7fbc4f599090b) called REV01 .

```bash
root@1v4n:~/CTF/SHS2K19/rev/rev03_GRANTED# md5sum REV03
692fe3db80f4e24b64c7fbc4f599090b  REV03
root@1v4n:~/CTF/SHS2K19/rev/rev03_GRANTED# file REV03
REV03: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 3.2.0, BuildID[sha1]=2144fe0926dbfc8fa3fa221d52860490c092bd1c, not stripped
root@1v4n:~/CTF/SHS2K19/rev/rev03_GRANTED# strings REV03 |less
/lib64/ld-linux-x86-64.so.2
libc.so.6
puts
__stack_chk_fail
realloc
printf
strlen
malloc
strcat
__ctype_b_loc
__cxa_finalize
strcmp
__libc_start_main
GLIBC_2.3
GLIBC_2.4
GLIBC_2.2.5
_ITM_deregisterTMCloneTable
__gmon_start__
_ITM_registerTMCloneTable
c2hzf
sxOXs0X
2wxdHRsZH
V9tMHIzXH
ZjFjdWx
shs2k19{H
f4k3_fl4H
dH3<%(
dH34%(
AWAVI
AUATL
[]A\A]A^A_
ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/You get the flag!
Mmm, nope
Faltan argumentos...
ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/
...
```
We did not find a possible chain that will confirm that it is our flag. Check with ltrace that the ELF contains the strcmp function (Compare two strings)

```
root@1v4n:~/CTF/SHS2K19/rev/rev03_GRANTED# ltrace ./REV03 AAAA
...
realloc(0x556eac09e260, 32)                                                                 = 0x556eac09e260
strcmp("AAAA", "shs2k19{4_l1ttle_m0r3_d1f1cult}")                                           = -50
printf("Mmm, nope")                                                                         = 9
Mmm, nope+++ exited (status 0) +++
root@1v4n:~/CTF/SHS2K19/rev/rev03_GRANTED# ./REV03 shs2k19{4_l1ttle_m0r3_d1f1cult}
You get the flag!
```
So our solver would fit us

```bash
root@1v4n:~/CTF/SHS2K19/forense/rev03# nano get_flag.sh
#! /bin/bash

ltrace -o output ./REV03 AAAA && cat output | grep "shs2k19{.*" | awk -F'"' '{print $4}' > flag
root@1v4n:~/CTF/SHS2K19/rev/rev03_GRANTED# nano get_flag.sh
root@1v4n:~/CTF/SHS2K19/rev/rev03_GRANTED# chmod +x get_flag.sh
root@1v4n:~/CTF/SHS2K19/rev/rev03_GRANTED# ./get_flag.sh
Mmm, noperoot@1v4n:~/CTF/SHS2K19/rev/rev03_GRANTED# cat flag
shs2k19{4_l1ttle_m0r3_d1f1cult}
```


### Flag
`shs2k19{4_l1ttle_m0r3_d1f1cult}`
