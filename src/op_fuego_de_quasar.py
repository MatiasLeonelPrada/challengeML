from flask import Flask, request
from satelite import Satelite
from trilateration import Trilateration
app = Flask(__name__)

@app.route('/topsecret', methods=['GET', 'POST'])
def top_secret():
    sat1 = Satelite('kenobi', 0, 0)
    sat2 = Satelite('skywalker', 3, 0)
    sat3 = Satelite('sato', 5, 3)
    trilateration = Trilateration([sat1, sat2, sat3])

    if request.method == 'POST':
        request_data = request.get_json()
        satellites = request_data["satellites"]
        trilat_distances = list()
        for satellite in satellites:
            trilat_distances.append(satellite['distance'])
        ship_pos = trilateration.get_location(trilat_distances)
        return str(ship_pos)
    else:
        return 'Invalid request.'

if __name__ == '__main__':
    # run app in debug mode on port 5000
    app.run(debug=True, port=5000)
