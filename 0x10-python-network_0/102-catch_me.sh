#!/bin/bash
# makes a request that causes the server to respond with a message
response=$(curl -s -L -X PUT --data "user_id=98" -H "Origin: HolbertonSchool" 0.0.0.0:5000/catch_me)

message=$(echo "$response" | grep -o "You got me!")

printf "%s\n" "$message"
