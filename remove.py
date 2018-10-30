import pymongo

client = pymongo.MongoClient('0.0.0.0')
db = client["caucoin_db"]
chain = db["blocks"]
state = db["states"]
coin = db["coins"]

chain.remove({})
state.remove({})
coin.remove({})

