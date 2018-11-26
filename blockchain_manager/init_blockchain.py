# -*- coding: utf-8 -*-
from blockchain_manager.blockchain import Blockchain
from node_info import my_ip, init_leader

bc = Blockchain(my_ip, "caucoin_db", "blocks", "states", "coins", init_leader)
