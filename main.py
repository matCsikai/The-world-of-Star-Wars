
from common import get_required_planet_data
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home_page():
    planets = get_required_planet_data()
    print(planets)
    return render_template("planets.html", planets=planets)


if __name__ == '__main__':
    app.run(debug=True)
