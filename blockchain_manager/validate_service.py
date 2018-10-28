# -*- coding: utf-8 -*-
def validate_tx(state_db, tx):
    return check_duplicated_eval(state_db, tx) and check_duplicated_score(state_db, tx)


def check_duplicated_eval(state_db, tx):
    # 1. get state list
    # 2. tx.subject == state.subject 인 것 중
    # 3. tx.user_id in state.user_id 검사
    # 4. 포함되지 않으면 return true, 포함되면 return false
    # (true 면 저장)

    result = state_db.find({
        "user_id": tx["user_id"], "evaluate_id": tx["evaluate_id"]
    }).count()

    if result == 0:
        return True
    else:
        print("Duplicated Evaluation!")
        return False


def check_duplicated_score(state_db, tx):
    # 1. get state list
    # 2. get state.score_list
    # 3. tx.user_id in state.score_list.user_id 검사
    # 4. 포함되지 않으면 return true, 포함되면 return false
    # (true 면 저장)

    result = state_db.find({
        "evaluate_id": tx["evaluate_id"],
        "scores": {"$elemMatch": {"user_id": tx["user_id"]}}
    }).count()

    if result == 0:
        return True
    else:
        print("Duplicated Score!")
        return False
