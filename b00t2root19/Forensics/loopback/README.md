## Description
* **Name:**  key_me_baby
* **Author:** Akir4
* **Artifact:** [Link](https://drive.google.com/open?id=1yO4j-7CEr2lvl3n7kkqGLSBNqsZlhmL_)
* **Points:** 159
* **Tag:** Forensics

<p align="center">
<img src="key_me_baby.png"/>
</p>

## Tools
* Firefox Version 60.5.1 https://www.mozilla.org/en-US/firefox/60.5.1/releasenotes/
* gdown 3.7.4 https://pypi.org/project/gdown/
* TShark (Wireshark) 2.6.7 https://www.wireshark.org/docs/relnotes/wireshark-2.6.7.html

## Writeup

```bash
root@1v4n:~/CTF/b002root19/Forensics# mkdir key_me_baby
root@1v4n:~/CTF/b002root19/Forensics# cd key_me_baby
root@1v4n:~/CTF/b002root19/Forensics/key_me_baby# gdown
oot@1v4n:~/CTF/b002root19/Forensics/key_me_baby# gdown https://drive.google.com/uc?id=1yO4j-7CEr2lvl3n7kkqGLSBNqsZlhmL_
Downloading...
From: https://drive.google.com/uc?id=1yO4j-7CEr2lvl3n7kkqGLSBNqsZlhmL_
To: /root/CTF/b002root19/Forensics/key_me_baby_GRANTED/data.pcapng
100%|█████████████████████████████████████████████████████████████| 36.7k/36.7k [00:00<00:00, 4.14MB/s]
root@1v4n:~/CTF/b002root19/Forensics/key_me_baby_GRANTED# file data.pcapng
data.pcapng: pcap-ng capture file - version 1.0
root@1v4n:~/CTF/b002root19/Forensics/key_me_baby_GRANTED# tshark -r data.pcapng -Y "usb.bus_id == 1 && usb.device_address == 71 && usb.transfer_type == 0x01" -T fields -e usb.capdata
Running as user "root" and group "root". This could be dangerous.

00:00:00:00:00:00:00:00


00:00:00:00

00:00:05:00:00:00:00:00

00:00:00:00:00:00:00:00

00:00:27:00:00:00:00:00

00:00:00:00:00:00:00:00

00:00:27:00:00:00:00:00

00:00:00:00:00:00:00:00

00:00:17:00:00:00:00:00

00:00:00:00:00:00:00:00

00:00:1f:00:00:00:00:00

00:00:00:00:00:00:00:00

00:00:15:00:00:00:00:00

00:00:00:00:00:00:00:00

00:00:12:00:00:00:00:00

00:00:00:00:00:00:00:00

00:00:12:00:00:00:00:00

00:00:00:00:00:00:00:00

00:00:17:00:00:00:00:00

00:00:00:00:00:00:00:00

00:00:2f:00:00:00:00:00

00:00:00:00:00:00:00:00

00:00:06:00:00:00:00:00

00:00:00:00:00:00:00:00

00:00:04:00:00:00:00:00

00:00:00:00:00:00:00:00

00:00:13:00:00:00:00:00

00:00:00:00:00:00:00:00

00:00:17:00:00:00:00:00

00:00:00:00:00:00:00:00

00:00:18:00:00:00:00:00

00:00:00:00:00:00:00:00

00:00:15:00:00:00:00:00

00:00:00:00:00:00:00:00

00:00:08:00:00:00:00:00

00:00:00:00:00:00:00:00

00:00:17:00:00:00:00:00

00:00:00:00:00:00:00:00

00:00:0b:00:00:00:00:00

00:00:00:00:00:00:00:00

00:00:08:00:00:00:00:00

00:00:00:00:00:00:00:00

00:00:0e:00:00:00:00:00

00:00:00:00:00:00:00:00

00:00:08:00:00:00:00:00

00:00:00:00:00:00:00:00

00:00:1c:00:00:00:00:00

00:00:00:00:00:00:00:00

00:00:30:00:00:00:00:00

00:00:00:00:00:00:00:00

root@1v4n:~/CTF/b002root19/Forensics/key_me_baby# nano get_flag.sh

#! /bin/bash

tshark -r data.pcapng -Y "usb.bus_id == 1 && usb.device_address == 71 && usb.transfer_type == 0x01" -T fields -e usb.capdata | sed '/^$/d;s/[[:blank:]]//g' > captured.txt && python2 bkeymap20.py > flag

root@1v4n:~/CTF/b002root19/Forensics/key_me_baby# chmod +x get_flag.sh
root@1v4n:~/CTF/b002root19/Forensics/key_me_baby# cat flag
b00t2root[capturethekey]
```

### Flag

`b00t2root[capturethekey]`
