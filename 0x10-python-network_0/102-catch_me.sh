#!/bin/bash
# sends a JSON POST request to a URL passed as the first argument, and displays the body of the response.
if [[ $# -lt 2 ]]; then
  echo "Error: URL and file are missing."
  echo "Usage: ./101-post_json.sh <URL> <filename>"
  exit 1
fi

url="$1"
file="$2"

if [[ ! -f "$file" ]]; then
  echo "Error: File '$file' does not exist."
  exit 1
fi

response=$(curl -s -X POST -H "Content-Type: application/json" --data "@$file" "$url")

if jq -e . >/dev/null 2>&1 <<<"$response"; then
  echo "Valid JSON"
  echo "$response"
else
  echo "Not a valid JSON"
fi

#!/bin/bash
# makes a request that causes the server to respond with a message
response=$(curl -s -L -X PUT --data "user_id=98" -H "Origin: HolbertonSchool" 0.0.0.0:5000/catch_me)

message=$(echo "$response" | grep -o "You got me!")

printf "%s\n" "$message"
