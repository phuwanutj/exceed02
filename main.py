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
Wr_myCollection = mongo.db.Wr


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
    filt = { "U_Username": data['U_Username']}
    query = U_myCollection.find(filt).count()
    if(query > 0):
        return { "Result":"Username already use" }
    data['U_UserID'] = U_myCollection.find().count()
    U_myCollection.insert_one(data)
    return { "Result" : data['U_UserID'] }


@app.route('/queue', methods=['POST'])
def queue_data_input():
    data = request.json
    filt = { "U_Username": data['Q_Username'] , "U_password" : data['Q_password']}
    query = U_myCollection.find(filt).count()
    if(query == 0):
        return { "Result":"Wrong Username or Password" }
    query = U_myCollection.find_one(filt)
    data['Q_UserID'] = query["U_UserID"]

    filt = { "Q_UserID": data['Q_UserID'] , "Q_status" : 0}
    query = Q_myCollection.find(filt).count()
    if(query > 0):
        return { "Result":"This Username already in queue" }

    data['Q_queueID'] = Q_myCollection.find().count()
    data['Q_status'] = 0
    timestamp = datetime.timestamp(datetime.now())
    data['Q_updateDate'] = timestamp
    Q_myCollection.insert_one(data)
    return {
            'Q_queueID' :  data['Q_queueID']
            ,'Q_updateDate' : data['Q_updateDate']
    }


@app.route('/queue', methods=['PATCH'])
def queue_data_update():
    data = request.json
    filt = { "Q_queueID": data['Q_queueID']}
    query = Q_myCollection.find_one(filt)
    output = {
        "Q_UserID" : query["Q_UserID"]
        ,"Q_shopID" : query["Q_shopID"]
        ,"Q_queueID" : query["Q_queueID"]
        ,"Q_status" : query["Q_status"]
        ,"Q_updateDate" : query["Q_updateDate"]
        ,"Q_Username" : query["Q_Username"]
        ,"Q_password" : query["Q_password"]
    }
    timestamp = datetime.timestamp(datetime.now())
    output['Q_updateDate'] = timestamp
    output['Q_status'] = data["Q_status"]
    updated_content = {"$set":output}
    Q_myCollection.update_one(filt, updated_content)
    return {
        "Q_queueID" : output["Q_queueID"]
        ,"Q_userID" : output["Q_UserID"]
        ,"Q_Username" : output["Q_Username"]
    }


@app.route('/queue', methods=['GET'])
def queue_data_get():
    filt = { "Q_status" : 0 }
    query = Q_myCollection.find(filt)
    output = []
    for ele in query:
        output.append({
                "Q_UserID" : ele["Q_UserID"]
                ,"Q_Username" : ele["Q_Username"]
                ,"Q_queueID" : ele["Q_queueID"]
                ,"Q_status" : ele["Q_status"]
                ,"Q_updateDate" : ele["Q_updateDate"]
                ,"Q_shopID" : ele["Q_shopID"]
            })
    return { "Result" : output }


@app.route('/add_wristband', methods=['POST'])
def add_wristband():
    data = request.json
    filt = { "W_wristbandID": data['W_wristbandID'] , "W_status" : 0}
    query = W_myCollection.find(filt).count()
    if (query>0):
        return { "Result" : "This wristband is using now."}
    myInsert = {
                "W_timestamp_in": 0,
                "W_timestamp_out": 0,
                "W_status": 0,
                "W_UserID": data["W_UserID"],
                "W_wristbandID": data["W_wristbandID"],
            }
    W_myCollection.insert_one(myInsert)

    filt = { "Wr_wristbandID": data['Wr_wristbandID'] }
    query = Wr_myCollection.find_one(filt)
    output = {
            "Wr_wristbandID" : query["Wr_wristbandID"]
            ,"Wr_status" : 1
            }
    updated_content = {"$set":output}
    Wr_myCollection.update_one(filt, updated_content)

    return {'result': 'Created successfully'}


@app.route('/get_wristband', methods=['GET'])
def get_wristband():
    data = request.json
    filt = { "Wr_status" : data["Wr_status"]}
    query = Wr_myCollection.find(filt)
    output = []
    for ele in query:
        output.append(ele["Wr_wristbandID"])
    return {"Result" : output
            ,"Wr_status" : data["Wr_status"]}


@app.route('/get_graph1', methods=['GET'])
def get_graph1():
    data = request.json
    filt = { "Q_shopID" : data["Q_shopID"]}
    query = Q_myCollection.find(filt)
    output = []
    for ele in query:
        filt_u = { "U_UserID" : ele["Q_UserID"]}
        query1 = U_myCollection.find_one(filt_u)
        output.append(query1["U_age"])
    num = query.count()
    return {"Result" : output, "Amount": num}


@app.route('/get_graph2', methods=['GET'])
def get_graph2():
    data = request.json
    filt = { "Q_shopID" : data["Q_shopID"]}
    query = Q_myCollection.find(filt)
    output = []
    for ele in query:
        filt_u = { "U_UserID" : ele["Q_UserID"]}
        query1 = U_myCollection.find_one(filt_u)
        output.append(query1["U_gender"])
    num = query.count()
    return {"Result" : output, "Amount": num}


@app.route('/get_graph3', methods=['GET'])
def get_graph3():
    data = request.json
    filt = { "Q_shopID" : data["Q_shopID"]}
    query = Q_myCollection.find(filt)
    output = []
    for ele in query:
        filt_u = { "U_UserID" : ele["Q_UserID"]}
        query1 = U_myCollection.find_one(filt_u)
        output.append(query1["U_occupation"])
    num = query.count()
    return {"Result" : output, "Amount": num}


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='3000', debug=True)
