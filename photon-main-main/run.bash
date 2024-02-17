pushd udp_files
echo "in udp"
python3 python_udpserver.py &
python3 python_udpclient.py &
popd
python3 python_graphics.py
echo "done"