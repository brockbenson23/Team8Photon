echo "in udp"
python3 python_udpserver.py &
python3 python_udpclient.py &
popd

start python3 python_udpserver.py
start python3 python_udpclient.py
python3 python_graphics.py
echo "done"

