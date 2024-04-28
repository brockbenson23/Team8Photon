#!/bin/bash

# Start UDP server and client in background
python3 python_udpserver.py &
SERVER_PID=$!  # Capture the PID of the server process
python3 python_udpclient.py &

# Wait for some time to allow the servers to initialize
sleep 2

# Start graphics script
python3 python_graphics.py

# Check if a process is listening on port 7501 and terminate it
if lsof -i :7501 >/dev/null 2>&1; then
    # Get the PID of the process
    PID=$(lsof -i :7501 | awk 'NR==2 {print $2}')
    # Terminate the process using SIGKILL
    echo "Terminating process with PID $PID"
    kill -9 "$PID"
else
    echo "No process is listening on port 7501"
fi

# Kill the UDP server and client processes
kill "$SERVER_PID"
killall python3 python_udpclient.py

echo "done"

