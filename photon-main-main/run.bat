@echo off
echo "in udp"
<<<<<<< HEAD
python3 python_udpserver.py &
python3 python_udpclient.py &
popd
=======
start python3 python_udpserver.py
start python3 python_udpclient.py
>>>>>>> 6bd9a4f3f04aa781d0ba5024bd90964706fefb4f
python3 python_graphics.py
echo "done"

