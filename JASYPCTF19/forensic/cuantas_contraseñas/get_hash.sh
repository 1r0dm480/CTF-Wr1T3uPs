#! /bin/bash

keepass2john NewDatabase.kdbx > Crack.hash && john -format=keepass Crack.hash > output && john --show Crack.hash  > output && cat output
