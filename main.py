from flask import Flask, request
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://exceed_group02:tg52cdr5@158.108.182.0:2255/exceed_group02'
mongo = PyMongo(app)

U_myCollection = mongo.db.User
S_myCollection = mongo.db.Shop
C_myCollection = mongo.db.Category
Q_myCollection = mongo.db.Queue
W_myCollection = mongo.db.Wristband


@app.route('/find_user', methods=['GET'])
def find_user():

    filt = {}

    query = U_myCollection.find(filt)
    output = []

    for ele in query:
        output.append({
                "U_UserID": ele["U_UserID"],
                "U_Username": ele["U_Username"],
                "U_email": ele["U_email"],
                "U_age": ele["U_age"],
                "U_gender": ele["U_age"],
                "U_name": ele["U_name"],
                "U_surname": ele["U_surname"],
                "U_occupation": ele["U_occupation"],
                "U_catId": ele["U_catId"]
                })

    return {"result": output}


@app.route('/find_shop', methods=['GET'])
def find_shop():

    filt = {}

    query = S_myCollection.find(filt)
    output = []

    for ele in query:
        output.append({
                "S_shopID": ele["S_shopID"],
                "S_name": ele["S_name"],
                "S_total_amount": ele["S_total_amount"],
                "S_limit_amount": ele["S_limi_amount"],
                "S_current_amount": ele["S_current_amount"],
                "S_lastest_time_enter": ele["S_lastest_time_enter"],
                "S_lastest_time_left": ele["S_lastest_time_left"],
                "S_catId": ele["S_catId"],
                })

    return {"result": output}


@app.route('/find_category', methods=['GET'])
def find_category():

    filt = {}

    query = C_myCollection.find(filt)
    output = []

    for ele in query:
        output.append({
                "C_catId": ele["C_catId"],
                "C_catName": ele["C_catName"],
                })

    return {"result": output}


@app.route('/find_queue', methods=['GET'])
def find_queue():

    filt = {}

    query = Q_myCollection.find(filt)
    output = []

    for ele in query:
        output.append({
                "Q_queueID": ele["Q_queueID"],
                "Q_userID": ele["Q_userID"],
                "Q_shopID": ele["Q_shopID"],
                "Q_createDate": ele["Q_createDate"],
                "Q_receiveDate": ele["Q_receiveDate"],
                "Q_status": ele["Q_status"],
                })

    return {"result": output}


@app.route('/find_wristband', methods=['GET'])
def find_wristband():

    filt = {}

    query = W_myCollection.find(filt)
    output = []

    for ele in query:
        output.append({
                "W_timestamp": ele["W_timestamp"],
                "W_username": ele["W_username"],
                })

    return {"result": output}
