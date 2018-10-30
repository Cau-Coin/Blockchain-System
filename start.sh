kill -9 `ps -ef | grep _manager_main.py | grep -v grep | awk '{print $2}'`

kill -9 `netstat -lntp | grep "0.0.0.0:5303" | grep -v grep | awk '{print $6}'`
kill -9 `netstat -lntp | grep "0.0.0.0:4444" | grep -v grep | awk '{print $6}'`

python3 blockchain_manager_main.py &
python3 network_manager_main.py &
