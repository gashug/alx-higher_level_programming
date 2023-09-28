#!/bin/bash
#  displays the size of the body of a URL response
curl -Is "$1" | grep Content-Length | cut -d: -f2
