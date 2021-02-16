from flask import Flask, request
from flask_pymongo import PyMongo
from datetime import datetime

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
                "W_timestamp_in": ele["W_timestamp_in"],
                "W_timestamp_out": ele["W_timestamp_out"],
                "W_status": ele["W_status"],
                "W_UserID": ele["W_UserID"],
                "W_wristbandID": ele["W_wristbandID"],
                })

    return {"result": output}


@app.route('/update_shop_total_amount', methods=['PATCH'])
def update_total_amount():
    data = request.json

    filt = {'S_shopID': 0}
    updated_content = {"$set": {'S_total_amount' : data["S_total_amount"]}}

    S_myCollection.update_one(filt, updated_content)

    return {'result' : 'Updated successfully!'}


@app.route('/update_shop_limit_amount', methods=['PATCH'])
def update_limit_amount():
    data = request.json

    filt = {'S_shopID': 0}
    updated_content = {"$set": {'S_limit_amount' : data["S_limit_amount"]}}

    S_myCollection.update_one(filt, updated_content)

    return {'result' : 'Updated successfully!'}


@app.route('/update_shop_current_amount', methods=['PATCH'])
def update_current_amount():
    data = request.json

    filt = {'S_shopID': 0}
    updated_content = {"$set": {'S_current_amount' : data["S_current_amount"]}}

    S_myCollection.update_one(filt, updated_content)

    return {'result' : 'Updated successfully!'}


@app.route('/update_shop_time_limit', methods=['PATCH'])
def update_limit_limit():
    data = request.json

    filt = {'S_shopID': 0}
    updated_content = {"$set": {'S_time_limit' : data["S_time_limit"]}}

    S_myCollection.update_one(filt, updated_content)

    return {'result' : 'Updated successfully!'}


@app.route('/update_shop_lastest_time_enter', methods=['PATCH'])
def update_lastest_time_enter():
    data = request.json

    filt = {'S_shopID': 0}
    updated_content = {"$set": {'S_lastest_time_enter' : data["S_lastest_time_enter"]}}

    S_myCollection.update_one(filt, updated_content)

    return {'result' : 'Updated successfully!'}


@app.route('/update_shop_lastest_time_left', methods=['PATCH'])
def update_lastest_time_left():
    data = request.json

    filt = {'S_shopID': 0}
    updated_content = {"$set": {'S_lastest_time_left' : data["S_lastest_time_left"]}}

    S_myCollection.update_one(filt, updated_content)

    return {'result' : 'Updated successfully!'}


@app.route('/add_wristband', methods=['POST'])
def add_wristband():
    data = request.json
    myInsert = {
                "W_timestamp_in": 0,
                "W_timestamp_out": 0,
                "W_status": 0,
                "W_UserID": data["W_UserID"],
                "W_wristbandID": data["W_wristbandID"],
            }
    W_myCollection.insert_one(myInsert)
    return {'result': 'Created successfully'}


@app.route('/update_timestamp', methods=['PATCH'])
def update_timestamp():
    data = request.json

    filt = {'W_wristbandID': data["W_wristbandID"], 'W_status': 0}
    query = W_myCollection.find_one(filt)
    shop = S_myCollection.find_one({'S_shopID': 0})
    if (data["W_status"] == 0) :
        updated_content = {"$set": {'W_status' : 0, 'W_timestamp_in': datetime.timestamp(datetime.now())}}
        W_myCollection.update_one(filt, updated_content)
        return {'result' : shop["S_time_limit"]}
    elif (data["W_status"] == 1 and query["W_status"] == 0) :
        updated_content = {"$set": {'W_status' : 1, 'W_timestamp_out': datetime.timestamp(datetime.now())}}
        W_myCollection.update_one(filt, updated_content)
        return {'result': "Time out"}


@app.route('/member', methods=['POST'])
def user_data_input():
    data = request.json
    data['U_UserID'] = U_myCollection.find().count()
    U_myCollection.insert_one(data)
    return { "Result" : data['U_UserID'] }


@app.route('/queue', methods=['POST'])
def queue_data_input():
    data = request.json
    data['Q_queueID'] = Q_myCollection.find().count()
    data['Q_status'] = 0
    data['Q_receiveDate'] = 0
    data['Q_lenuser'] = len(data['Q_userID'])
    timestamp = datetime.timestamp(datetime.now())
    data['Q_createDate'] = timestamp
    Q_myCollection.insert_one(data)
    return {
            'Q_queueID' :  data['Q_queueID']
            ,'Q_createDate' : data['Q_createDate']
    }


@app.route('/queue', methods=['PATCH'])
def queue_data_update():
    data = request.json
    filt = { "Q_queueID": data['Q_queueID']}
    query = Q_myCollection.find_one(filt)
    output = {
        "Q_userID" : query["Q_userID"]
        ,"Q_shopID" : query["Q_shopID"]
        ,"Q_queueID" : query["Q_queueID"]
        ,"Q_status" : query["Q_status"]
        ,"Q_receiveDate" : query["Q_receiveDate"]
        ,"Q_lenuser" : query["Q_lenuser"]
        ,"Q_createDate" : query["Q_createDate"]
    }
    #if(output['Q_status']==1):
    #    return { "Result" : "QR already use" }
    timestamp = datetime.timestamp(datetime.now())
    output['Q_receiveDate'] = timestamp
    output['Q_status'] = 1
    name = []
    for i in range (len(output["Q_userID"])):
        filte = { "U_UserID": output["Q_userID"][i]}
        queryy = U_myCollection.find_one(filte)
        name.append(queryy["U_Username"])

    updated_content = {"$set":output}
    Q_myCollection.update_one(filt, updated_content)
    return {
        "Q_queueID" : output["Q_queueID"]
        ,"Q_lenuser" : output["Q_lenuser"]
        ,"Q_userID" : output["Q_userID"]
        ,"name" : name
    }


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='3000', debug=True)
