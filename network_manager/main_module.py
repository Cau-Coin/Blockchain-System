# -*- coding: utf-8 -*-
from flask import Flask, request
import json
import requests

from network_manager.db_manager import DataManager
from node_list import *

app = Flask(__name__)

ip_list = node_list
leader = "115.68.207.11"
data_manger = DataManager("0.0.0.0", "caucoin_db", "blocks", "states")


@app.route("/write_transaction", methods=["POST"])
def receive_input():
    dst = "http://0.0.0.0:5303/input"
    data = request.json
    requests.post(url=dst, json=data)
    return "Delivering tx data is completed!"


@app.route("/read_all_data", methods=["GET"])
def read_all_data():
    data = data_manger.get_all_data()
    return json.dumps(data)


@app.route("/read_one_data/<evaluate_id>", methods=["GET"])
def read_one_data(evaluate_id):
    data = data_manger.get_one_data(evaluate_id)
    return json.dumps(data)


@app.route("/transaction", methods=["POST"])
def send_tx():
    pass


@app.route("/transaction", methods=["POST"])
def receive_tx():
    pass


@app.route("/block", methods=["POST"])
def broadcast_block():
    pass


@app.route("/block", methods=["POST"])
def receive_block():
    pass


@app.route("/leader_update", methods=["POST"])
def broadcast_leader():
    pass


@app.route("/leader_update", methods=["POST"])
def receive_leader():
    pass


# @app.route('/read_block',methods=["POST"])
# def Read_AllData():
# 	if request.method == 'POST':
#
#
#
#
#
# @app.route('/input',methods=["POST"])
# def Test():
#
# 	print(request.json)
# 	return 'aaa'
# # 테스트용 route, 나는 준희한테 이 route를 통해서 보내게 된다. 단, 5305 port로.
#
#
# def BroadTransaction(j_input):
#
# 	for ipaddr in NODE_IP:
# 		# 여기서 반복문으로 requests.post를 통해서 데이터를 날리게 된다.
#
# 		#jsonObjectinput = json.loads(j_input)
# 		dst = 'http://' + ipaddr + ':5303' + '/input'
# 		#print(type(j_input))
# 		res = requests.post(url=dst,json=j_input)
#
#
#
#
# @app.route('/write_transaction',methods=["POST","GET"])
# def writeTransaction():
# 	if request.method == 'POST':
# 		jsonInput = request.json
# 		print(request.json)
# 		#dataInput = jsonInput.decode()
#
# 		#print(type(request.json))
# 		#dataInput = json.loads(jsonInput)
# 		#Json Data 형식으로 가져온다
#
# 		dataInput = json.dumps(jsonInput)
# 		# 기본적으로, request.json으로 받아오면, dict형태로 가져오는 것 같다
# 		# str로 바꾸기 위해서는 json.dumps로 바꾸면된다.
# 		# 나중에 혹시 json 문자열을 다시 dict형태로 바꾸려면
# 		# json.loads(input)을 주면된다.
# 		#if dataInput == null:
# 		#	return 'Null Input'
#
# 		#print('Test Write_Transaction 장건희 병신' + dataInput)
# 		#print ('Test write_transaction ' + dataInput)
#
# 		BroadTransaction(dataInput)
#
# 	return 'Send Successful'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4444)
