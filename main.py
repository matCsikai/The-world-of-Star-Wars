from common import get_required_planet_data, get_planet_data
from flask import Flask, render_template, request, redirect, url_for, session, escape
import requests

app = Flask(__name__)


@app.route("/")
def home_page():
    planets = get_required_planet_data('http://swapi.co/api/planets/?page=1')
    response = requests.get('http://swapi.co/api/planets/').json()
    next_page_id = ""
    previous_page_id = ""
    if response['next'] is not None:
        next_page = response['next']
        next_page_id = next_page[34:]
    if response['previous'] is not None:
        previous_page = response['previous']
        previous_page_id = previous_page[34:]
    return render_template("planets.html", planets=planets, previous_page_id=previous_page_id, next_page_id=next_page_id)


@app.route("/<page>")
def planets_page(page):
    planet_route = "http://swapi.co/api/planets/?page=" + page
    response = requests.get(planet_route).json()
    next_page_id = ""
    previous_page_id = ""
    if response['next'] is not None:
        next_page = response['next']
        next_page_id = next_page[34:]
    if response['previous'] is not None:
        previous_page = response['previous']
        previous_page_id = previous_page[34:]
    get_required_page = get_required_planet_data(planet_route)
    return render_template("planets.html", planets=get_required_page, previous_page_id=previous_page_id, next_page_id=next_page_id)


if __name__ == '__main__':
    app.run(debug=True)
