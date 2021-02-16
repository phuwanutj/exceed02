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


@app.route('/find_all_user', methods=['GET'])
def find_all_user():

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


@app.route('/find_user', methods=['GET'])
def find_user():

    username = request.args.get('U_Username')
    password = request.args.get('U_password')
    filt = {"U_Username": username, "U_password": password}

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


@app.route('/find_all_queue', methods=['GET'])
def find_all_queue():

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


@app.route('/find_queue', methods=['GET'])
def find_queue():

    id = request.args.get('Q_quueueID')
    filt = {"Q_queueID": id}

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


@app.route('/update_shop_total_amount', methods=['PATCH'])
def update_total_amount():
    data = request.json

    filt = {'S_shopID': 0}
    updated_content = {"$set": {'S_total_amount' : data["S_total_amount"]}}

    S_myCollection.update_total_amount(filt, updated_content)

    return {'result' : 'Updated successfully!'}


@app.route('/update_shop_limit_amount', methods=['PATCH'])
def update_limit_amount():
    data = request.json

    filt = {'S_shopID': 0}
    updated_content = {"$set": {'S_limit_amount' : data["S_limit_amount"]}}

    S_myCollection.update_limit_amount(filt, updated_content)

    return {'result' : 'Updated successfully!'}


@app.route('/update_shop_current_amount', methods=['PATCH'])
def update_current_amount():
    data = request.json

    filt = {'S_shopID': 0}
    updated_content = {"$set": {'S_current_amount' : data["S_current_amount"]}}

    S_myCollection.update_current_amount(filt, updated_content)

    return {'result' : 'Updated successfully!'}


@app.route('/update_shop_time_limit', methods=['PATCH'])
def update_limit_limit():
    data = request.json

    filt = {'S_shopID': 0}
    updated_content = {"$set": {'S_time_limit' : data["S_time_limit"]}}

    S_myCollection.update_time_limit(filt, updated_content)

    return {'result' : 'Updated successfully!'}


@app.route('/update_shop_lastest_time_enter', methods=['PATCH'])
def update_lastest_time_enter():
    data = request.json

    filt = {'S_shopID': 0}
    updated_content = {"$set": {'S_lastest_time_enter' : data["S_lastest_time_enter"]}}

    S_myCollection.update_lastest_time_enter(filt, updated_content)

    return {'result' : 'Updated successfully!'}


@app.route('/update_shop_lastest_time_left', methods=['PATCH'])
def update_lastest_time_left():
    data = request.json

    filt = {'S_shopID': 0}
    updated_content = {"$set": {'S_lastest_time_left' : data["S_lastest_time_left"]}}

    S_myCollection.update_lastest_time_left(filt, updated_content)

    return {'result' : 'Updated successfully!'}
