pushd udp_files
echo "in udp"
python python_udpserver.py &
python python_udpclient.py &
popd
python python_graphics.py
echo "done"
