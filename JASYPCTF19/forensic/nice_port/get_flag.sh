#! /bin/bash

tshark -r captura.pcapng -Y "ftp" | awk '{print $8}' | grep "JASYP{.*"
