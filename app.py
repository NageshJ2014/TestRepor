from flask import Flask,jsonify,request,render_template
import json

# stores = [
#     {'name':"First Store",
#     'items':[
#              {'name':'st1_item1','price':70.0},
#              {'name':'st1_item2','price':200.0},
#              {'name':'st1_item3','price':2990.0}
#             ]
#     },
#     {'name':"Second Store",
#     'items':[
#              {'name':'Second_store_item1','price':70.0},
#              {'name':'Second_store_item2','price':200.0},
#              {'name':'Second_store_item3','price':2990.0}
#             ]
#     }
# ]

stores = [];

with open('Store.json', 'w') as fout:
    json.dump(stores, fout)


app = Flask(__name__)

@app.route ("/")
def home():
    return render_template("index.html")

#POST store
@app.route("/store", methods = ['POST'])
def create_store():
    request_data = request.get_json();
    name = request_data['name']
    new_store = {
                 'name':name,
                 'items':[]
                }
    for store in stores:
        if store['name'] == name:
            return jsonify({"Error Message":"Store {} Already Exists".format(name)}) , 409

    stores.append(new_store)
    with open('Store.json', 'w') as fout:
        json.dump(stores, fout)
    return jsonify(new_store),201;

# GET /store/<string:name>
@app.route("/store/<string:name>")
# @app.route("/store/<string:name>/")
def get_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(store);
    return jsonify({'message':"Store {} Not Found".format(name)}) , 500

# GET /store # Get all the stores
@app.route("/store/")
def get_stores():
    return jsonify({'stores':stores})

# POST /store/<string:name>/item {name:price}
@app.route("/store/<string:name>/item", methods = ['POST'])
def create_item_in_store(name):
    request_data = request.get_json()
    for store in stores:
        if store['name'] == name:
            new_item = {
                'name':request_data['name'],
                'price': request_data['price']
            }
            store['items'].append(new_item)
            with open('Store.json', 'w') as fout:
                json.dump(stores, fout)
            return jsonify(new_item)
    return  jsonify({'message':"Store {} Not Found".format(name)})


# GET /store/<string:name>/item <string:name>
@app.route("/store/<string:name>/item")
def get_items_in_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(store['items']);
    return jsonify({'message':"Store {} Not Found".format(name)})

app.run(debug='TRUE');
