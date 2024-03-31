import numpy as np
from Nasa import Nasa
from Gemini import Gemini
from decimal import *
import json
from io import BytesIO
from flask import Flask, render_template, request, jsonify
from vertexai.generative_models import Image
import base64

app = Flask(__name__)
nasa = Nasa()
gemini = Gemini()
layers = list(nasa.get_layers())
layer_data = {}


@app.route("/")
def home():
    return render_template("homepage.html")


@app.route("/form")
def form():
    return render_template("form.html")


@app.route("/secondpage")
def second_page():
    return render_template("secondpage.html")


@app.route(
    "/examine/<string:latitude>/<string:longitude>/<string:date>",
    methods=["GET"],
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
    data = analysis.split("\n\n")

    return jsonify(
        {
            "Chlorophyll": data[0],
            "DaytimeSST": data[1],
            "NighttimeSST": data[2],
            "PAR": data[3],
            "Analysis": data[4],
        }
    )


if __name__ == "__main__":
    app.run(port=5000, debug=True)
