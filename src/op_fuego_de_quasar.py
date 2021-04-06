"""This module contains the API REST implemented using flask framework."""
from flask import Flask, request
from satelite import Satelite
from trilateration import Trilateration
from message_decoder import MessageDecoder
app = Flask(__name__)

STATUS_OK = 200
STATUS_ERROR = 404


@app.route('/topsecret', methods=['POST'])
def top_secret():
    """Flask API to obtain the location of the cargo ship and the message.
    """
    sat1 = Satelite('kenobi', 0, 0)
    sat2 = Satelite('skywalker', 3, 0)
    sat3 = Satelite('sato', 5, 3)
    trilateration = Trilateration([sat1, sat2, sat3])
    decoder = MessageDecoder()

    if request.method == 'POST':
        try:
            request_data = request.get_json()
            satellites = request_data["satellites"]
            trilat_distances = list()
            received_msgs = list()
            for satellite in satellites:
                trilat_distances.append(satellite['distance'])
                received_msgs.append(satellite['message'])
            ship_pos = trilateration.get_location(trilat_distances)
            message_decoded = decoder.get_messages(received_msgs)
            response = {
                "position": {
                    "x": str(ship_pos[0]),
                    "y": str(ship_pos[1])
                },
                "message": message_decoded
            }
        except Exception:
            response = {
                "msg": "The message or the position of the ship \
                    could not be determined. Please check the payload."
            }
            return response, STATUS_ERROR
        return response, STATUS_OK
    return 'Invalid request.', 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
