#! /bin/bash

tshark -r data.pcapng -Y "usb.bus_id == 1 && usb.device_address == 71 && usb.transfer_type == 0x01" -T fields -e usb.capdata | sed '/^$/d;s/[[:blank:]]//g' > captured.txt && python2 bkeymap20.py > flag
