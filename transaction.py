import json
import uuid


def new_evaluate_tx(tx_id, tx_maker, timestamp, evaluate_id, dept, grade, semester, subject, takeyear, score,
                    review):
    eval_tx_data = {
        "tx_id": tx_id,
        "tx_maker": tx_maker,
        "timestamp": timestamp,
        "tx_type": "evaluate",
        "evaluate_id": evaluate_id,
        "dept": dept,
        "grade": grade,
        "semester": semester,
        "subject": subject,
        "takeyear": takeyear,
        "score": score,
        "review": review
    }

    return eval_tx_data


def create_evaluate_tx(tx_maker, timestamp, dept, grade, semester, subject, takeyear, score, review):
    tx_id = str(uuid.uuid4())
    evaluate_id = str(uuid.uuid4())

    return new_evaluate_tx(tx_id, tx_maker, timestamp, evaluate_id, dept, grade, semester, subject, takeyear, score,
                           review)


def new_comment_tx(tx_id, tx_maker, timestamp, evaluate_id, comment):
    comment_tx_data = {
        "tx_id": tx_id,
        "tx_maker": tx_maker,
        "timestamp": timestamp,
        "tx_type": "comment",
        "evaluate_id": evaluate_id,
        "comment": comment,
    }

    return comment_tx_data


def create_comment_tx(tx_maker, timestamp, evaluate_id, comment):
    tx_id = str(uuid.uuid4())

    return new_comment_tx(tx_id, tx_maker, timestamp, evaluate_id, comment)


def new_score_tx(tx_id, tx_maker, timestamp, evaluate_id, score):
    score_tx_data = {
        "tx_id": tx_id,
        "tx_maker": tx_maker,
        "timestamp": timestamp,
        "tx_type": "score",
        "evaluate_id": evaluate_id,
        "score": score,
    }

    return score_tx_data


def create_score_tx(tx_maker, timestamp, evaluate_id, score):
    tx_id = str(uuid.uuid4())

    return new_score_tx(tx_id, tx_maker, timestamp, evaluate_id, score)


def tx_to_json(tx):
    return json.dumps(tx)


def json_to_tx(json_tx):
    return json.loads(json_tx)


def create_tx(my_ip, json_input):
    data_input = json.loads(json_input)

    if data_input["tx_type"] == "evaluate":
        return create_evaluate_tx(my_ip, data_input["timestamp"], data_input["dept"], data_input["grade"],
                                  data_input["semester"], data_input["subject"], data_input["takeyear"],
                                  data_input["score"], data_input["review"])
    elif data_input["tx_type"] == "comment":
        return create_comment_tx(my_ip, data_input["timestamp"], data_input["evaluate_id"], data_input["comment"])
    elif data_input["tx_type"] == "score":
        return create_score_tx(my_ip, data_input["timestamp"], data_input["evaluate_id"], data_input["score"])
    else:
        print("Create tx is failed! - tx_type mismatched")
        return {}
