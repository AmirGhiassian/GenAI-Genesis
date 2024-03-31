from Nasa import Nasa
from Gemini import Gemini
from decimal import *
import json
from flask import Flask, request, jsonify

app = Flask(__name__)
nasa = Nasa()
gemini = Gemini()
layers = list(nasa.get_layers())
layer_data = {}


@app.route(
    "/examine/<string:latitude>/<string:longitude>/<string:date>", methods=["GET"]
)
def examine(latitude, longitude, date):

    nasa.set_time(date)
    nasa.set_cordinates(float(latitude), float(longitude))

    # nasa.show_image(layer)
    # latitude = 7.925600
    # longitude = 113.773700
    for layer in layers:
        layer_data[layer] = nasa.get_image(layer)

    analysis = gemini.multi_model_prompt(
        layer_data["Chlorophyll"],
        layer_data["DaytimeSST"],
        layer_data["NighttimeSST"],
        layer_data["PAR"],
    )
    return jsonify({"analysis": analysis})


@app.route("/test", methods=["GET"])
def test():
    return "help"


if __name__ == "__main__":
    app.run(port=5000, debug=True)
