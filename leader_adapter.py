import requests
from flask import request, Blueprint

from block import *
from transaction import new_transaction

leader_adapter = Blueprint('leader_adapter', __name__)


@leader_adapter.route("/transaction", methods=["POST"])
def receive_tx_msg():
    # http로 tx 받음
    if request.method == "POST":
        tx_json = new_transaction(request.json).to_json()
        print(tx_json)
        return tx_json
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
