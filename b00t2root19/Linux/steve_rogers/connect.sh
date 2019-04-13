#!/bin/bash

exec socat tcp-connect:18.217.123.244:2604 file:`tty`,raw,echo=0
