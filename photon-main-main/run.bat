@echo off
echo "in udp"
start python3 python_udpserver.py
start python3 python_udpclient.py
python3 python_graphics.py
echo "done"

