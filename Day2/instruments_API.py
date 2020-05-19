from flask import Flask, json, abort, request
from instrument import GetInstruments, GetUser, addNewInstrument, addNewUser, add_key_to_instrument


app = Flask(__name__)


@app.route('/')
def index():
    return "Hello, World!"


@app.route('/instruments')
def get_all_instruments():
    response = app.response_class(
        response=json.dumps(GetInstruments()),
        status=200,
        mimetype='application/json'
    )
    return response


@app.route('/users')
def get_users():
    response = app.response_class(
        response=json.dumps(GetUser()),
        status=200,
        mimetype='application/json'
    )
    return response


@app.route('/add/instruments/<instrument_type>', methods=["GET", "POST"])
def add_new_instrument(instrument_type):
    addNewInstrument({"type": instrument_type})
    response = app.response_class(
        response=json.dumps({"type": instrument_type}),
        status=200,
        mimetype='application/json'
    )
    return response


@app.route('/add/user/<firstName>/<lastName>', methods=["GET", "POST"])
def add_new_user(firstName,lastName):
    addNewUser({"firstName": firstName, "lastName": lastName})
    response = app.response_class(
        response=json.dumps({"firstName": firstName, "lastName": lastName}),
        status=200,
        mimetype='application/json'
    )
    return response


@app.route('/instruments/<instrument_id>', methods=["GET"])
def get_instrument_by_id(instrument_id):
    instruments = GetInstruments()
    response = app.response_class(
        response=json.dumps(instruments[instrument_id]),
        status=200,
        mimetype='application/json'
    )
    return response


@app.route('/instruments/<instrument_id>/users/<user_id>', methods=["GET", "POST"])
def add_instrument_to_users(instrument_id, user_id):
    instruments = GetInstruments()
    users = GetUser()
    if instrument_id in instruments.keys() and user_id in users.keys():
        add_key_to_instrument("user_id", user_id, instrument_id)
    response = app.response_class(
        response=json.dumps({'user_id': user_id, "id": instrument_id}),
        status=200,
        mimetype='application/json'
    )
    return response

@app.route('/instruments/users/<user_id>', methods=["GET", "POST"])
def get_instruments_by_user_id(id):
    instruments = GetInstruments()
    newdict = {}
    for instrument in instruments.values():
        if instrument["user_id"] == id:
            newdict[instrument["id"]] = instrument
    response = app.response_class(
        response=json.dumps(newdict),
        status=200,
        mimetype='application/json'
    )
    return response

@app.route('/add/link/instruments/<id_instruments>', methods=["GET", "POST"])
def add_video_to_Instrument(id_instrument):
    link = request.args.get("link")
    instruments = GetInstruments()
    if id_instrument in instruments.keys():
        add_key_to_instrument("link", link, id_instrument)

    response = app.response_class(
        response=json.dumps({id_instrument: link}),
        status=200,
        mimetype='application/json'
    )
    return response


if __name__ == '__main__':
    app.run()

bwasglaf