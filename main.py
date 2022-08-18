from flask import request
from config import app
from service import *
from models import User, Order, Offer


@app.route('/users/', methods=['GET', 'POST'])
def page_get_users():
    if request.method == 'GET':
        return app.response_class(
            response=json.dumps(get_all(User), indent=4),
            status=200,
            mimetype="application/json"
        )
    elif request.method == 'POST':
        if isinstance(request.json, list):
            insert_data(User, request.json)
        elif isinstance(request.json, dict):
            insert_data(User, [request.json])
        else:
            return "Unsupported format. Please use .json or dict"
        return app.response_class(
            response=json.dumps(request.json, indent=4),
            status=200,
            mimetype="application/json")


@app.route('/users/<int:pk>', methods=['GET', 'PUT', 'DELETE'])
def page_get_user_by_id(pk):

    if request.method == 'GET':
        data = get_by_pk(User, pk)

        return app.response_class(
            response=json.dumps(data, indent=4, ensure_ascii=False),
            status=200,
            mimetype="application/json"
        )
    elif request.method == 'PUT':
        if isinstance(request.json, list):
            update_values(User, pk, request.json)
        elif isinstance(request.json, dict):
            update_values(User, pk, [request.json])
        else:
            return "Unsupported format. Please use .json or dict"
        return "Data recorded"
    elif request.method == 'DELETE':
        delete_by_pk(User, pk)
        return "Data deleted"


@app.route('/orders/', methods=['GET', 'POST'])
def page_get_all_orders():
    if request.method == 'GET':
        return app.response_class(
            response=json.dumps(get_all(Order), indent=4),
            status=200,
            mimetype="application/json"
        )
    elif request.method == 'POST':
        if isinstance(request.json, list):
            insert_data(Order, request.json)
        elif isinstance(request.json, dict):
            insert_data(Order, [request.json])
        else:
            return "Unsupported format. Please use .json or dict"
        return app.response_class(
            response=json.dumps(request.json, indent=4),
            status=200,
            mimetype="application/json")


@app.route('/orders/<int:pk>', methods=['GET', 'PUT', 'DELETE'])
def page_get_order_by_id(pk):
    if request.method == 'GET':
        data = get_by_pk(Order, pk)

        return app.response_class(
            response=json.dumps(data, indent=4, ensure_ascii=False),
            status=200,
            mimetype="application/json"
        )
    elif request.method == 'PUT':
        if isinstance(request.json, list):
            update_values(Order, pk, request.json)
        elif isinstance(request.json, dict):
            update_values(Order, pk, [request.json])
        else:
            return "Unsupported format. Please use .json or dict"
        return "Data recorded"
    elif request.method == 'DELETE':
        delete_by_pk(Order, pk)
        return "Data deleted"


@app.route('/offers/', methods=['GET', 'POST'])
def page_get_all_offers():
    if request.method == 'GET':
        return app.response_class(
            response=json.dumps(get_all(Offer), indent=4, ensure_ascii=False),
            status=200,
            mimetype="application/json"
        )
    elif request.method == 'POST':
        if isinstance(request.json, list):
            insert_data(Offer, request.json)
        elif isinstance(request.json, dict):
            insert_data(Offer, [request.json])
        else:
            return "Unsupported format. Please use .json or dict"
        return app.response_class(
            response=json.dumps(request.json, indent=4),
            status=200,
            mimetype="application/json")


@app.route('/offers/<int:pk>', methods=['GET', 'PUT', 'DELETE'])
def page_get_offer_by_id(pk):
    if request.method == 'GET':
        data = get_all_union(Offer, User, pk)

        return app.response_class(
            response=json.dumps(data, indent=4, ensure_ascii=False),
            status=200,
            mimetype="application/json"
        )
    elif request.method == 'PUT':
        if isinstance(request.json, list):
            update_values(Offer, pk, request.json)
        elif isinstance(request.json, dict):
            update_values(Offer, pk, [request.json])
        else:
            return "Unsupported format. Please use .json or dict"
        return "Data recorded"
    elif request.method == 'DELETE':
        delete_by_pk(Offer, pk)
        return "Data deleted"


if __name__ == '__main__':
    init_db()
    app.run(host="0.0.0.0", port=8000, debug=True)
