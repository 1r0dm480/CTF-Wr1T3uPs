#! /bin/bash

stegcracker perro_maligno.jpg /usr/share/wordlists/rockyou.txt && cat perro_maligno.jpg.out | grep "JASYP{.*"
