#! /bin/bash

ltrace -o output ./REV03 AAAA && cat output | grep "shs2k19{.*" | awk -F'"' '{print $4}' > flag
