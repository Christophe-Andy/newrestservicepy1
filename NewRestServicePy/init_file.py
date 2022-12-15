#!/usr/local/bin/python
# -*- coding: utf-8 -*-
#import py_eureka_client.eureka_client as eureka_client
from flask import Flask, jsonify, request, redirect, url_for
from flasgger import Swagger, LazyString, LazyJSONEncoder, swag_from
import json
from fonctions import *
from data_inout import *

app = Flask(__name__)
app.json_encoder = LazyJSONEncoder

"""your_rest_server_port = 5002  # uniquement pour l'enregistement eureka

eureka_client.init(
    eureka_server="http://admin:admin@38.242.196.119:8761/eureka/",
    app_name="StartTests0",  # only mentioned here. ca : christophe andy
    instance_ip="38.242.196.119",  # ip of the VM (server) or of the local machine (local)
    instance_port=your_rest_server_port,
)"""  # port defined for usage

swagger_template = dict(
    info={
        "title": LazyString(lambda: "Spring 0 Projet Stress Test BEAC 2022"),
        "version": LazyString(lambda: "0.1"),
        "description": LazyString(
            lambda: "Affichage de resultats de calculs suivant 2 exemples indicateurs."
        ),
    },
    host=LazyString(lambda: request.host),
)
swagger_config = {
    "headers": [],
    "specs": [
        {
            "endpoint": "api_calcul",
            "route": "/api_calcul.json",
            "rule_filter": lambda rule: True,
            "model_filter": lambda tag: True,
        }
    ],
    "static_url_path": "/flasgger_static",
    "swagger_ui": True,
    "specs_route": "/",
}

swagger = Swagger(app, template=swagger_template, config=swagger_config)

a = 5.54  # Peut provenir de bases de donnees ou de saisie
b = 10.45
e = 1.58


@swag_from("api_affichage.yml", methods=["GET"])
@app.route("/apiPy/GetIndicators/<indicateur>", methods=["GET"])
def affiche_indicateur(indicateur):
    # return jsonify(get_dico_elem_json(indicateurs, paramaff))
    indicateurs_dict = inventaire_ind(a, b, e)
    return indicateurs_dict[indicateur]


@swag_from("api_resultats.yml", methods=["GET"])
@app.route("/apiPy/GetResults/<resultats>", methods=["GET"])
def affiche_resultats(resultats):
    return resultats


@app.route("/apiPy/StartTests0", methods=["POST"])
def demarrer_tests0():
    content_type = request.headers.get("Content-Type")
    if content_type == "application/json":
        scenario = request.json
        # scenario_dict = json.load(senario)
        list_varm = [1, 2, 3, 4]

        df = file_to_dataframe("data_indratio_proto_st.xlsx", "calculs")
        results = stresstest0(list_varm, df)
        resultats_test = json.dumps(results)

        return (
            "Infos sur le scénario %s bien reçues et traitées !" % scenario["libelle"]
        )
    else:
        return "Content-Type not supported!"


@swag_from("api_passage.yml", methods=["POST"])
@app.route("/apiPy/SendResults", methods=["POST"])
def passage_variable():

    results = {}

    if request.method == "POST":
        try:
            varm1 = request.form["v1"]
            varm2 = request.form["v2"]
            varm3 = request.form["v3"]

            dico_varm = {"varm1": varm1, "varm2": varm2, "varm3": varm3}
            list_varm = [1, int(varm1), int(varm2), int(varm3)]

            df = file_to_dataframe("data_indratio_proto_st.xlsx", "calculs")
            results = stresstest0(list_varm, df)

            # results_json = jsonify(results)
            # entree_json = request.get_json()
            # lib = entree_json.get("libelle")

            # Retourner les resultats
            return redirect(url_for("affiche_resultats", resultats=results))
        except:
            results = {"Inconnu": "Inconnu"}
            return redirect(url_for("affiche_resultats", resultats=results))


@swag_from("api_stresstestcrud.yml")
@app.route("/apiPy/stresstestcrud/<val>", methods=["GET", "POST", "DELETE", "PUT"])
def passage_val(val):
    if request.method == "GET":
        return redirect(url_for("/apipoc/affichage/", param=val))


if __name__ == "__main__":
    app.run()
    # app.run(host="localhost", port=5000, debug=True)
