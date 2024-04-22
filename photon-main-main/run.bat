echo "python3 python_udpserver.py &"
echo "python3 python_udpclient.py &"

start python3 python_udpserver.py
start python3 python_udpclient.py
python3 python_graphics.py
echo "done"

