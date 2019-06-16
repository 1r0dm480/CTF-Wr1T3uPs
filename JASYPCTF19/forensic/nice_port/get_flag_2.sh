#! /bin/bash

strings captura.pcapng | grep "JASYP{.*" | awk '{print $2}'
