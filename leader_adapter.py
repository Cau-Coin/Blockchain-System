import requests
from flask import request, Flask

from block import *
from transaction import new_transaction

app = Flask(__name__)


@app.route("/transaction", methods=["POST", "GET"])
def receive_tx_msg():
    # http로 tx 받음
    if request.method == "POST":
        json_tx = request.json
        tx_data = json.dumps(json_tx)

        return new_transaction(tx_data)

    else:
        print("[Error] Not defined request method!")


def propose_block(last_block, tx_list, my_address):
    b = new_block(last_block, tx_list, my_address)
    block_json = b.to_json()

    # b를 http 전송
    dst = "http://" + my_address + ":4444" + "/block"

    requests.post(url=dst, json=block_json)
    pass


def broadcast_next_leader(next_leader, my_address):
    # http로 다음 리더 ip를 브로드캐스트
    dst = "http://" + my_address + ":4444" + "/leader"

    requests.post(url=dst, data=next_leader)


@app.route("/input", methods=["POST", "GET"])
def receive_tx_request():
    if request.method == "POST":
        json_data = json.dups(request.json)

        tx = new_transaction(json_data)

        return tx

    else:
        print("[Error] Not defined request method!")
