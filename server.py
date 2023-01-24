#IMPORTS:
from flask import Flask, render_template, redirect, flash, request
import jinja2
from melons.py import get_all_melons, find_melon_by_id

app = Flask(__name__):
app.jinja_env.undefined = jinja2.StrictUndefined


#ROUTES:

@app.route('/')
def home():
    return render_template("base.html")

# shows all melons 
@app.route('/melons') 
def melons():
    melon_list = get_all_melons()
    return render_template("melons.html", melon_list=melon_list)

# shows info about a specfic melon
@app.route('/melon/<melon_id>')
def melon_details(melon_id):
    melon = melons.find_melon_by_id(melon_id)
    return render_template("melon_details.html". melon=melon)

# adds a specfic melon to cart
@app.route('/add_to_cart/<melon_id>')
def add_to_cart(melon_id):
    return(f'{melon_id} added to the cart!')

# displays melon/s in the users cart
@app.route('/cart')
def cart():
    return render_template("cart.html")


# SERVER SETUP:
if __name__ == "__main__":
    app.env = "development"
    app.run(debug = True, port = 8000, host = "localhost")