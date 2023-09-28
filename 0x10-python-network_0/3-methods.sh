#!/bin/bash
# script that displays all HTTP methods the server will accept
curl -ILs "$1" | grep Allow | cut -d " " -f2-
