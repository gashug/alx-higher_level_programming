#!/bin/bash
# script that returns status code
curl -s -o /dev/null -w "%{http_code}" "$1"
