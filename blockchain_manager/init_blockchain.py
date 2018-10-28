# -*- coding: utf-8 -*-
from blockchain_manager.blockchain import Blockchain
from network_manager_main import my_ip, leader

bc = Blockchain(my_ip, "caucoin_db", "blocks", "states", leader)
