@echo off

REM Start UDP server and client
start /B python3 python_udpserver.py
start /B python3 python_udpclient.py

REM Wait for some time to allow the servers to initialize
timeout /t 2 /nobreak

REM Start graphics script
start python3 python_graphics.py

REM Check if a process is listening on port 7501 and terminate it
netstat -ano | findstr ":7501" | find "LISTENING" >nul
if %ERRORLEVEL% EQU 0 (
    FOR /F "tokens=5" %%P IN ('netstat -ano ^| findstr ":7501" ^| find "LISTENING"') DO (
        echo Terminating process with PID %%P
        taskkill /F /PID %%P
    )
) else (
    echo No process is listening on port 7501
)

REM Kill the UDP server and client processes
taskkill /F /IM python3.exe /FI "WINDOWTITLE eq python_udpserver.py"
taskkill /F /IM python3.exe /FI "WINDOWTITLE eq python_udpclient.py"

echo done

